# Sending mail class
# Send a format mail

from use_template import Use_template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

class Sending():

	def to_list(self, name, to_addr): # Create a user dictionary.
		user_list = {
			"name" : name,
			"email" : to_addr
		}
		return user_list
	def format_mail(self, to_list): # Create the context of this mail.
		template = Use_template()
		file_ = 'template/message.txt'
		template_msg = template.get_template(file_)
		new_msg = template.render_context(template_msg, to_list)
		return new_msg
	def mail_sending(self, to_list): # Sending mail.
		host = "smtp.gmail.com" # Set SMTP server.
		port = 587 # Set TLS port.
		email_conn = smtplib.SMTP(host, port) # Objection name
		email_conn.ehlo()
		email_conn.starttls() # SMTP commands will be Encrypted.
		user_name = # From_email.
		password = # From_email password.
		email_conn.login(user_name, password) # Log in email on an SMTP server.
		to_email = to_list["email"]
		from_email = user_name
		# The construction of this mail.
		msg = MIMEMultipart("alternative")
		msg['From'] = from_email
		msg['To'] = to_email
		msg['Subject'] = "Welcome!"
		msg.attach(MIMEText(self.format_mail(to_list), 'plain')) # Mail contents.
		email_conn.sendmail(from_email, to_email, msg.as_string()) #Sending.
		email_conn.quit()