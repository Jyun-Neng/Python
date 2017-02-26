# Get the file path that I need.
# Get the context of the file.

import os
class Use_template():
	def get_template_path(self, path):
		file_path = os.path.join(os.getcwd(), path) # File path.
		if not os.path.isfile(file_path): # Check whether the path is exist.
			raise Exception("This is not a valid path: %s"%(file_path))
		return file_path

	def get_template(self, path): 
		file_path = self.get_template_path(path)
		return open(file_path).read() # Get the contexts of the file.

	def render_context(self, template_string, context): 
		return template_string.format(**context) # ** Can read dictionary.

#file_ = 'template/message.txt'

#context = {
#	"name" : "Jyun-Neng",
#	"email" : "jyunnengji@gmail.com"
#}

#template_context = get_template(file_)

#print(render_context(template_context, context))
