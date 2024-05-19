num_1 = int(input("please select number 1 : "))
num_2 = int(input("please select number 2 : "))

print("--" * 20)

if num_1 != num_2:
    print("They are not equal")
    print(f"{min(num_1,num_2)} is the smallest")
    print(f"{max(num_1,num_2)} is the largest")
else:
    print("Both are equal")

print("--" * 20)

num_3 = int(input("please select number 3 : "))

print("--" * 20)
if num_1 == num_2 == num_3:
    print("All three are equal")
else:
    print("They are not equal")
    print(f"{min(num_1,num_2,num_3)} is the smallest in all three")
    print(f"{max(num_1,num_2,num_3)} is the largest in all three")
