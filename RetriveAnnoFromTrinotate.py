#!/usr/bin/env python
import pandas as pd
import numpy as np
import csv

df = pd.read_excel("trinotate_test.xlsx")
# df.head()
term2gene = []
term2trans = []
term2name = []
kegg2gene = []
kegg2trans = []
for index, row in df.iterrows():
    geneID, transcriptID, blastGO, pfamGO, KEGGID = row["#gene_id"], row["transcript_id"], row["gene_ontology_blast"], row["gene_ontology_pfam"], row["Kegg"]
    #get the GO ID and corresponding gene
    if blastGO != ".":
        for GOcol in blastGO.split("`"):
            GOterm, GOname = GOcol.split("^")[0], GOcol.split("^")[2]
            term2gene.append([GOterm, geneID])
            term2trans.append([GOterm, transcriptID])
            term2name.append([GOterm, GOname])
    elif pfamGO !=".":
        for GOcol in pfamGO.split("`"):
            GOterm, GOname = GOcol.split("^")[0], GOcol.split("^")[2]
            term2gene.append([GOterm, geneID])
            term2trans.append([GOterm, transcriptID])
            term2name.append([GOterm, GOname])
    else:
        continue
    # get the KEGG ID and corresponding gene
    if KEGGID != ".":
        for KEGGcol in KEGGID.split("`"):
            if "KO:" in KEGGcol:
                KEGGID = KEGGcol.split("KO:")[-1]
                kegg2gene.append([KEGGID, geneID])
                kegg2trans.append([KEGGID, transcriptID])
# remove redundant gene-GO rows
term2gene = set(map(tuple,term2gene))
kegg2gene = set(map(tuple,kegg2gene))

with open("term2gene.csv", "w") as file:
    writer = csv.writer(file)
    for list in term2gene:
        writer.writerow(list)
with open("term2transcript.csv", "w") as file:
    writer = csv.writer(file)
    for list in term2trans:
        writer.writerow(list)
with open("term2name.csv", "w") as file:
    writer = csv.writer(file)
    for list in term2name:
        writer.writerow(list)
with open("kegg2gene.csv", "w") as file:
    writer = csv.writer(file)
    for list in kegg2gene:
        writer.writerow(list)
with open("kegg2trans.csv", "w") as file:
    writer = csv.writer(file)
    for list in kegg2trans:
        writer.writerow(list)