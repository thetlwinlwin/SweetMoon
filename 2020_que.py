CAR_PRICE = 0
CAR_DISCOUNT_PERCENT = 0
TRADE_IN_VALUE = 0

user_choice = input("cars => saloon(s), hatch(h) or estate(e) : ").lower()

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
EXTRA_DISCOUNT_PRECENT = 0

extras = input("Do you want to add any extras? (y/n) : ").lower()
while extras == "y":
    extra = input(
        "(ls) luxury seats or (n) navigation or (p) parking or (b) bluetooth or (s) sound system : "
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
    extras = input("Do you want to add any more extras? (y/n) : ").lower()


is_old_customer = input("Are you old customer y/n : ").lower()

if is_old_customer == "y":
    CAR_DISCOUNT_PERCENT += 0.1
    EXTRA_DISCOUNT_PRECENT += 0.1

is_trade_in = input("Do you want to trade in your car y/n : ").lower()

if is_trade_in == "y":
    CAR_DISCOUNT_PERCENT += 0.05
    EXTRA_DISCOUNT_PRECENT += 0.05
    offer_amount = int(input("We offer : "))
    TRADE_IN_VALUE = offer_amount

AFTER_CAR_PRICE = CAR_PRICE - (CAR_PRICE * CAR_DISCOUNT_PERCENT) - TRADE_IN_VALUE
AFTER_EXTRA_PRICE = EXTRA_PRICE - (EXTRA_PRICE * EXTRA_DISCOUNT_PRECENT)
TOTAL_PRICE = AFTER_CAR_PRICE + AFTER_EXTRA_PRICE


print(f"Total price is {TOTAL_PRICE}")
