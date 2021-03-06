def help():
    print("Use:\npython SumOrthorfinder.py Orthogroups.txt\n"
          "#Find the orthologs for transcripts from orthogroup result in Orthofinder")

import csv
import sys
try:
    file = sys.argv[1]
except IndexError:
    help()
    exit()
# file = 'orthotest.txt'
print('Reading %s' % file)
res = {}
#define a list containing other species' abbriviation (ortholog species)
otho_spc = ['lja|', 'gma|', 'mtr|', 'pvu|']
for lines in open(file):          #each line is an orthogroup
# for lines in open('orthotest.txt'):
    if 'ahy|' in lines and any([i in lines for i in otho_spc]):       #if orthogroup has target transcript(start with 'seq|') and other species protein
        cols = lines.strip().replace('OG\d*\: ', '').split(' ')
        ortho = ""
        for prot in cols:     #collect the orthologs from other species
            if any(i in prot for i in otho_spc):
                ortho += ";" + prot
        for prot in cols:     #append collected orthologs to targeted transcripts
            if 'ahy|' in prot:  #find targeted transcripts
                if prot not in res.keys():
                    res[prot] = ortho
                else:
                    print('redundant ahy ID: %sin one orthogroup' % prot)
                    # res[prot] += ";" + ortho

with open("ortho_result.csv", "w") as file:
    writer = csv.writer(file)
    for key, value in res.items():
        ln = [key,value]
        writer.writerow(ln)