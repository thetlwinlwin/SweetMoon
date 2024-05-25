# arrays are the list of element of the same type


# 1D array => called "list"
sm_groceries = ["brocoli", "pasta", "cheese", "eggs"]
# pseudocode
# DECLARE SmGroceries: ARRAY[0:3] OF STRINGS
# SmGroceries[0] <- "brocoli"
# SmGroceries[1] <- "pasta"
# SmGroceries[2] <- "cheese"
# SmGroceries[3] <- "eggs"


# 2D array
# SM marks of 3 subs in 4 terms
# 1st term => 56,40,80  =>k
# 2nd term => 68,72,91  =>j
# 3rd term => 59,83,100 =>l
# 4th term => 98,71,67  =>m

sm_marks = [
    [56, 40, 80],
    [68, 72, 91],
    [59, 83, 100],
    [98, 71, 67],
]

# pseudocode
# DECLARE SmMarks : Array[0:3,0:2] OF INTEGER
# SmMarks[0,0] <- 56
# SmMarks[0,1] <- 40
# SmMarks[0,2] <- 80
# SmMarks[1,0] <- 68
# SmMarks[1,1] <- 72
# SmMarks[1,2] <- 91
# SmMarks[2,0] <- 59
# SmMarks[2,1] <- 83
# SmMarks[2,2] <- 100
# SmMarks[3,0] <- 98
# SmMarks[3,1] <- 71
# SmMarks[3,2] <- 67

for row in sm_marks:
    for element in row:
        print(element)

print(f"4th term 2nd sub is {sm_marks[3][1]} marks")
100, 100
100, 100

num_of_terms = int(input("Please enter the number of term : "))
num_of_sub = int(input("Enter number of sub for each term : "))

result = []

for col in range(num_of_sub):
    result.append([])
    for row in range(num_of_terms):
        marks = input("enter marks : ")
        result[col].append(marks)

print(f"final result is {result}")
