import smtplib
import os
from email.message import EmailMessage
import json


def notification(message):
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ.get("MAIL_ADDRESS")
        smtp_server = os.environ.get("SMTP_SERVER")
        smtp_port = int(os.environ.get("SMTP_PORT"))
        receiver_address = message["username"]

        msg = EmailMessage()
        msg.set_content(f"mp3 file_id: {mp3_fid} is now ready!")
        msg["Subject"] = "mp3 download"
        msg["From"] = sender_address
        msg["To"] = receiver_address

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.send_message(msg)
        print("Mail sent")
    except Exception as err:
        print(err)
        return err
    finally:
        server.quit()
