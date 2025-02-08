import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using SMTP.
    :param sender_email: Email address of the sender
    :param sender_password: Password for the sender's email account
    :param recipient_email: Email address of the recipient
    :param subject: Subject of the email
    :param body: Body/content of the email
    """
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the body to the email
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server (e.g., Gmail)
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Log in to the email account
            server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # Get user input
    sender_email = input("Enter your email address: ").strip()
    sender_password = input("Enter your email password: ").strip()
    recipient_email = input("Enter the recipient's email address: ").strip()
    subject = input("Enter the email subject: ").strip()
    body = input("Enter the email body: ").strip()

    # Send the email
    send_email(sender_email, sender_password, recipient_email, subject, body)