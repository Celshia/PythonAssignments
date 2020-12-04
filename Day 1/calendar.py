
print('sun mon tue wed thu fri sat')
x = 3
count = x-1
print(' ' * ((x-1) * 4), end='')

for var in range(1,32):
    print(f'{var:<3}', end = ' ')
    count+=1
    if(count==7):
        count=0
        print()

def day_of_week(year, month, day):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7
year=int(input("enter a year : "))
month=int(input("enter a month : "))
day=int(input("enter a day : "))
print(day_of_week(year, month, day))
