import smtplib

host = input("Enter your host: ") # Set SMTP server.
port = input("Enter your TLS port: ") # Set TLS port.
print("Your host is " + host)
print("Your TLS port is " + port)

email_conn = smtplib.SMTP(host, port) # Objection name
email_conn.ehlo()
email_conn.starttls() # SMTP commands will be Encrypted.
user_name = input("Enter your account: ")
password = input("Enter your password: ")
try:
	email_conn.login(user_name, password) # Log in SMTP server.
	print("Log in!")
except smtplib.SMTPAuthenticationError:
	print("Incorrect password or account.")

from_email = user_name
to_email = input("Enter the email that you want to send to.\n")
msg = input("contents:\n")
email_conn.sendmail(from_email, to_email, msg) #Send a email.
email_conn.quit()