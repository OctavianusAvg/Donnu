"""Варіант 5: б) Дано текстові файли f1 і f2. Переписати зі збереженням порядку проходження
кожен другий компонент файлу f1 в f2, а кожен другий компонент файлу f2 - в файл f1.
Використовувати допоміжний файл h.
Виконав : Канюка Р. 122В
"""
import string
import random
def rewrite(readPath,writePath):
    """Функція для передачі кожного другого компоненту з вмісту файлу.
    readPath - шлях до файлу для зчитування.
    writePath - шлях до файл для запису.
    повертає кінцевиу строку.
    """
    read = open(readPath,"rt")
    write = open(writePath,"wt")
    strg = read.read(-1)
    result = ''
    for i in range(1,len(strg),2):
        result += strg[i]
    write.write(result)
    read.close()
    write.close()
    return result
def randGnrText(writePath):
    """Рандомно генерує текст та записує в файл
        writePath - шлях до файлу для запису.
        повертає згенероване значення
    """
    write = open(writePath,"wt")
    digits = "".join( [random.choice(string.digits) for i in range(random.randint(0,10))] )
    chars = "".join( [random.choice(string.ascii_letters) for i in range(random.randint(0,25))] )
    result = chars + digits 
    write.write(result)
    return result
while True:
    #Файли f1.txt f2.txt - випадково згенеровані строки.
    #h - Проміжний файл.
    f1 = "f1.txt"
    f2 = "f2.txt"
    h = "h.txt"
    print("Початкові данні в файлі f1:",randGnrText(f1))
    print("Початкові данні в файлі f2:",randGnrText(f2))
    # f1 --> h
    rewrite(f1, h)
    
    # f2 --> f1
    print("Кінцеві данні для файлу f1:",rewrite(f2, f1))
    
    # h --> f2
    h = open("h.txt","rt")
    f2 = open("f2.txt","wt")
    text = h.read(-1)
    print("Кінцеві данні для файлу f2:",text)
    f2.write(text)
    h.close()
    f2.close()
    
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
