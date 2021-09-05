import db
def create_user_table():
	query = "create table user(id int, username varchar(250), password varchar(250))"
	con = db.get_con()
	con.execute(query)
	con.close()

def create_category_table():
	query = "create table category(id int, name varchar(250))"
	con = db.get_con()
	con.execute(query)
	con.close()

def create_product_table():
	query = "create table product(id int, name varchar(250), category_id int)"
	con = db.get_con()
	con.execute(query)
	con.close()

def create_expenses_table():
	query = "create table expense(id int, product_id int, cost decimal(10,5))"
	con = db.get_con()
	con.execute(query)
	con.close()
create_user_table()
create_category_table()
create_product_table()
create_expenses_table()