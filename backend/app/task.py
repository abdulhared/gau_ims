from app.extensions import celery, mail
from app.models.models import SupportTicket
from flask_mail import Message
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

def format_eat(dt):
    """Format datetime to East Africa Time (EAT) string."""
    if dt is None:
        return "N/A"
    eat_offset = 3  # EAT is UTC+3
    eat_time = dt + timedelta(hours=eat_offset)   
    return eat_time.strftime("%Y-%m-%d %H:%M:%S")

@celery.task(bind=True, max_retries=3)
def send_confirmation_email(self, ticket_id):
    """Send confirmation email to student"""
    try:
        from app import create_app
        app = create_app('development')  # or 'production' based on your environment

        with app.app_context():
            ticket = SupportTicket.query.get(ticket_id)

            if not ticket or not ticket.std_email:
                logger.error(f"Ticket with ID {ticket_id} not found or has no email.")
                return
            
            msg = Message(
                subject="Support Ticket Confirmation",
                recipients=[ticket.std_email],
                body=f"""Dear {ticket.std_name},

Your ticket #{ticket.id} has been received.

Reg. No: {ticket.reg_number}
Issue: {ticket.issue_type}
submitted at: {format_eat(ticket.created_at)}

We will get back to you shortly.

Support Team
Gau ICT Department """,
                html=f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"></head>
<body style="font-family:Arial,sans-serif;">
<div style="max-width:500px;margin:0 auto;background:white;padding:25px;border-radius:8px;">
<h2>Hello {ticket.std_name},</h2>
<p>Your support ticket has been received.</p>
<p style="padding:15px;background:#f0f4f8;border-left:4px solid #2c3e50;">
<strong>Ticket #{ticket.id}</strong><br>
Reg. No: {ticket.reg_number}<br>
Issue: {ticket.issue_type}<br>
Submitted: {format_eat(ticket.created_at)}
</p>
<p>We will get back to you soon.</p>
</div>
</body>
</html>"""
            )

            mail.send(msg)
            logger.info(f"Confirmation email sent to {ticket.std_email} for ticket ID {ticket_id}.")
            return {'status': 'success', 'ticket_id': ticket_id}
    except Exception as e:
        logger.error(f"Error sending email for ticket ID {ticket_id}: {str(e)}")
        raise self.retry(exc=e, countdown=60)  # Retry after 60 seconds
