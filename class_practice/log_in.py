from message import User_record
from format_mail_sending import Sending
obj = User_record()

while True:

	new_visitor = input("Enter your name or enter quit to exit this program.\n ")
	
	if new_visitor == "quit": # exit this program.
		break
	elif new_visitor == "manager": # Show all users.
		all_user = obj.get_user_details()
		print(all_user)
	else: # Add user
		welcome_message = obj.add_user(new_visitor)
		print(welcome_message)
		# Sending email.
		new_email = input("Enter your email: ")
		auto_sending = Sending()
		to_list = auto_sending.to_list(new_visitor, new_email)
		auto_sending.mail_sending(to_list)
		print("We send a mail to your email, please check it!")

print("Thanks!")
