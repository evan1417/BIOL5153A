#! /bin/bash 

#assn01-1
	find /Users/Evan/ -iname "nad*" 

#assn01-2
	top -F -R -o cpu 
	#3.2%
	#PhysMem: 7789M used (1747M wired), 402M unused.
	#Above numbers copy and pasted from the memory line

#assn01-3 
	cd ~/Desktop/Programming/watermelon_files | grep misc_feature watermelon.gff > text.txt | sort -k7nr text.txt > IR_Regions.gff | less -S IR_Regions.gff
	#Outputs to a text file then returns what the text file has to confirm it is sorted correctly

#assn01-4 
	cd ~/Desktop/Programming/watermelon_files | sort -k3 watermelon.gff | egrep -ci 'repeat_region|IR' watermelon.gff 
	#Output=6 inverted repeat regions 
	cd ~/Desktop/programming/watermelon_files | grep -ci 'chloroplast' watermelon.gff 
	#Output=28 total chloroplast sequences 
	#More sequences come from outside the IR sequences of the chloroplast - difference of 22 sequences 

#assn01-5 
	cd ~/Desktop/Programming/watermelon_files_1;column -t genes.fsa;grep -r 'GGATCC' genes.fsa;grep -v 'GAATTC' genes.fsa
	

#assn01-6
	cd ~/Desktop/Programming/example_files | sed -n '500,1000 p' shaver_etal.csv > shaver_500.txt
	#wc -l gives the line numbers, was used to confirm the 500th and 1000th lines were the correct ones that were printed
	#sed -n with p at the end of the range will print the selected lines. Then the print is routed to a separate plain text file

#assn01-7
	cd ~/Desktop/Programming/example_files | sort -k2,2r -k3,3 fruit.txt
	