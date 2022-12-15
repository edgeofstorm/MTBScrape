# from ..constants import EMAIL_FROM, EMAIL_TO, EMAIL_PASS
import smtplib
from email.message import EmailMessage
import os


EMAIL_FROM = os.environ.get("EMAIL_FROM", "enesekinci1907@gmail.com")
EMAIL_TO = os.environ.get("EMAIL_TO", "enesekinci1907@gmail.com")
EMAIL_PASS = os.environ.get('EMAIL_PASS', "itpdsxtommbjkeve")


class EmailService():

    @staticmethod
    def send_email(*, subject, html):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_FROM
        msg["To"] = EMAIL_TO

        msg.set_content('MTB Email')
        msg.add_alternative(html, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_FROM, EMAIL_PASS)
            smtp.send_message(msg)
