#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import time
import sys
import requests

def progress_bar(y=100):
	step = y/100
	out = ""
	for x in range(101):
		out = "#"*(x//5)
		out = "[" + out + "] Progress: " + str((step/100)*x) + "%."
		sys.stdout.write('\r'+out)
		sys.stdout.flush()
		time.sleep(0.1)
		
def progress_bar_status(status=200, summary=1000):
	progress = status/(summary/100)
	
	out = "#"*(progress//5)
	out = "[" + out + "] Progress: " + str(progress) + "%."
	sys.stdout.write('\r'+out)
	sys.stdout.flush()
	time.sleep(0.1)