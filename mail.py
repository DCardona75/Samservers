import smtplib
from email.message import EmailMessage

# Get form data
name = input("Name: ")
email = input("Email: ")
subject = input("Subject: ")
message = input("Message: ")

# Set up email message
msg = EmailMessage()
msg.set_content(f"From: {name}\nEmail: {email}\n\n{message}")
msg['Subject'] = subject
msg['From'] = email
msg['To'] = 'your_email@example.com'

# Set up SMTP settings
smtp_server = 'contact@samservers.com'
smtp_port = 995
smtp_username = 'contact@samservers.com'
smtp_password = 'Cardonapass1!'

# Send email
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.send_message(msg)

print("Email sent!")
