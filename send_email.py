from email.mime.text import MIMEText
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
msg = MIMEText(contents, 'plain')
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

try:
	email_conn.sendmail(from_email, to_email, msg.as_string()) #Send a email.
	print("Successful!")
except smtplib.SMTPException:
	print("Error sending mail.")
email_conn.quit()