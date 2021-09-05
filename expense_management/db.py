import sqlite3
import settings

def get_con():
	con = sqlite3.connect(settings.DBNAME)
	return con

def search_user_username_password(username, password):
	query = f"select * from user where username='{username}' and password='{password}'"
	con = get_con()
	cur = con.cursor()
	cur.execute(query)
	data = cur.fetchall()
	con.close()
	return data


def search_user(user_id, con=None):
	query = f"select * from user where id={user_id}"
	close_con = False
	if not con:
		con = get_con()
		close_con  = True
	cur = con.cursor()
	cur.execute(query)
	data = cur.fetchall()
	if close_con:
		con.close()
	return data

def insert_user(**data):
	query = "insert into user(id,username,password) values({user_id},'{username}','{password}')".format_map(data)
	con = get_con()
	con.execute(query)
	con.commit()
	data = search_user(data.get("user_id"),con)
	con.close()
	return data
