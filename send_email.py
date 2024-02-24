import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "pgtech246@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "pgtech246@gmail.com"
    context = ssl._create_default_https_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
