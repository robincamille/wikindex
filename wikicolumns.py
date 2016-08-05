# @robincamille
# This script takes a long list of text and splits it into columns of
# 30 items each, using Wikipedia formatting.

def makecolumns(inlist, outfile):
     #inlist is a list, outfile is a file
     outfile.write('{{col-begin}}\n{{col-break}}\n')

     for n in inlist:
          if inlist.index(n)>1 and inlist.index(n)%30 == 0: #change 30 to whatever you want if columns are too long/short
               outfile.write(n + '{{col-break}}\n')
          else:
               outfile.write(n)

     outfile.write('{{col-end}}')
     outfile.close()
