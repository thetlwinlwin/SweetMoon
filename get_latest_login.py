user_name = input("Enter Username : ")  # Dave
textfile = open("users.txt")

end_of_file = False

while not end_of_file:
    user = textfile.readline().strip()  # Dave
    if user == "":
        print("User not Found")
        end_of_file = True
    if user == user_name:
        last_login = textfile.readline().strip()
        print(f"last login date {last_login}")
        end_of_file = True

textfile.close()
