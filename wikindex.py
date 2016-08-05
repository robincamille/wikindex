# -*- coding: utf-8 -*-

# @robincamille
# This script takes a plain-text index of names in a typical format and
# outputs a list of names in Wikipedia format. For instance, the line
# "Smith, Jane, 76" in a typically-formatted index will become
# [[Jane Smith]] in the outputted file.

# Input: Plain-text file, index copied/pasted from an old book
# Output: Plaint-text file, names in Wikipedia format, split into columns
# of 30 names each (you'll have to fiddle with this if your list is huge)

# From command line:
# python wikindex.py [inputfilename] [outputfilename]


import re, sys
from wikicolumns import *

indexorigfile = sys.argv[1] #input file
outTextFile = sys.argv[2] #output file

##indexorigfile = 'sample_index-raw.txt'
##outTextFile = 'sample_index-wik-col.txt'

outText = open(outTextFile,'w')

#with open(indexorigfile) as indexorig:
indexorigf = open(indexorigfile, 'r')
indexorig = indexorigf.read()

# Clean out unnecessary elements
indexorig = re.sub(r'(\d{0,2})','',indexorig)
     #take out page numbers (does not take out Roman numerals)
indexorig = re.sub(r'"','',indexorig)
     #take out double quotation marks
indexorig = re.sub(r',,',',',indexorig)
     #take out double commas
indexorig = re.sub(r'((,|\s|\.)+\n)','\n',indexorig)
     #take out endline commas, spaces, and periods

lines = re.split("\n+", indexorig)
nameslist = []
# Formatting
for line in lines:
     line = re.split(", ",line)
     line.reverse() #switch names from (last, first) to (first, last)

     line = str(line)
     line = re.sub(r"(\[(\'|\")\s*)","*[[",line)
          #output name in wiki format *[[name]]
     line = re.sub(r"((\'|\")\]\s*)","]]\n",line)
     line = re.sub(r"(\',\s\')"," ",line) 

     if re.match(r"^\*\[\[(([A-Z](\.|\s|\]))|Dr\.|Mrs(\.*)\s|Rev\.|Miss\s|Prof\.|Mr(\.*)\s|Messrs(\.*))",line):
               #ignore names beginning with initials, like J. Adams, or titles
          pass
     elif re.search(r"(See|see|Index|INDEX|\(|\)|\~)",line):
          #remove lines that include 'see' or 'index' or parens or tilde
          pass                   
     elif re.match(r"^\*\[\[[A-Z]",line):
          #only names beginning with capital letters
          nameslist.append(line)
          #print line
     else:
          pass

makecolumns(nameslist, outText)

indexorigf.close()
outText.close()

#print 'Wikified!'
