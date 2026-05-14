numbers = [1, 2, 3, 2, 4, 1, 5]
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print("List after removing duplicates:", unique_list)