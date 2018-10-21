
#Acts as the database for our users, admin and attendant
#Here we are using a data structure ie lists
class users:
	def __init__(self, _id, username, password):
		self.id = _id
		self.username = username
		self.password = password
		
