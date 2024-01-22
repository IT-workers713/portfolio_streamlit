import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "your username "
    password = "your password"
    receiver = "your mail "
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")



