
data =  {
    1: [111,'Abcd',100],
    2: [101, 'AAbb', 137.2],
    3: [106, 'Acbc',157.47],
    4: [111,'AAAA', 123.43],
    5: [123,'AAbb', 123.43],
    6: [121,'AAcc', 123.43],
    7: [131,'AddA', 123.43]
}


""" lst = {1: [100, "AAA", 18000],
2: [101, "BBB", 50000],
3: [102, "CCC", 21000]} """
print ("{:<8} {:<10} {:<8} {:<10}".format('SNo','Id','Name','Salary'))
for x, i in data.items():
    id, name, salary = i
    print ("{:<8} {:<10} {:<8} {:<10}".format(x, id, name, salary))
