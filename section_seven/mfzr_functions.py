from functools import reduce


def capitalize_pet_name(item: str):
    return item.upper()


def pass_over_half(score):
    return score > 50


def accumulator(acc, item):
    return acc + item


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(capitalize_pet_name, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort(reverse=True)
print(list(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(pass_over_half, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
my_numbers.extend(scores)
print(reduce(accumulator, my_numbers, 0))
