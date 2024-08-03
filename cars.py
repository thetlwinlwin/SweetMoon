HATCHBACK = 535_000
SALOON  = 495_000
ESTATE = 625_000


car_choice = int(input('car model? 1 or 2 or 3 : '))

if car_choice == 1:
    car_cost = HATCHBACK
elif car_choice == 2:
    car_cost = SALOON
elif car_choice == 3:
    car_cost = ESTATE
else:
    print('invalid input')


SEATS = 45_000
GPS = 5_500
PARKING = 10_000
BLUETOOTH = 350
SOUND = 1_000

extra_cost = 0

need_extra = input('you want any extra? y/n : ')

while need_extra =='y':
    ext = int(input('which extra>> 1.seats 2.gps 3.park 4.blue 5.sound : '))
    if ext == 1:
        extra_cost += SEATS  
    elif ext == 2:
        extra_cost += GPS
    elif ext == 3:
        extra_cost += PARKING
    elif ext == 4:
        extra_cost += BLUETOOTH
    elif ext == 5:
        extra_cost += SOUND
    else:
        print('invalid input')

    need_extra = input('you want more? y/n : ')

car_discount = 0
extra_discount = 0
old_car_price = 0

trade_in = input('trading in? y/n : ')
if trade_in == 'y':
    car_discount += (car_cost/100)*5
    extra_discount += (extra_cost/100)*5
    old_car_price = int(input('the price of old car is : '))
    while old_car_price <10000 or old_car_price >100_000:
        print('price doesn\'t match')
        old_car_price = int(input('the price of old car is : '))
        
    

is_old = input('old customer? y/n : ')
if is_old == 'y':
    car_discount += (car_cost/100)*10
    extra_discount += (extra_cost/100)*10
    

print(f'car price is now {car_cost-car_discount-old_car_price}')
print(f'extra price is now {extra_cost-extra_discount}')

















