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
     elif re.search(r"(See|see)",line): #remove lines that include 'See ___'
          pass                   
     elif re.match(r"^\*\[\[[A-Z]",line): #only names beginning with capital letters
          outText.write(line)
          #print line
     else:
          pass

outText.close()

#from here to bottom: breaks list into columms of 30 items and outputs second file, index-wikified-listified.txt

outText=open('index-wikified.txt','r')
out=outText.readlines()
outTextCol=open('index-wikified-listified.txt','w')
outTextCol.write('{{col-begin}}\n{{col-break}}\n')

for n in out:
     if out.index(n)>1 and out.index(n)%30 == 0: #change 30 to whatever you want if columns are too long/short
          outTextCol.write(n + '{{col-break}}\n')
     else:
          outTextCol.write(n)

outTextCol.write('{{col-end}}')

outText.close()
outTextCol.close()
print 'Done!'
