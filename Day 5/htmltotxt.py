import urllib.request
import re

link=urllib.request.urlopen('http://ramakrishnavivekananda.info/')
f=link.read()
D = f.decode('utf-8')
x=re.sub('<.*?>','',D)
with open('G:/python ex/file.txt','w',encoding='utf-8') as fwrite:
    fwrite.write(x)
