
data =  [
    [111,'Abcd',100,'f'],
    [101, 'AAbb', 137.2,'f'],
    [106, 'Acbc',157.47,'f'],
    [111,'AAAA', 123.43,'f'],
    [123,'AAbb', 123.43,'m'],
    [121,'AAcc', 123.43,'m'],
    [131,'AddA', 123.43,'m']
]


#prefixing and increment
l=len(data)

for i in range(l):
    if(data[i][3] == 'm'):
        data[i][1] = 'Mr.' + data[i][1]
    elif(data[i][3] == 'f'):
        data[i][1] = 'Ms.' + data[i][1]
    data[i][2] = data[i][2] + (data[i][2] * 0.1)

print(data)
