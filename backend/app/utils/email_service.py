import os 
import smtplib
from flask import Blueprint, request, jsonify
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()  # Load .env file

EMAIL_ADDRESS = os.environ.get('MAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

email_bp = Blueprint('email_bp', __name__)

# @email_bp.route('/ticket/received', methods=['POST'])
# def send_mail(to_email, subject, body):
#     """
#     reusable function to send an email
#     """
    
    
    
    

#     print("Sending email to...", to_email)  # for debugging

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         smtp.send_message(msg)


#         print("Email sent successfully to", to_email)