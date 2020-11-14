#!/usr/bin/env python3


"""
	Iterate through project files
		create dictionary with glossary files
	Compile dictionary to navigable markdown doc.
"""

import os

path_to_this_dir = os.getcwd()
this_dir = path_to_this_dir.split('/')[-1]


def gather_glossary(f_tree_root):
	"""
		Input: f_treestr -> 

		Output: 
	"""
	glossary_entries = {}

	for root, dirs, files in os.walk(f_tree_root, onerror=print, followlinks=False):
		for name in files:
			if name == 'entry.gls':
				file_name = '/'.join([root, name])
				print(file_name)
				
				for node in file_name.split('/')[1:]:
					print(node)

	return glossary_entries

def main():
	"""
		Display navigable glossary
	"""
	glossary = gather_glossary('.')


if __name__ == '__main__':
	main()
