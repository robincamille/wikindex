outText=open('index-wikified.txt','r') #or whichever file you're listifying
out=outText.readlines()
outTextCol=open('index-listified.txt','w')
outTextCol.write('{{col-begin}}\n{{col-break}}\n')

for n in out:
     if out.index(n)>1 and out.index(n)%30 == 0: #change 30 to whatever you want if columns are too long/short
          outTextCol.write(n + '{{col-break}}\n')
     else:
          outTextCol.write(n)

outTextCol.write('{{col-end}}')

outText.close()
outTextCol.close()
print 'Listified!'
