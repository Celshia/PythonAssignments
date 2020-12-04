n = int(input('Enter a number: '))
for Number in range (n, n+100):
    count = 0
    for i in range(2, Number):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')


         
