#!/usr/bin/env python3

import shutil
import os

def read_file(path_to_file):
	if os.path.exists(path_to_file) and os.path.isfile(path_to_file):
		f = open(path_to_file, 'r')
		data = f.read()
		f.close()
		return data


def read_lines_in_file(path_to_file):
	if os.path.exists(path_to_file) and os.path.isfile(path_to_file):
		f = open(path_to_file, 'r')
		for line in f.readlines():
			yield line


def write_to_file(path_to_file, data):
	if os.path.exists(path_to_file) and os.path.isfile(path_to_file):
		f = open(path_to_file, 'w')
		f.write(data)
		f.close()
		return True


def append_to_file(path_to_file, data):
	if os.path.exists(path_to_file) and os.path.isfile(path_to_file):
		f = open(path_to_file, 'a')
		f.write(data)
		f.close()
		return True


def create_file(path_to_file):
	if not os.path.exists(path_to_file) and not os.path.isfile(path_to_file):
		f = open(path_to_file, 'x')
		f.close()
		return True


def create_dir(path_to_dir):
	if not os.path.exists(path_to_dir):
		os.mkdir(path_to_dir)
		return True


def delete_file(path_to_file):
	if os.path.exists(path_to_file) and os.path.isfile(path_to_file):
		os.remove(path_to_file)
		return True


def copy_file(path_to_src, path_to_dst):
	if os.path.exists(path_to_src) and os.path.isfile(path_to_src):
		shutil.copyfile(path_to_src, path_to_dst)
		return True

def main():
	pass


if __name__ == '__main__':
	main()

