import re
var = ''
with open('file.html', 'r') as File:
    var = File.read()
var = re.sub('>', ' ', var)
links = re.findall('(https?://[^\s]+)', var)
for l in links:
    print(l)
