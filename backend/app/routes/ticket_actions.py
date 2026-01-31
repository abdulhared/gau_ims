from flask import Blueprint, request, jsonify
from app.models.models import SupportTicket
from app.extensions import db
from app.services.email_service import send_email_received

ticket_actions_bp = Blueprint('ticket_actions_bp', __name__)

@ticket_actions_bp.route('/tickets/actions', methods=['POST'])
def notify_ticket_received():
    data = request.get_json()

    ticket_id = data.get('ticket_id')
    action = data.get('action')

    if not ticket_id or not action:
        return jsonify({"error": "Invalid request"}), 400
    
    ticket = SupportTicket.query.get(ticket_id)
    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404
    if action == 'send_email':
        send_email_received(ticket)
        return jsonify({"message": "Notification sent"}), 200
    if action == 'resolved':
        ticket.status = 'resolved'
        db.session.commit()
        return jsonify({"message": "Ticket marked as resolved"}), 200
    return jsonify({"error": "Invalid action"}), 400 