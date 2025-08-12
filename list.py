#append items in list
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


print(f"Items in list: {my_list}")

#insert 15 at second position

my_list.insert(1, 15)
print(f"Updated list: {my_list}")

#extend list

my_list.extend([50,60,70])
print(f"Extended list: {my_list}")

#remove last item from list

my_list.pop()
print(f"Updated list with last item removed: {my_list}")

#sort list in ascending order

my_list.sort()
print(f"Sorted list in ASC: {my_list}")

#sort list in descending oder

my_list.sort()
new_list = sorted(my_list, reverse=True)
print(f"Sorted list in DESC: {new_list}")

#Index of value 30

index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")