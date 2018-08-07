#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import json
import logging 
from logging.config import dictConfig

ones = np.ones([6,6])

with open('log-config.json') as f:
	conf = f.read()
	conf = json.loads(conf)
	dictConfig(conf)


logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')