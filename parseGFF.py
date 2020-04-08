#! /usr/bin/env python3

# importing modules
import csv
from Bio import SeqIO
import argparse

# create an argument parser object
parser = argparse.ArgumentParser(description="This script parses a GFF file and does stuff with it")

# adding the required arguments to the parser 
parser.add_argument("gff", help = "Name of the GFF file")
parser.add_argument("fasta", help = "Name of the Fasta file")

# parse the arguments
args = parser.parse_args()

# read and parse the FASTA file 
genome = SeqIO.read(args.fasta, 'fasta')

# adding args.gff will hold the info parse on the command line
with open(args.gff, "r") as gff_file: # opening the file and reading it
        
    #create a csv reader object
    reader = csv.reader(gff_file, delimiter = "\t")
        
    for line in reader: 
        # skip blank lines 
        if not line: 
            continue 
        else:
            # data line where information is taken from the file and printed
            feature = line [2]
            if feature != "CDS":
                continue # from column 2 it reads if the column contains the phrase CDS and if not then it skips it in STDOUT
            else: 
                start = line [3]
                end = line [4] 
                print(start, end)

for sequence in SeqIO.parse(args.fasta, "fasta"):
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    length = len(sequence)
    gc_content = (c_count + g_count / length)
    gc_round = round(gc_content, 2)
print(str(gc_round))
            
            # calculate and print the GC content for that substring to two decimal
