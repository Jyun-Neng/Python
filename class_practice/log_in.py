from message import User_record

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

print("Thanks!")
