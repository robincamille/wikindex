# -*- coding: utf-8 -*-

import re

outText=open('index-wikified.txt','w')

filename=open('xxxxx.txt','r') #copy and paste the index into a file, replace xxxxx with filename
fcontent=filename.read()
filename.close()

fcontent1 = re.sub(r'(\d{0,2})','',fcontent) #take out page numbers (does not take out Roman numerals)
fcontent2 = re.sub('("|\s\(.*?\))','',fcontent1) #take out double quotation marks and anything in parens
fcontent3 = re.sub(',,',',',fcontent2) #take out double commas
fcontent4 = re.sub(r'((,|\s|\.)+\n)','\n',fcontent3) #take out endline commas, spaces, and periods

lines = re.split("\n+", fcontent4)

for line in lines:
     line = re.split(", ",line)
     line.reverse() #switch names from (last, first) to (first, last)

     line = str(line)
     line = re.sub(r"(\[(\'|\")\s*)","*[[",line) #output name in wiki format *[[name]]
     line = re.sub(r"((\'|\")\]\s*)","]]\n",line)
     line = re.sub(r"(\',\s\')"," ",line) 
     #print line

     if re.match(r"^\*\[\[(([A-Z](\.|\s|\]))|Dr\.|Mrs(\.*)\s|Rev\.|Miss\s|Prof\.|Mr(\.*)\s|Messrs(\.*))",line): #ignore names beginning with initials, like J. Adams, or titles
          pass
     elif re.search(r"(See|see|Index|INDEX)",line): #remove lines that include 'see' or 'index'
          pass                   
     elif re.match(r"^\*\[\[[A-Z]",line): #only names beginning with capital letters
          outText.write(line)
          #print line
     else:
          pass

outText.close()

print 'Wikified!'
