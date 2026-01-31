from flask_mail import Message
from app.extensions import mail


def send_email_received(ticket):
    
    msg = Message(
        subject="Support Ticket Received: ",
        recipients=[ticket.std_email],
        body=f"""
Hello {ticket.std_name},

Your support ticket has been received successfully. Here are the details of your ticket:
Ticket ID: {ticket.id}
Issue Type: {ticket.issue_type}

We will get back to you shortly.
Best regards,
Support Team
"""
    )
    mail.send(msg)