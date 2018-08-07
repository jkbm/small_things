#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from utils import progress_bar_status

if __name__ == "__main__":
	s = 1000
	for x in range(0, (s+1), 50):
		progress_bar_status(x, s)
"""
from time import sleep

for i in range(10):
	print i,
	sleep(2)
	"""