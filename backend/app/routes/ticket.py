from flask import Blueprint, request, jsonify, render_template
from flask_mail import Message
from app.extensions import db, mail               # ← mail must be initialized
from app.models.models import SupportTicket

ticket_bp = Blueprint('ticket_bp', __name__)

@ticket_bp.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json() or {}

    new_ticket = SupportTicket(
        std_name=data.get('stdName'),
        std_email=data.get('stdEmail'),
        reg_number=data.get('regNumber'),
        issue_type=data.get('issueDescription')
    )

    try:
        db.session.add(new_ticket)
        db.session.commit()

        return jsonify({
            'message': 'Ticket created successfully',
            'ticket_id': new_ticket.id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to process request"}), 500

# Get All Tickets (GET)
@ticket_bp.route('/tickets/list', methods=['GET'])
def get_tickets():
    tickets = SupportTicket.query.all()

    results = []
    for ticket in tickets:
        results.append({
            'id': ticket.id,
            'reg_number': ticket.reg_number,
            'issue_type': ticket.issue_type,
            'created_at': ticket.created_at
        })

    return jsonify(results), 200
