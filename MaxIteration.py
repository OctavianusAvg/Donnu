'''
Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Виконав : Канюка Р. 122В
'''
from memory_profiler import memory_usage
from datetime import datetime
import numpy as np
import random
while True :    
    while True:
            try:
                n = int(input("Введіть n : "))  
                if(n > 0 and n <= 5):
                    break
                else : print("Розміри масиву мають бути меншими 5 і більші за 0")
            except ValueError :
                print('Введіть число!')
    # Генерація масиву n*n
    arr = np.array([[random.randint(-10,30) for i in range(n)] for j in range(n)])
    print(arr)
    # Знаходження максимуму методои ітерацій
    max_elem = 0
    start = datetime.now()
    for i in range(n):
        for j in range(n):
            if(max_elem < arr[i][j]):
                max_elem = arr[i][j]
    print("Кількість використаних МБ :",memory_usage())
    print("Затрачений час :",datetime.now() - start)
    print("Максимальне значення =", max_elem)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
"""
Час розробки: 3 хвилини
Простіше та ефективніше використовувати метод ітерацій
для знаходження максимального
елементу багатовимірного масиву
"""
