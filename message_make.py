
init_times = 1 # The amount of visitors.
visitor_list = []
place_list = ["st", "nd", "rd", "th"]


unf_message = """Welcome {visitor}!
You're the {time}{var} visitor to visit our website."""

def message_make(names, times): # Make a message.  

	place_list = ["st", "nd", "rd", "th"]
	
	if times == 1:
		place = place_list[times - 1]
	elif times == 2:
		place = place_list[times - 1]
	elif times == 3:
		place = place_list[times - 1]
	else:
		place = place_list[3]

	new_message = unf_message.format(visitor = names[times - 1], var = place, time = times) # Show the vistor's name 
																							# and the place that the vistor visits 
																							# the website.
	return new_message
		
while True:

	new_visitor = input("Enter your name or enter quit to quit this program.\n ")
	
	if new_visitor == "quit":
		break
	else:
		visitor_list.append(new_visitor) # Record the visitor's name.
		message = message_make(visitor_list, init_times)
		init_times += 1 # Increase the amount of visitors.
		print(message)

print("Who has been visited our website?")
for name in visitor_list:
	print(name)
