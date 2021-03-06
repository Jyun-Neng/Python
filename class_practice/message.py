from use_template import Use_template
class User_record():
	user_detail = []
	def add_user(self, name):
		same_name = 0
		name = name[0].upper() + name[1:].lower()
		if len(self.user_detail) > 0: # Whether the user_detail is first add. 
			for detail in self.user_detail: # Browse the user_detail.
				if name == detail["name"]: # Whether the user has been added.
					reg_name = name
					reg_num = detail["num"]
					same_name += 1
			if same_name != 0: # The user is in the user_detail.
				num = reg_num + 1
				for detail in self.user_detail:
					if name == detail["name"]:
						detail["num"] = num
			else: # The user is not in the user_detail.
				details = {
						"name" : name,
						"num" : 1
					}
				num = 1
				self.user_detail.append(details)
		else: # First added.
			details = {
					"name" : name,
					"num" : 1
				}
			num = 1
			self.user_detail.append(details)
		message = self.make_message(name, num) # Show the welcome message.
		return message
	def get_user_details(self): # Show all the user.
		return self.user_detail
	def make_message(self, name, time): 
		template = Use_template()
		file_ = 'template/welcome_message.txt'
		unf_message = template.get_template(file_)
		new_message = unf_message.format(visitor = name, times = time)
		return new_message