# system resource monitoring
import psutil
# waiting time for the next checking
from time import sleep
# sending emails
import smtplib
# creating email content
from email.mime.text import MIMEText
# handling email attachments
from email.mime.multipart import MIMEMultipart


# Email settings
# Set the email address to send alerts from
EMAIL_ADDRESS = 'your_email@example.com'
# Set the email password
EMAIL_PASSWORD = 'your_password'
# Set the recipient email address for alerts
ALERT_EMAIL = 'alert_recipient@example.com'
# Set the SMTP server for sending emails
SMTP_SERVER = 'smtp.gmail.com'
# Set the SMTP server port
SMTP_PORT = 587

def send_alert(cpu_usage):
    subject = "CPU Usage Alert"
    body = f"CPU usage is at {cpu_usage}% "

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ALERT_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # Start TLS for security
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, ALERT_EMAIL, msg.as_string())
        server.quit()
        print(f"Alert sent: {body}")
    except Exception as e:
        print(f"Failed to send email alert: {e}")


def monitor_cpu():
    while True:
        # If cpu over 80% usage
        if psutil.cpu_percent(interval=1) > 80:
            send_alert(psutil.cpu_percent(interval=1))
        # Time between checks in seconds
        sleep(10)


if __name__ == "__main__":
    monitor_cpu()