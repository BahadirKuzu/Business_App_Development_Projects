import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def send_email(subject, body, receiver_email):
    # Retrieve email credentials and server settings from environment variables
    sender_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")
    host = os.getenv("EMAIL_HOST")
    port = int(os.getenv("EMAIL_PORT"))

    # Create a MIME multipart message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the email body in plain text format
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server using the host and port from the environment variables
    try:
        with smtplib.SMTP(host, port) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, password)  # Log in to the server
            server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
            print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # Example usage of the send_email function
    send_email("Test Subject", "This is a test email body.", "your_email@example.com")
