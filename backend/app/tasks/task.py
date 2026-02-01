from app.celery_app import celery_app

@celery_app.task(name="send_email_received_async")
def send_email_received_async(ticket_id):
    from app.models.models import SupportTicket
    from flask_mail import Message
    from app.extensions import mail
    from app.models.models import SupportTicket

    
    ticket = SupportTicket.query.get(ticket_id)
    if not ticket:
        return

    msg = Message(
        subject="Support Ticket Received",
        recipients=[ticket.std_email],
        body=f"""
Hello {ticket.std_name},

Your support ticket has been received successfully.

Ticket ID: {ticket.id}
Issue Type: {ticket.issue_type}

We will get back to you shortly.

Best regards,
Zula Support Team 
"""
    )

    with mail.connect() as conn:
        conn.send(msg)
