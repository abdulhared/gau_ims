from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.models import SupportTicket
from app.task import send_confirmation_email

ticket_bp = Blueprint('ticket_bp', __name__)

# Create Ticket (POST)
@ticket_bp.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()

    new_ticket = SupportTicket(
        std_name=data.get('stdName'),
        std_email=data.get('stdEmail'),
        reg_number=data.get('regNumber'),
        issue_type=data.get('issueDescription')
    )

    db.session.add(new_ticket)
    db.session.commit()

    # Send confirmation email asynchronously
    send_confirmation_email.delay(new_ticket.id)

    return jsonify({
        'message': 'Ticket created successfully',
        'ticket_id': new_ticket.id
    }), 201


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
