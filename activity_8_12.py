all_subs_results = []
no_of_sub = 5
no_of_test = 3


for i in range(1, no_of_sub + 1):
    marks_of_single_sub = []
    for ii in range(1, no_of_test + 1):
        mark = float(input(f"enter marks of sub {i} in test {ii} : "))
        marks_of_single_sub.append(mark)

    avg_marks = round((sum(marks_of_single_sub) / len(marks_of_single_sub)), 2)
    highest_marks = max(marks_of_single_sub)
    lowest_marks = min(marks_of_single_sub)

    print(f"\nIn sub {i}")
    print(f"{avg_marks=}")
    print(f"{highest_marks=}")
    print(f"{lowest_marks=}")
    print("\n")

    all_subs_results.extend(marks_of_single_sub)
    marks_of_single_sub.clear()


highest_in_all_subs = max(all_subs_results)
lowest_in_all_subs = min(all_subs_results)
avg_in_all_subs = round((sum(all_subs_results) / (no_of_sub * no_of_test)), 2)

print(f"{all_subs_results}")
print("\n")
print(f"{highest_in_all_subs=}")
print(f"{lowest_in_all_subs=}")
print(f"{avg_in_all_subs = }")


"""
EXTRA

finding the test number and subject of the highest marks
"""
x = all_subs_results.index(highest_in_all_subs) / no_of_test

if all_subs_results.index(highest_in_all_subs) + 1 > no_of_test:
    test_num = int((all_subs_results.index(highest_in_all_subs) + 1) / no_of_sub)
else:
    test_num = all_subs_results.index(highest_in_all_subs) + 1

sub_of_highest_marks = int(all_subs_results.index(highest_in_all_subs) / no_of_test) + 1


print(f"{sub_of_highest_marks=}")
print(f"{test_num=}")
