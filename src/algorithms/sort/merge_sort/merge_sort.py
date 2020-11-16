#!/usr/bin/env python3


def merge_sort(array):
	# Array of length 0 cannot be sorted
	# Array of length 1 is technically already sorted
	if len(array) <= 1:
		return array

	print(array)
	median = len(array) // 2

	# split the array about the median
	l, r = array[:median], array[median:]
	print(l)
	print(r)
	
	# keep splitting and sorting
	merge_sort(l)

	# keep splitting and sorting
	merge_sort(r)

	# counters for l, r, and array
	i, j, k = 0, 0, 0
	
	# increment up comparing values in l and r
	# appending the lesser values to array
	# until either l or r are exhausted
	while i < len(l) and j < len(r):
		print(array)
		if l[i] < r[j]:
			array[k] = l[i]
			i += 1
		else:
			array[k] = r[j]
			j += 1
		k += 1

	# clean up l and r if any values remain
	while i < len(l):
		print(array)
		array[k] = l[i]
		i += 1
		k += 1

	while j < len(r):
		print(array)
		array[k] = r[j]
		j += 1
		k += 1


def main():
	pass


if __name__ == '__main__':
	main()
