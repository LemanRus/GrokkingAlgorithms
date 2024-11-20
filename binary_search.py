def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
my_list2 = [1, 3, 6, 9, 12, 15, 17, 23, 45, 56, 68, 78, 89, 98, 99]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

print(binary_search(my_list2, 12))
print(binary_search(my_list2, 0))
