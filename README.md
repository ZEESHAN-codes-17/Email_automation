# Python Email Automation Bot

This is a **Python Email Automation Bot** that can send emails automatically to multiple recipients daily. It supports optional attachments and reads recipients from a CSV file.

---

## Features

- Send emails to multiple recipients from a CSV file.
- Schedule daily emails at a specific time.
- Optional attachment support.
- Fully customizable subject and body of the email.

---

## Prerequisites

- Python 3.x installed
- `smtplib`, `email`, `schedule`, `csv` libraries (all included in standard Python)
- A **Gmail account** with **2-Step Verification enabled**
- A **Google App Password** (16-character) for your account

---

## Setup

1. **Clone this repository** or download the files.
2. **Create your own CSV file** with recipient emails:
   - Name the file: `recipients.csv`
   - Each row should contain **one email address**.
   - Example:

```
friend1@example.com
friend2@example.com
friend3@example.com
```

3. **Update your Python script**:
   - Replace placeholders in the script:

```python
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_char_app_password"
SUBJECT = "Your email subject"
BODY = "Your email body"
ATTACHMENT_PATH = ""  # leave empty if no attachment
CSV_FILE = "recipients.csv"
SCHEDULE_TIME = "21:55"  # 24-hour format
```

> ⚠️ **Do not share your real email or app password publicly.**

4. **Install required libraries** (if not already installed):
```bash
pip install schedule
```

---

## How to Use

1. Make sure your **CSV file** (`recipients.csv`) is in the same folder as the script.
2. Open terminal / command prompt in the script's folder.
3. Run the script:
```bash
python email_bot.py
```
4. The script will **send emails daily** at the scheduled time.
5. Press `Ctrl+C` to stop the automation.

---

## Notes

- **Attachments:** If you want to attach a file, update `ATTACHMENT_PATH` in the script with the file path.  
- **Email body & subject:** Customize them as needed in the script.  
- **Security:** For professional use or GitHub, use **environment variables** instead of hardcoding your credentials.  

---

Enjoy your automated email bot! 🚀
