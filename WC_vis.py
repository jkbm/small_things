#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import csv
 
file = open('WorldCupMatches.csv')
reader = csv.reader(file)
data = list(reader)
adata = data[:101]
labels = data[0]
values = adata[1:]
print(labels)
