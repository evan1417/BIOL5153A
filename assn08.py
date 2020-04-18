#! usr/bin/env python3 

import re # import the regex module 
from prettytable import PrettyTable # import table module for clean output

# string of names
concert = "Katherine went to the concert to see Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine, felt left out."

# make all names uppercase to avoid tense issues
upper = concert.upper()

# for loop 
for match in re.finditer("[KC]ATH[A-Z]+", upper): # finds ATH string and reads if there is a K or C in front and any letter a-z after that
    start = match.start() # takes start position of each name
    end = match.end() # takes end position of each name 

    x = PrettyTable() # sets variable to create table 
    x.field_names = ["Full Match", "Position of First Character", "Position of Last Character", "Length of Match"] # sets column headers for the table 

    x.add_row([match.group(0), str(start), str(end), end-start]) # for each name in the find loop, it will print these things

    print(x) # prints the table 