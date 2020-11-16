#!/usr/bin/env python3

import os
import shlex
import subprocess as sp

cmd_strings = {
	'list files': 'ls -l',
	'os info': 'uname -a',
	'usb devices': 'lsusb -v'	
}

def blocking_run_cmd(cmd_string):
	cmd = sp.run(cmd_string.split())
	return cmd


def non_blocking_run_cmd(cmd_string):
	cmd = sp.call(cmd_string.split())
	return cmd


def main():
	pass


if __name__ == '__main__':
	main()
