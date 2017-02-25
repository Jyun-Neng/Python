from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

host = "smtp.gmail.com" # Set SMTP server.
port = 587 # Set TLS port.

email_conn = smtplib.SMTP(host, port) # Objection name
email_conn.ehlo()
email_conn.starttls() # SMTP commands will be Encrypted.
user_name = input("Enter your account: ")
password = input("Enter your password: ")

try:
	email_conn.login(user_name, password) # Log in email on an SMTP server.
	print("Log in!")
except smtplib.SMTPAuthenticationError:
	print("Incorrect password or account.")

from_email = user_name
# Enter the information of this mail.
to_email = input("Enter the email that you want to send to.\n")
subject = input("Enter the subject of this mail.\n")
contents = input("contents:\n")
# Set the construction of this mail.
msg = MIMEMultipart("alternative")
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(contents, 'plain')) # Mail contents.
# Attachment file.
att = MIMEText(open('class_practice.py','r').read(), 'base64', 'utf-8') # The file should in the same folder.
att["Content-Type"] = 'application/octet-stream' # Can download.
att["Content-Disposition"] = 'attachment; filename = "class_practice.py"'
msg.attach(att)

try:
	email_conn.sendmail(from_email, to_email, msg.as_string()) #Send a email.
	print("Successful!")
except smtplib.SMTPException:
	print("Error sending mail.")
email_conn.quit()