import string
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

User_dbs = {}

class Users(): 

	def __init__(self):
		

		self.detail = {}
		
	def put(self, username, password, role):
		
		if username in User_dbs:
			return {"message":"User already in system"}
		self.detail["username"] = username
		self.detail["role"] = role
		Hash = generate_password_hash(password)
		self.detail["password"] = Hash

		User_dbs[username] = self.detail
		return {"message":" {} : Added successfully".format(username)}

	def password_check(self, username, password):
		if username in User_dbs:
			result = check_password_hash(User_dbs[username]["password"], password)
			if result is True:
				return "Validated"
			return {'message': 'Invalid password'}
		return {"message": "No such user"}
	def get_user_by_username(self,username):
		if username in User_dbs:
			return User_dbs[username]
		return {"message":"No such user"}
	def get_all_users(self):
		return User_dbs