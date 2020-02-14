#За s-назвою місяця визначити відповідну пору року.
from enum import Enum
while True :
    class month (Enum):
        January = 1
        February = 2
        March = 3
        April = 4
        May = 5
        June = 6
        July = 7
        August = 8
        September = 9
        October = 10
        November = 11
        December = 12
    class season (Enum):
        Winter = 1
        Spring = 2
        Summer = 3
        Autumn = 4
    while True:
        s = month[input ('month : ')]
        if s == month.December or s == month.January or s == month.February:
            print('It is ', season.Winter.name)
        elif s == month.March or s == month.April or s == month.May:
            print('It is ', season.Spring.name)
        elif  s == month.June or s == month.July or s == month.August:
            print('It is ', season.Summer.name)
        elif s == month.September or s == month.October or s == month.November:
            print('It is ', season.Autumn.name)
        else :
            print ('Incorect month ');
            continue
        break
    result = input('Бажаєте продовжити ? Y/N:')
    if(result == 'Y' or result == 'y'):
        continue
    else :
        break