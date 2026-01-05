import smtplib
import os
from email.message import EmailMessage

def send_email():
    # Fetch credentials from environment variables
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')

    msg = EmailMessage()
    msg['Subject'] = 'Scheduled Automated Email'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg.set_content('This is a scheduled email sent from a GitHub Action every 10 minutes.')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    send_email()