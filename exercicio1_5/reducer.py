#!/usr/bin/python
import sys

salesTotal = {}


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey , thisSale = data_mapped

          
    if thisKey in salesTotal.keys():
        salesTotal[thisKey] += float(thisSale)

    # Si no  está lo añade al diccionario

    if thisKey not in salesTotal.keys():
        salesTotal[thisKey] = float(thisSale) 	



   for key ,value in salesTotal.items():
    print(key + "\t" + str(value))



    
