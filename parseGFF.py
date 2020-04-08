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
                start = int(line [3])
                end = int(line[4]) 
                strand = line[6]
                attributes = line[8]
                
                #extract the sequence from the lines subtracting 1 ensures you have the right start coordinate
                sequences = genome.seq[start-1:end]

                # calculating the gc content
                g_count = sequences.count("G")
                c_count = sequences.count("C")
                length = len(sequences)
                gc = (c_count + g_count)/length
                gc_round = round(gc, 2)
                
                print(attributes)
                print(gc_round)