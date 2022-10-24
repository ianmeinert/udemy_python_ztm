def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    evens.sort()
    return evens.pop()


print(highest_even([8, 10, 2, 3, 4, 11]))
