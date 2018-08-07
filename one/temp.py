##!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import utils


path = os.curdir
files = os.listdir(path)
print files

if __name__ == "__main__":
	utils.progress_bar()