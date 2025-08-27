# Import required modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import schedule
import time
import csv

# ----------------- Step 1: Configuration -----------------
SENDER_EMAIL = "write_your_email_here"  # sender email
APP_PASSWORD = "your_password_herer"   # 16-character app password

SUBJECT = "Daily Report"
BODY = "Hello, this is an automated email sent from Python!"
ATTACHMENT_PATH = ""          # leave empty if none
CSV_FILE = "recipients.csv"            # list of emails
SCHEDULE_TIME = "21:55"                # 24h format, daily time

# ----------------- Step 2: Read recipients from CSV -----------------
def get_recipients():
    recipients = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # skip empty rows
                    recipients.append(row[0].strip())
    else:
        print(f"CSV file not found: {CSV_FILE}")
    return recipients

# ----------------- Step 3: Send Email Function -----------------
def send_email():
    recipients = get_recipients()
    if not recipients:
        print("No recipients found. Exiting.")
        return

    for receiver_email in recipients:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email
        msg['Subject'] = SUBJECT
        msg.attach(MIMEText(BODY, 'plain'))

        # Add attachment if exists
        if ATTACHMENT_PATH and os.path.exists(ATTACHMENT_PATH):
            attachment = open(ATTACHMENT_PATH, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(ATTACHMENT_PATH)}")
            msg.attach(part)
            attachment.close()

        # Connect and send
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
            print(f"Email sent to {receiver_email}")
            server.quit()
        except Exception as e:
            print(f"Failed to send email to {receiver_email}: {e}")

# ----------------- Step 4: Schedule Email -----------------
schedule.every().day.at(SCHEDULE_TIME).do(send_email)
print(f"Automation started. Emails will be sent daily at {SCHEDULE_TIME}. Press Ctrl+C to stop.")

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
