#!/usr/bin/env python

import os
import sys 

target_dir = os.walk(sys.argv[1])
sig_file = sys.argv[2]

#Open the file sig_file as a binary read only
#then read in every line throwing them into the list
#called lines
with open(sig_file,'rb') as signatures:
	signaturelines = signatures.readlines()
#Just a debug to make sure it stepped through the lines
#	for singlesig in lines:
#		print "imported: " + singlesig

#Step through the given directory
for base_dir, sub_dirs, files in target_dir:
	for filename in files:
		print "Scanning: " + base_dir + "/" + filename
		with open("./" + base_dir + "/" + filename,'rb') as activescan:
			for scanline in activescan.readlines():
				for singlesig in signaturelines:
					if singlesig in scanline:
						print singlesig + " found in " + filename
