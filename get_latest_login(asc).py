user_name = input("Enter username : ")

textfile = open("users(asc).txt")
textfile.close()

lines = textfile.readlines()

user_index = 0
user_found = False

for i in range(len(lines)):
    user = lines[i].strip()
    if user == user_name:
        user_index = i
        user_found = True

latest_login = lines[user_index + 1]
print(f"latest login at {latest_login}")


if not user_found:
    print("User not Found")
