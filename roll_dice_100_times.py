import random

roll = [0, 0, 0, 0, 0, 0]

# (1, 2, 3, 1, 4, 3, 3, 6, 1, 6, 6)
# 1 ka 3 khar
# 2 ka 1 khar
# 3 ka 3 khar
# 4 ka 2 khar
# 5 ka 0 khar
# 6 ka 3 khar
# [3, 1, 3, 2, 0, 3]

for _ in range(0, 100):
    random_result = random.randint(1, 6)
    # roll[random_result - 1] += 1

    if random_result == 1:
        roll[0] += 1
    if random_result == 2:
        roll[1] += 1
    if random_result == 3:
        roll[2] += 1
    if random_result == 4:
        roll[3] += 1
    if random_result == 5:
        roll[4] += 1
    if random_result == 6:
        roll[5] += 1

print(roll)

# for i in range(1, 7):
#     print(f"number {i} got {roll[i-1]} times")
