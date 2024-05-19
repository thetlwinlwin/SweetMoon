import datetime

user_name = input("Enter your username : ")
date = str(datetime.date.today())

text_file = open("users_v2.txt", "a")
text_file.write("\n" + user_name)
text_file.write("\n" + date)

text_file.close()
