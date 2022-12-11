#!/usr/bin/python
import sys

saleItems = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    # Si está suma los valores

    if thisKey in saleItems.keys():
	saleItems[thisKey] += float(thisSale)

    # Si no  está lo añade al diccionario

    if thisKey not in saleItems.keys():
	saleItems[thisKey] = float(thisSale) 	



   for key ,value in saleItems.items():
	print(key + "\t" + str(value))

