# 1 Square the numbers in the list
my_list = [5, 4, 3]

print(list(map(lambda num: num ** 2, my_list)))

# 2 Sort the list based on the second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(list(sorted(a, key=lambda x: x[1])))
