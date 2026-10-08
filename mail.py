import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_alert_email(subject, body_text, recipient_email):
    sender_email = "yourgmail@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Use Google App Password here
    smtp_password = "your_16_digit_app_password"

    # Create Email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body_text, "plain"))

    try:
        print(f"Connecting to SMTP Server '{smtp_server}'...")

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        server.login(sender_email, smtp_password)

        server.sendmail(
            sender_email,
            recipient_email,
            msg.as_string()
        )

        server.quit()

        print(f"Alert notification sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to deliver notification: {e}")


# Example
send_alert_email(
    subject="CRITICAL: Memory Threshold Exceeded",
    body_text="Server RAM usage is currently at 94%. Immediate cleanup required.",
    recipient_email="sandeepsomavarapu535@gmail.com"
)
