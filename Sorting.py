import numpy as np
import random
from datetime import datetime
import time
def userInput():
    """ Введення данних з клаіваутури користувачем

    Дозволенно вводити від 1 до 30 елементів.
    """
    while True:
        try:
            n = int(input('Введіть кількість елементів : '))
            if(n <= 0 or n > 30):
                print('Число має бути невідємним і не більшим за 30')
                continue
            break
        except ValueError :
            print('Введіть ціле число!')
    while True:
        z = np.zeros(n)
        try:
            for i in range(1,n+1):
                z[i-1] = input(f'Елемент {i}: ')
            break
        except ValueError :
            print('Введіть ціле число!')
    return z
    
    
def generateRand():
    """Генерація пвесдовипадкових чисел

    Генерує 100 тисяч елементів.Обрежено сортування
    данної послідовності може зайняти тривалий час. 
    """
    n = 100000
    arr = np.empty(n);
    for i in range(n):
        arr[i] = random.randint(0,n)
    return arr

def bubbleSearch(arr,order = True):
    """Метод бульбашкового сортування 

    Найпростіщий алгоритм сортування ,який порівнює
    дві сусідні пари між собою і міняє їх місяцми.
    """
    start_now = datetime.now()
    A = arr.copy()
    n = len(A)
    similes = 0
    swaps = 0
    for i in range(1,n):
        for j in range(n - 1 , i - 1 , -1):
            if(A[j - 1] > A[j] and order):
                A[j],A[j-1]= A[j-1],A[j]
                swaps += 1
            elif(A[j - 1] < A[j] and not order):
                A[j],A[j-1]= A[j-1],A[j]
                swaps += 1
            similes += 1
    print('(BubbleSearch)Кількість порівнянь:',similes)
    print('(BubbleSearch)Кількість обмінів:',swaps)
    print('(BubbleSearch)Кількість обмінів:', (datetime.now() - start_now))
    return A

def selectionSearch(arr,order = True):
    """Метод Сортування вибором

    Простий  алгоритм сортування ,який на кожному i-му прозоді
    по масиву здійснює пошук мінімального(максимального) елемента
    за один прохід.
    """
    start_now = datetime.now()
    A = arr.copy()
    n = len(A)
    similes = 0
    swaps = 0
    for i in range(n - 1):
        min = i
        for j in range(i + 1 , n):
            if A[j] < A[min] and order:
                min = j
            elif A[j] > A[min] and not order:
                min = j
            similes += 1
        A[i], A[min] = A[min], A[i]
        swaps += 1
    print('(SelectionSearch)Кількість порівнянь:',similes)
    print('(SelectionSearch)Кількість обмінів:',swaps)
    print('(SelectionSearch)Затрачений час:', (datetime.now() - start_now))
    return A

def insertionSearch(arr,order = True):
    """Сортування вставками

    Простий в реалізації алгоритм сортування ,який полягає в тому ,
    що окремо аналізуються кожен окремий еллемент
    і переміщується в відсортовану частину.    
    """
    start_now = datetime.now()
    A = arr.copy()
    n = len(A)
    similes = 0
    swaps = 0
    for i in range(1,n):
        j = i - 1
        key = A[i]
        similes += 1
        while j >= 0 and A[j] > key and order:
            swaps += 1
            A[j + 1] = A[j]
            j -= 1
        while j >= 0 and A[j] < key and not order:
            swaps += 1
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    print('(InsertionSearch)Кількість порівнянь:',similes)
    print('(InsertionSearch)Кількість обмінів:',swaps + similes)
    print('(InsertionSearch)Затрачений час:', (datetime.now() - start_now))
    return A
#Задання чи генерація послідовності
while True:
    quest = input('Ви хочете задати послідовність? Y/N: ')
    if(quest == 'Y' or quest == 'y'):
        g = userInput()
        print('Початкова послідовність :', g)
        print('\nПрості методи сортування виконуються за зростанням: \n -------------------------------')
        result = bubbleSearch(g,True)
        selectionSearch(g,order = True)
        insertionSearch(g)
        print('Відсортована послідовність :',result)
        
        print('\nПрості методи сортування виконуються за спаданням: \n -------------------------------')
        result = bubbleSearch(g,False)
        selectionSearch(g,order = False)
        insertionSearch(g,False)
        print('Відсортована послідовність :',result)
        
        
    else :
        quest = input('Згенерувати послідовність? Y/N: ')
        if(quest == 'Y' or quest == 'y'):
            g = generateRand()
            input('Сортування 100000 елементів може ,зайняти більше години часу. Підтвердіть процес.')
            print('Початок сортування вставками...')
            insertionSearch(g)
            print('Кінець сортування')
            
        else :
            print('Ну... ладно.')
            break
    quest = input('Завершити виконання програми? Y/N: ')
    if(quest == 'Y' or quest == 'y'):
        break
            
            



