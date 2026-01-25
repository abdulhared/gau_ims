# app/emails/ticket_email.py
from flask import Blueprint, jsonify
from app.extensions import db, mail
from app.models.models import SupportTicket
from flask_mail import Message
from datetime import datetime, timedelta
import traceback

email_bp = Blueprint('email_bp', __name__)


def format_eat(dt):
    if not dt:
        return "N/A"
    eat_time = dt + timedelta(hours=3)
    return eat_time.strftime('%Y-%m-%d %H:%M EAT')


@email_bp.route('send-confirmation/<ticket_id>', methods=['POST'])
def send_confirmation(ticket_id):
    ticket = SupportTicket.query.get_or_404(ticket_id)

    if not ticket.std_email:
        return jsonify({"error": "No email address for this ticket"}), 400

    try:
        msg = Message(
            subject="Support Ticket Received – Garissa University",
            recipients=[ticket.std_email],
            body=f"""Hello {ticket.std_name},

Your ticket #{ticket.id} has been received.

Reg. No: {ticket.reg_number}
Issue: {ticket.issue_type}
Submitted: {format_eat(ticket.created_at)}

We will get back to you soon.

Support Team
Garissa University College""",

            html=f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="font-family:Arial,sans-serif;line-height:1.5;color:#333;background:#f9f9f9;margin:0;padding:20px;">
<div style="max-width:500px;margin:0 auto;background:white;padding:25px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2c3e50;margin-top:0;">Hello {ticket.std_name},</h2>
<p>Your support ticket has been received.</p>
<p style="margin:20px 0;padding:15px;background:#f0f4f8;border-left:4px solid #2c3e50;">
<strong>Ticket #{ticket.id}</strong><br>
Reg. No: {ticket.reg_number}<br>
Issue: {ticket.issue_type}<br>
Submitted: {format_eat(ticket.created_at)}
</p>
<p>We will get back to you soon.</p>
<p style="margin-top:30px;font-size:14px;color:#555;">
Best regards,<br><strong>Support Team</strong><br>Garissa University College
</p>
</div>
</body>
</html>"""
        )
        mail.send(msg)
        return jsonify({"message": "Confirmation email sent"}), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Failed to send confirmation email"}), 500


@email_bp.route('send-resolved/<ticket_id>', methods=['POST'])
def send_resolved(ticket_id):
    ticket = SupportTicket.query.get_or_404(ticket_id)

    if ticket.status == 'resolved':
        return jsonify({"message": "Ticket is already resolved"}), 200

    if not ticket.std_email:
        return jsonify({"error": "No email address for this ticket"}), 400

    try:
        msg = Message(
            subject=f"Ticket #{ticket.id} – Resolved",
            recipients=[ticket.std_email],
            body=f"""Hello {ticket.std_name},

Your ticket #{ticket.id} has been resolved.

Issue: {ticket.issue_type}

If the problem persists, please create a new ticket.

Thank you for your patience.

Support Team
Garissa University College""",
            # html=... (add later if needed)
        )

        mail.send(msg)                    # send first
        ticket.status = 'resolved'
        db.session.commit()               # commit only if email succeeded

        return jsonify({
            "message": "Ticket marked resolved & email sent",
            "ticket_id": ticket.id,
            "status": ticket.status
        }), 200

    except Exception as e:
        db.session.rollback()
        traceback.print_exc()
        return jsonify({"error": "Failed to resolve and send email"}), 500