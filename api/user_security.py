from .user_model import users

user_list = [users(1, 'admin', 'admin1'), users(2, 'user', 'user1')]

username_mapping = {u.username: u for u in user_list}
userid_mapping = {u.id: u for u in user_list}


def authenticate(username, password):
	user = username_mapping.get(username, None)
	if user and user.password == password:
		return user
	return {'message':'Username and password entered, do not match'}, 401

def identity(payload):
	user_id = payload['identity']
	return userid_mapping.get(user_id, None)