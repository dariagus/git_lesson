#Однострочный комментарий

"""
Многострочный комментарий

"""

"""
1. Как объявить переменную?
Переменная - поименованная область в оперативной памяти

Ограничения на переменную накладываются также как и на др идентификаторы
1) Нельзя начинать название переменной с цифры
2) Использовать латиницу, "_" и цифры можно, кирилицу и и пробелы нельзя

Python интерпретируемый язык, регистр зависимый, 2 версии языка
"""

a = 1  # PEP - 8 read about that (Google) rools about decorations 
print (a)

"""
2. Какие типы данных существуют в Python?

Является характеристикой и отражает:
1) Кол-во оперативной памяти
2) Диапазон допустимых значений
3) Допустимые операции
4) Формат отображения /представления 
"""
"""
Типы данных:
1) Скалярные (простые) типы, могут содержать только одно значение
   - int        -целые числа 
   - float      -дробные / числа с плавающей точкой
   - complex    -комплексные числа
   - bool       -логические плаги
   - str        -строки
   - bytes      - байтовые строки 
"""

i1 = 10
i2 = 0b100 # Двоичная Система Счисления
i3 = 0o777 # Восьмиричная СС
i4 = 0x2F  # Шестнадцатиричная СС

f1 = 1.23
f2 = 1e6     # 6 - степень 10 = миллион (е = 10)
f3 = 123e-3  # 10 в -3 степени 

c1 = 3.13j

b1 = True
b2 = False

s1 = 'Hel"lo'
s2 = "Pyt'hon"
s3 = '\tHel"\'\\lol\n'
"""
\t - табуляция
\n - перенос строки
экранирование символ обратного слэша - "\"
\- для недействительности кавычек (чтобы видно было в тексте)
"""
s4 = '''
         f,asl
                 fwrg
'''            # Можно использовать также двойный кавычки - "

s5 = """ Hello ' " world!!! """
s6 = u' '      # для Python 2 - юникодная строчка
s7 = '^\d+$\n' # регулярное выражение
s7s = r'^\d+$' # raw string

bs1 = b'Hello'

# строчки должны быть либо байтовые, либо юникодные для объединения

"""
2) Структурные типы (сложные, составные переменные)
    - tuple   - кортежи   (их нельзя менять)
    - list    - списки    (можно менять)
    - set     - множества (все значения в множестве уникальны)
    - dict    - словари
    - object  - объекты
"""
t = (1, 1.2, True, 'str', (1, 2, 3)) # Создается в круглых скобках
print (t[2]) # Индексация находится в квадратных скобках, начинается с нуля

l = [1, 1.222, (45, 45), 'kl', []]  # Создается в крадватных скобках

s = {1, 2, 2, 3, 3} # Создается в фигурных скобкаx, остается только одно значение {1, 2, 3}; True = 1, False = 0; только цифры
s2 = set() # Пустое множество, для создание используем конструкцию set

print (s)

d = {
        'key_1':1,
        'key_2':{1, 2, 3},
        
    } # Создается в фигурных скобкаx

print (d['key_1'])

"""
3) Специальные: None
   - пустая строчка, нет значения
   - всегда пишется с большой буквы
Динамическая типизация у Python
"""
abc = None # потом можно найти значение
g = 7
abc = g*12
print (abc)


"""
Преподаватель: Кирилл
Номер телефона: +7 (911) 279-02-46
ДЗ: 1) зарегестрироваться на github.com
    2) прочитать про PEP (8 read about that (Google) rools about decorations)
"""
