import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()  # Load .env file


EMAIL_ADDRESS = os.environ.get('MAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'STUDENT SUPPORT'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'abdizehared17@gmail.com'
msg.set_content('Issue ticket number 0002 has been received and is being reviewed. Gau ICT Dept')

print("Sending test email...", EMAIL_ADDRESS) # for debugging 


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
    print("Test email sent successfully!")