results = []
no_of_sub = 1
no_of_test = 5


for i in range(1, no_of_test + 1):
    mark = float(input(f"enter test {i} marks : "))
    results.append(mark)

avg_marks = sum(results) / len(results)
highest_marks = max(results)
lowest_marks = min(results)

print(f"The average mark is {sum(results)/len(results)}")
print(f"The highest mark is {highest_marks} in test {results.index(highest_marks)+1}")
print(f"The lowest mark is {lowest_marks} in test {results.index(lowest_marks)+1}")
