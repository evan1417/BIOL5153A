#! /usr/bin/env python3

# storing each line as a list variable
watermelon = []

# opening the file and reading it
with open("/users/evan/desktop/watermelon_files/watermelon.gff", 'rt') as myfile:
    # reading the file
    for line in myfile:
        gene = line.split()[10]  # get gene name from split line

        if not gene == "similar":  # ignore similar
            watermelon.append(gene)

watermelon.sort()  # sort list
print(watermelon)
