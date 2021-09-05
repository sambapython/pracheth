from db import insert_user, search_user_username_password
def create_user():
	user_id=input("Enter userid:")
	username=input("Enter username:")
	password=input("Enter password:")
	data= insert_user(user_id=user_id, username=username, password=password)
	return data

def login_user():
	username=input("Enter username:")
	password=input("Enter password:")
	data = search_user_username_password(username=username, password=password)
	return data

	



