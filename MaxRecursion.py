'''
Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Виконав : Канюка Р. 122В
'''
from memory_profiler import memory_usage
from datetime import datetime
import numpy as np
import random

def maximum(arr, n, i = 0 ,j = 0):
    """ Функція знаходит максимум і викликає функцію inner()
        для кожного рядку arr і повертає максимальне значення в масиві.

        arr - двувимірний масив розмірами n*n
        n - розмірність масиву
        i - початкове значення індексу по рядкам
        j - початкове значення індексу по стовпцям
    """
    def inner(arr, n, i, j):
        """ Функція знаходить максимальний елемент в кожному рядку і повертає його.

            arr - двувимірний масив розмірами n*n
            n - розмірність масиву
            i - індекс по рядкам в масиві
            j - початкове значення індексу по стовпцям
        """
        if (j == n - 1):
            return arr[i][n-1]
        while(j < n):
            nxt = inner(arr, n, i, j+1);
            if(arr[i][j] > nxt):
                return arr[i][j]
            else:
                return nxt
        
    
    max_arr = np.zeros([1,n])
    while(i < n):
        max_arr[0][i] = inner(arr, n, i, j)
        i += 1
    return inner(max_arr , n , 0, 0)

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
    start = datetime.now()
    max_elem = maximum(arr , n)
    print("Кількість використаних МБ :",memory_usage())
    print("Затрачений час :",datetime.now() - start)
    print("Максимальне значення =", max_elem)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
"""
Час розробки : 20 - 30 хв
Алгоритм знаходження максимуму реалізований через ітерації є простішим і ефективнішим,
але рекурсивний метод знаходження максимуму, надає унікальний досвід і підтверджує,
що ітераційний метод можна реалізувати рекурсивно.
"""
