#!/usr/bin/env python

import os
import sys

if len(sys.argv) != 3:
	sys.exit ("Usage: vs.py [TARGET DIR TO SCAN] [SIGNATURE FILE]")

target_dir = os.walk(sys.argv[1])
sig_file = sys.argv[2]

#Open the file sig_file as a binary read only
#then read in every line throwing them into the list
#called lines
with open(sig_file,'rb') as signatures:
	signaturelines = signatures.readlines()
	signaturelines = [s.strip() for s in signaturelines]

#Step through the given directory
for base_dir, sub_dirs, files in target_dir:
	for filename in files:
		#print "Scanning: " + base_dir + "/" + filename
		#Open each file
		with open(os.path.abspath(base_dir + "/" + filename), 'rb') as activescan:
			#pull in the lines from the file
			for scanline in activescan.readlines():
				#Step through the signatures pulled in above
				for singlesig in signaturelines:
					#The actual search
					if singlesig in scanline:
						print singlesig + " found in " + base_dir + "/" + filename
