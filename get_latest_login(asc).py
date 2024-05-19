user_name = input("Enter username : ")

textfile = open("users(asc).txt")
lines = textfile.readlines()[::-1]
textfile.close()

user_not_found = True

for i in range(len(lines)):
    user = lines[i].strip()
    if user == user_name:
        print(f"last login is {lines[i-1]}")
        user_not_found = False
        break

if user_not_found:
    print("User not Found")
