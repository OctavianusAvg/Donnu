'''
б) Дан текстовий файл f. Записати в файл g компоненти файлу f в зворотному
порядку, без повторюваних компонентів.
Виконав : Канюка Р. 122В
'''
import os
import string
import random
def randGnrText(writePath):
    """Рандомно генерує текст та записує в файл
        writePath - шлях до файлу для запису.
        повертає згенероване значення
    """
    if( not(os.path.exists(writePath))):
        write = open(writePath, "xt")
    else :
        write = open(writePath, "wt")
    digits = "".join( [random.choice(string.digits) for i in range(random.randint(0,10))] )
    chars = "".join( [random.choice(string.ascii_letters) for i in range(random.randint(0,25))] )
    result = chars + digits 
    write.write(result)
    write.close()
    return result

while True:
    #Генерація випадкового тексту для файлу f
    f_p = "f2.txt"
    g_p = "g2.txt"
    print("Початкові данні в файлі f:",randGnrText(f_p))
    elem = set()
    res = ''
    #Зчитування тексту
    for i in open(f_p,"rt").read(-1):
        if(i not in elem):
            res += i
            elem.add(i)
    res = res[::-1]
    print("Кінцеві данні, що запишуться в файл g:",res)
    if( not(os.path.exists(g_p))): g = open(g_p, "xt");
    else : g = open(g_p, "wt");
    g.write(res)
    
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
