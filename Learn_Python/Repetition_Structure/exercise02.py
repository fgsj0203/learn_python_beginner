login_name = str(input("Enter with your name: "))
password_login = str(input("Enter with your password: "))

while login_name == password_login:
    print("Login invalid, try again!")
    login_name = str(input("Enter again your name: "))
    password_login = str(input("Enter with your password: "))

print("Your login is: ", login_name, " and ", password_login)
