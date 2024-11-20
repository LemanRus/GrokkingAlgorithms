def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(find_smallest(arr)))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
print(selection_sort([5, 3, 6, 2, 10, -1, -5, 0, 0.6, 1.3, -0.56]))