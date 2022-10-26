# Exercise: Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Create a set and add the value if the value occurs in some_list  more than once
duplicates = set([value for value in some_list if some_list.count(value) > 1])
print(f'{len(duplicates)} duplicates: {duplicates}')
