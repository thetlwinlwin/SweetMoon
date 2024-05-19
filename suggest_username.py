user_input = input("Enter some name in your mind : ")

while len(user_input) < 4 or len(user_input) > 12:
    print("\n Invalid Input. Try Again\n")
    user_input = input("Enter some name in your mind : ")
