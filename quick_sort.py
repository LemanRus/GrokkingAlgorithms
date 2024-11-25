def fast_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		less = [x for x in arr[1:] if x < pivot]
		great = [x for x in arr[1:] if x > pivot]
		return fast_sort(less) + [pivot] + fast_sort(great)
		

print(fast_sort([1, 78, 5, -5, 87, -13, -76, -90]))