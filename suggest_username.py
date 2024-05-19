user_input = input("Enter some name in your mind : ")

while len(user_input) < 4 or len(user_input) > 12:
    print("\n Invalid Input. Try Again\n")

    print(f'\nTry like "cheeselover {user_input}"')
    print(f'\nTry like "Moonlit Sun {user_input}"')
    print(f'\nTry like "Hello Darkness my old friend {user_input}"\n')

    user_input = input("Enter some name in your mind : ")

print("username is accepted")
