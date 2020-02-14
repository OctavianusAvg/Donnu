#За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
#наявність високосних років.
while True :
    days = range (1, 32)
    mounths = range (1, 13)
    years = range (1901, 2020)
    while True :
        try :
            d, m, y = int (input ( 'day:')), \
            int (input ( 'mounth:')), \
            int (input ( 'year:'))
            break
        except ValueError:
            print('Введіть число')
    d2 = d
    m2 = m
    y2 = y
    if(d >= 28 and m == 2 and y % 4 != 0):
        m += 1
        d = 1
    elif(d >= 29 and m == 2 and y % 4 == 0):
        m += 1
        d = 1
    elif(d >= 31):
        if(m == 1 or m == 3 or m == 5 or m == 7 or m == 8  or m == 10 or m == 12):
              m += 1
              d = 1
              if(m - 1 == 12):
                  y += 1
                  m = 1
    elif(d >= 30 ):
        if(m == 4 or m == 6 or m == 9 or m == 11):
            m += 1
            d = 1
    else :
        d += 1
    print('NextDay :',d,'Month :',m ,'Year :', y)
    if (d2 == 1):
        m2 -= 1;
        if(m2 == 2 and y2 % 4 != 0):
            d2 = 28
        elif(m2 == 2 and y2 % 4 == 0):
            d2 = 29
        elif (m2 == 4 or m2 == 6 or m2 == 9 or m2 == 11):
            d2 = 30
        else :
            if(m2 == 1):
                m = 1
                y -= 1
            d2 = 31
    else:
        d2 -= 1;
    print('PreviousDay :', d2, 'Month :', m2, 'Year :', y2)
    answ = input( 'Бажаєте продовжити ? Y/N: ')
    if( answ == 'Y' or answ == 'y' ):
        continue
    else :
        break

