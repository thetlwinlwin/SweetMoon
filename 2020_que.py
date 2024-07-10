print("Hello WElCOMe from car paradise\n")

CAR_PRICE = 0
CAR_DISCOUNT = 0

user_choice = input("cars => saloon(s), hatch(h) or estate(e) : ")

if user_choice == "s":
    CAR_PRICE = 495000
elif user_choice == "h":
    CAR_PRICE = 535000
elif user_choice == "e":
    CAR_PRICE = 625000
else:
    print("invalid input")
    exit()


EXTRA_PRICE = 0
EXTRA_DISCOUNT = 0

extras = input("Do you want to add any extras? (y/n) : ")
while extras == "y":
    extra = input(
        "(ls) Set of luxury seats or (n) Satellite navigation or (p) Parking sensors or (b) Bluetooth connectivity or (s) Sound system : "
    ).lower()
    if extra == "ls":
        EXTRA_PRICE += 45000
    elif extra == "n":
        EXTRA_PRICE += 5500
    elif extra == "p":
        EXTRA_PRICE += 10000
    elif extra == "b":
        EXTRA_PRICE += 350
    elif extra == "s":
        EXTRA_PRICE += 1000
    else:
        print("Invalid input")
        exit()
    extras = input("Do you want to add any more extras? (y/n) : ")
