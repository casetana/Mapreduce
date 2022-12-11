#!/usr/bin/python
import sys

#salesTotal = 0
#oldKey = None

topSale = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if thisKey in topSale.keys():
	if float(topSale[thisKey]) < float(thisSale): topSale[thisKey] = thisSale
    if thisKey not in topSale.keys():
	topSale[thisKey] = thisSale 	



   for key ,value in topSale.items():
	print(key + "\t" + value)
