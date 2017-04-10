#!/bin/python3

def mathem_one(filename, fnum):
    infile = open(filename, 'r').read().split()
    infnum = len(open(filename, 'r').readlines())
    if (fnum <= infnum):
        ages = [int(i) for i in open(filename, 'r').readlines(fnum)]
    else:    
        ages = [int(i) for i in infile]
    return str(round(sum(ages)/len(ages)))