#! /bin/bash/python

#Opens the file and calculates the length of the sequence. I used a random .fasta file and converted it to .txt
dna = open("/Users/evan/Desktop/dna.txt")
dna_contents = dna.read()
length = len(dna_contents)

#Counts the individual nucleotide values
a_count = dna_contents.count('A')
t_count = dna_contents.count('T')
g_count = dna_contents.count('G')
c_count = dna_contents.count('C')

#Calculates the percent of each nucleotide
a_content = a_count/length 
t_content = t_count/length
g_content = g_count/length 
c_content = c_count/length 

#Rounding the decimal values - this can most likely be done alongside the percent section
a_round = round(a_content, 2)
t_round = round(t_content, 2)
g_round = round(g_content, 2)
c_round = round(c_content, 2)

print('Here are the nucleotide values: ' + '\n' + 'A content = ' + str(a_round) + 
      '\n' + 'T content = ' + str(t_round) + 
      '\n' + 'G content = ' + str(g_round) + 
      '\n' + 'C content = ' + str(c_round))