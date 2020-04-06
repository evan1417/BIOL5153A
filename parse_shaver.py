#! /usr/bin/env python3

import csv

#define shaver_etal 
infile = "shaver_etal.csv"

#open shaver
with open('shaver_tabbed.txt', 'w') as output:

	with open(infile, 'r') as shaver:
		#create a csv reader object
		reader = csv.reader(shaver, delimiter=',')
		for line in reader:
       		# skip blank lines
			if not line:
				continue
			else:
				#print(line)
				linewriter = csv.writer(output, delimiter = '\t', quotechar)
				linewriter = csv.writer()
            
