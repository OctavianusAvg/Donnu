'''
Дан текстовий файл f. Отримати в файлі g кількість букв, що знаходяться в файлі
f.
Виконав : Канюка Р. 122В
'''
import random
import string
def randGnrText(writePath):
    """Рандомно генерує текст та записує в файл
        writePath - шлях до файлу для запису.
        повертає сгенеровану строку.
    """
    write = open(writePath,"wt")
    digits = "".join( [random.choice(string.digits) for i in range(random.randint(0,10))] )
    chars = "".join( [random.choice(string.ascii_letters) for i in range(random.randint(0,25))] )
    result = digits + chars
    write.write(result)
    return result
while True:
    g = random.randint(0,30)
    print("g =", g)
    #Псевдовипадково згенерований текст в файлі
    f_path = "f.txt"
    print("Данні в файлі f :",randGnrText(f_path))
    f = open(f_path, "rt")
    text = f.read(g)
    f.close()
    print("Кінцевий текст : ",text)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
