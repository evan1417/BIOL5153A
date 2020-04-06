#! /usr/bin/env python3

# importing csv module 
import csv

#defining file 
my_file = "/users/evan/desktop/python_homework/watermelon.gff"

# storing each line as a list variable
watermelon = []

# opening the file and reading it
with open(my_file, "r") as watermelon:
        
    #create a csv reader object
    reader = csv.reader(watermelon, delimiter = "\t")
        
    for line in reader: 
        # skip blank lines 
        if not line: 
            continue 
        else:
            # data line where information is taken from the file and printed
            print(line[3], line[4]) 


