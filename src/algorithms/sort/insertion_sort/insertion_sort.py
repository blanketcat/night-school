#!/usr/bin/env python3

# Really feel like I should be able to do this without
# using j.

def insertion_sort(array):
	for i in range(1, len(array)):
		key = arr[i]
		
		j = i - 1
		
		while j >= 0 and array[j] > key:
			array[j + 1] = array[j]
			j -= 1

		array[j+1] = key


def main():
	pass


if __name__ == '__main__':
	main()
