#Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
#цієї ж суми в гривнях.
from enum import Enum

class converter (Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4
while (True) :
    while (True) :
        try :
            x = float (input ( 'amount of money: '))
            break
        except ValueError:
            print('Неправильне значення кількості')
    while (True) :
        try :
            p = converter [input ( 'currency: ')]
            break
        except KeyError:
            print('Валюта не задана чи задана не правильно')

    if p == converter.USD:
        print('В гривнях', x * 24.42)
    elif p == converter.EUR:
        print('В гривнях', x * 26.66)
    elif p == converter.CZK:
        print('В гривнях', x * 1.07)
    elif p == converter.PLN:
        print('В гривнях', x * 6.26)
    answ = input( 'Бажаєте продовжити ? Y/N: ')
    if( answ == 'Y' or answ == 'y' ):
        continue
    else :
        break