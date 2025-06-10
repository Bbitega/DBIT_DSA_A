def revs_list(list):
    list.reverse()
    return list

my_list=[1, 2, 3, 4, 5]
revs_list=revs_list(my_list.copy())

print("Original list: ",my_list)
print("Reversed list: ",revs_list)

