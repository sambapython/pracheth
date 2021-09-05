import sys
print("WELCOME TO EXPENSE MANAGEMENT")
from home import home_menu, top_menu
from user_menu import create_user, login_user
option = home_menu()
if option == "1":
		data = create_user()
		if not data:
			print("user not created successfullly.")
		else:
			print(data)
			print("user created successfully.")
		home_menu()
elif option == "2":
	data = login_user()
	if data:
		print("LOGIN success")
		option = top_menu()
		if option == "1":
			product_menu()
		elif option == "2":
			category_menu()
		elif option == "3":
			expense_menu()
		elif option == "Q":
			sys.exit(0)

	else:
		print("LOGIN FAIL")
		home_menu()

elif option == "Q":
	sys.exit(0)
