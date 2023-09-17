import smtplib
import os
import imghdr
from email.message import EmailMessage

def send_email(image_loc):
    USERNAME = os.getenv("PY_USERNAME")
    PASSWORD = os.getenv("PY_PASSWORD")
    RECIEVER = os.getenv("PY_USERNAME")

    email_message = EmailMessage()
    email_message['Subject'] = "PythonShowcase"
    email_message['From'] = USERNAME
    email_message['To'] = RECIEVER

    email_message.set_content("Webcam motion alert has been triggered!")

    with open(image_loc, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail_send = smtplib.SMTP_SSL('smtp.gmail.com')
    with smtplib.SMTP_SSL('smtp.gmail.com') as gmail_send:
        # uncomment == DEBUG
        # gmail_send.set_debuglevel(1)
        gmail_send.login(USERNAME, PASSWORD)
        gmail_send.send_message(email_message)

if __name__ == "__main__":
    send_email(image_loc="images/image_22.png")