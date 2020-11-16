#!/usr/bin/env python3

"""
	This is technically a Header Linked List

	These are really too low level to be useful in python unless you were
	dealing with an array that was large enough to warrant storing it in 
	sections in files or a database
	
	Including for "completeness" in the data structures collection
	Will become relevant if other langauges are ever added to the repo
"""

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
	def __init__(self, head=None):
		self.arg = arg
		self.head = head
		

	def prepend(self, data):
		next_node = self.head
		self.head = Node(val=data, next_node=next_node)

	def traverse(self):
		cur_node = self.head

		if cur_node is not None:
			node_count = 1
			while next_node is not None:
				node_count += 1

	def append(self, data):
		pass

	def length(self):
		cur_node = self.head

		if cur_node is not None:
			node_count = 1
			while next_node is not None:
				node_count += 1


	def has_value(self, data):
		pass

	def insert(self, data, start_node):
		pass

	def delete(self, node):
		pass


def main():
	pass


if __name__ == '__main__':
	main()
