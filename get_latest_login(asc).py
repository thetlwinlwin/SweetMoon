user_name = input("Enter username : ")

textfile = open("users(asc).txt")

end_of_file = False
latest_login = None

while not end_of_file:
    user = textfile.readline().strip()
    if user == "":
        end_of_file = True
    if user == user_name:
        login_date = textfile.readline().strip()
        latest_login = login_date

if latest_login:
    print(f"latest login is {latest_login}")
else:
    print("User not found")

textfile.close()
