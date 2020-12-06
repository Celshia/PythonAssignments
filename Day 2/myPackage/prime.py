def Prime():
    lower = int(input("Enter start range: "))
    upper = int(input("Enter end range: "))
    num = [] 
    for num in range(lower,upper + 1):
  
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=' ')
Prime()      
