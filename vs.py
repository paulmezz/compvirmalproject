#!/usr/bin/env python

import os
import sys 

target_dir = os.walk(sys.argv[1])
sig_file = sys.argv[2]

with open(sig_file,'rb') as signatures:
	lines = signatures.readlines()
	for singlesig in lines:
		print "imported: " + singlesig


for base_dir, sub_dirs, files in target_dir:
	for filename in files:
		print base_dir + "/" + filename
