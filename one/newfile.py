##!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import utils

current_time = time.localtime()

print("Year progress:")
utils.progress_bar_status(current_time[1], 12)
print("\nMonth progress:")
utils.progress_bar_status(current_time[2], 31)
print("\nDay progress:")
utils.progress_bar_status(current_time[3], 24)