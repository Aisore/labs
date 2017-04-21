#!/bin/python3
def mathem_one(filename):
    infile = open(filename, 'r').read().split()
    ages = [int(i) for i in infile]
    return str(round(sum(ages)/len(ages)))
def find_slice(fname, times):
    ages = [int(i) for i in fname[:times]]
    return str(round(sum(ages)/len(ages)))