"""
email_handler.py
Keyword: net_api_email

Wysyłanie wyników e-mailem w załączniku do wybranych odbiorców.
Używamy modułu smtplib w uproszczeniu.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

def send_email_with_attachment(host, port, login, password, to_addr, subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg["From"] = login
    msg["To"] = to_addr
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    msg.attach(MIMEText(body))

    if attachment_path:
        part = MIMEBase("application", "octet-stream")
        with open(attachment_path, "rb") as f:
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={attachment_path}")
        msg.attach(part)

    try:
        smtp = smtplib.SMTP(host, port)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(login, password)
        smtp.sendmail(login, to_addr, msg.as_string())
        smtp.close()
        return True
    except Exception as e:
        print(f"Błąd wysyłania maila: {e}")
        return False
