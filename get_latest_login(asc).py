user_name = input("Enter username : ")

textfile = open("users(asc).txt")

# lines = textfile.readlines()

# # user_index = 0
# # user_found = False

# # for i in range(len(lines)):
# #     user = lines[i].strip()
# #     if user == user_name:
# #         user_index = i
# #         user_found = True

# # latest_login = lines[user_index + 1]
# # print(f"latest login at {latest_login}")

# # if not user_found:
# #     print("User not Found")


user_found = False

while not user_found:
    user_logins = []
    user = textfile.readline().strip()
    if user == "":
        break
    if user == user_name:
        login_date = textfile.readline().strip()
        user_logins.append(login_date)

if user_found:
    print(f"latest login is {user_logins[-1]}")
else:
    print("User not Found")


textfile.close()
