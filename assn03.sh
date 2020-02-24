#! /bin/bash

#assn03-1
for i in {808..8008}
do
   echo "TR $i"
done

#assn03-2
	nano .bash_profile #copy and pasted the below aliases into .bash_profile

	alias hw='cd ~/Desktop/Programming/bio_project/homework/'
	alias razor='ssh eta003@razor.uark.edu'	
	alias python='python3'
	alias idle='idle3'

	source .bash_profile #confirms changes 

#assn03-3
	hw | cd gene_trees
	ls -al | grep -c '.fasta'
	#15085 fasta files

#assn03-4
	hw | cd gene_trees
	ls -al | grep -c '.tre
	#14640 tre files

#assn03-5
	hw | cd gene_trees
	ls -al | grep -c '.sched'
	#15262 sched files

#assn03-6
	hw | cd gene_trees
i=*.fasta
for i in *.fasta 
Do 
	if [[$I != *.tre]]; then 
	echo does not match 
	fi 
Done > test_no_match.txt
Wc -l test_no_match.txt
	#445 non matching files 


#assn03-7
	hw | gene_trees
	#30434,243628


#assn03-8
	hw | cd gene_trees
	for t in *.fasta; do test -e ${t%.fasta}_raxml.tre && echo $t>>tre.txt || echo write_raxml_job_script.py $t '>' ${t%.fasta}_alignment.pbs>>cluster.txt; done; less cluster.txt


	
