'''
Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.
Виконав : Канюка Р. 122В
'''
from memory_profiler import memory_usage
from datetime import datetime
import numpy as np
import random
def numSqrt(n):
    
    def inner(n, i = 0):
        if((len(n) - 1) ==  i):
            return int(n[len(n)- 1])
        return int(n[i]) + inner(n,i+1)
    
    while (len(n) > 1):
        n = str(inner(n))
    return int(n);
    
while True:
    #Ініціалізація n і знаходження довжини
    while True:
        try:
            n = input("Введіть число для знаходження цифрового кореня : ")
            beg = int(n)
            break
        except ValueError :
            print('Введіть число!')
    #Реалізація алгоритму
    start = datetime.now()
    summ = numSqrt(n)
    print("Кількість використаних МБ :",memory_usage())
    print("Затрачений час :",datetime.now() - start)
    print("цифровий корінь ", beg , "=", summ)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
"""
Час розробки :  10 - 15 хв
Реалізовувати данне завдання ,методом рекурсій складніше ,
і читабельність коду в данній реалізації не краща.
Проте по часу алгоритми мають майже однакові результати.
"""
