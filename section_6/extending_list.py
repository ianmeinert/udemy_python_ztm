class SuperList(list):
    pass


super_list1 = SuperList()

super_list1.append(5)
print(len(super_list1))
print(issubclass(SuperList, list))
