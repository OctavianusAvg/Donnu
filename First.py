"""
а) Дан файл f, компоненти якого є цілими числами. Записати в файл g всі подвоєні
компоненти файлу f.
Виконав : Канюка Р. 122В
"""
import os
import random
while True:
    f_p = "f.txt"
    g_p = "g.txt"
    
    #Генерація випадкових чисел для файлу f
    if( not(os.path.exists(f_p))): f = open(f_p, "xt");
    else : f = open(f_p, "wt");
    begin = ''
    for b in range(10):
       begin += str(random.randint(0,30))
       
    print("Вихідні данні :", begin)
    f.write(begin)
    f.close()
    
    # Запис в файл g подвоєних значень з файлу f
    f = open(f_p, "rt")
    if( not(os.path.exists(g_p))): g = open(g_p, "xt");
    else : g = open(g_p, "wt");
    res = ''
    for i in f.read(-1):
        res += str(int(i) * 2)
        
    print("Кінцеві данні :",res)
    g.write(res)
    f.close()
    g.close()
    
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break

