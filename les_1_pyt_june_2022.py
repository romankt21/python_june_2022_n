# print('hi')  # рядковий коментар

"""j        #  блочний коментар, може бути '''jj'''
kkh
"""

# print('hello')

# if __name__=='__main__':
#     print('Hello')


# print('hello')
# print(1,2,3,4, sep='*')  # sep='*' розділяє позиції   #  1*2*3*4
# i = 3
# f = 1.3
# b = True # False
# s = 'text'
# n = None
#
# print(type(i))  #<class 'int'>
# print(type(f))  #<class 'float'>
# print(type(b))  #<class 'bool'>
# print(type(s))  #<class 'str'>
# print(type(n))  #<class 'NoneType'>

# a=b=c=10
#
# print((a, b, c))
#
# print(int(1.5)) # відкидає дробову частину, залишає цілу частину 1
#
# str1 = str(25)  # перетворюємо число в стрінгу
#
# print(type(str1))   # <class 'str'>

# int() # метод конвертації в ціле число
# float()   # метод конвертації в число з комою
# str() # метод конвертації в стрінгу

# i=5
#  i+=1     # додає до i 1
# i*=2
# print(i)

# a = 5
# b = 2
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)  #  переводить в int, відкидає дробову частину , результат 2,
# print(a % b) # остача 1
# print(a ** b) # в степені




# num = int(input('Enter number:'))   # за допомогою int переводимо в int
# num2 = input('Enter number2:')
#
# print(type(num))    # <class 'int'>
# print(type(num2))   # <class 'str'>

# a = 5
# b = 6
# print('a<b', a < b)  # a<b True
# print('a>b', a > b)  # a>b False
# print('a>=b', a >= b)  # a>=b False
# print('a<=b', a <= b)  # a<=b True
# print('a!=b', a != b)  # a!=b True
# print('a!=b', a is not b)  # a!=b True
# print('a==b', a == b)  # a==b False
# print('a==b', a is b)     #   a==b False. is використовується, коли потрібно порівняти з None


# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(a == b),  #True, порівнюється наповнення
# print(a is b),  # False, порівнюється посилання, комірки мають різне місце в пам'яті


#  # перевіряємо дані з типом
# print(isinstance('string', str))    # True
# print(isinstance(5, str))           # False
# print(isinstance(1.6, int))          # False
# print(isinstance(1.6, float))        # True


# # if else
# num = int(input('num:')) # input завжди повертає str
# if (5 <= num <= 7) or (num > 15 and num < 20):
#     print(True)
# elif num == 8:
#     print(8)
# else:
#     print('some')
#


# num = int(input('num:'))
#
# res = 'yes' if num > 5 else 'no'
# print(res)

# #list список (масив в js)

# l = [1, 2, 3, 4, 5, 7]
# print(l[0])     # 1
# print(l[-1])    # 7
# print(l[-2])    # 5
# a = l # списки - посилальні типи даних, посилаються на одну комірку
#
# b = l.copy() # створює повну копію
#
# l[0] = 55 # переприсвоєння
#
# print(l)
# print(a)
# print(b)
#
# print(len(l))
# del l[3] # видалиться елемент з індексом 3
#
# print(l)
# print(len(l))
#
# print(a)
# print(b)


# l = [1, 2, 3, 4, 5, 7]
# a = l
#
# print(a == l) # порівнює всі значення, результат True
# print(a is l) # порівнює адреси комірок пам'яті True
#
# b = l.copy()
# print(b is l) # порівнює адреси комірок пам'яті False
# print(b is not l) # порівнює адреси комірок пам'яті (не рівні) True

# a = [1, 2, 3, 4, 5, 6]
# print(a)    #  [1, 2, 3, 4, 5, 6]
# a.append(8)     # додає 8 в кінець
# print(a)    # [1, 2, 3, 4, 5, 6, 8]
#
# a.insert(1,555)  # додає в список з номером 1 цифру 555
# print(a)        # [1, 555, 2, 3, 4, 5, 6, 8]
# #
# pop = a.pop () #забирає останнє значення
# print(pop)      #  8
# print(a)        #  [1, 555, 2, 3, 4, 5, 6]
# #
# popq = a.pop(0)     # вилучає з індексом (0)
# print(popq)         # 1
# print(a)            #   [555, 2, 3, 4, 5, 6]

# a = [1, 2, 3, 4, 5, 6, 2]
# a.remove(2)  # видаляє 1-шу двійку, яку знайде
# print(a)  # [1, 3, 4, 5, 6, 2]

# a.extend([22, 33, 44])  # розширення списку наступним списком (додавання списків
# print(a)  # [1, 2, 3, 4, 5, 6, 2, 22, 33, 44]
#
# b = a + [333, 444, 555]  # теж розширення списку
# print(b)  # [1, 2, 3, 4, 5, 6, 2, 22, 33, 44, 333, 444, 555]
#
# a+=[99, 88] # теж розширення списку
# print(a)  # [1, 2, 3, 4, 5, 6, 2, 22, 33, 44, 99, 88]

# a = [1, 2, 3, 4, 5, 6, 2, 7, 9]
# print(a.index(4)) # знайти індекс числа 4 - 3
# print(a.index(2, 3, 7 )) # знайти індекс числа 2, починаючи з 3 числа до 7 - 6

# a.reverse()     # розвертає список
# print(a)        # [9, 7, 2, 6, 5, 4, 3, 2, 1]
# a.reverse() # розвертаємо список
# print(a) # [9, 7, 2, 6, 5, 4, 3, 2, 1]


# a.sort() # сортує масив, за замовчуванням від меншого до більшого
# print(a) # [1, 2, 2, 3, 4, 5, 6, 7, 9]

# a.sort(reverse=True)  # сортує список в зворотньому порядку, від більшого до меншого
# print(a)  # [9, 7, 6, 5, 4, 3, 2, 2, 1]

# print(a.count(2))  # рахує к-сть 2 в списку  -  2
# print(a) # [1, 2, 3, 4, 5, 6, 2, 7, 9]


# a = [1, 2, 3, 4, 5, 6, 2, 7, 9]
#
# l = a[0: 4] # повертає новий список з 0 до 4 елемента, 4 не включається, старий список не змігюється
# b = a[: 4]  # повертає новий список з 0 до 4 елемента, 4 не включається, старий список не змігюється
# print(l)  #  [1, 2, 3, 4]
# print(b) #  [1, 2, 3, 4]
#
# c = a[0: 8: 2] # повертає новий список з 0 до 8 елемента, 8 не включається, з кроком 2
# print(c)  # [1, 3, 5, 2]
#
# e = a[::-1] # зворотній список
# print(e)  # [9, 7, 2, 6, 5, 4, 3, 2, 1]
#
# f = a [::2] # список через
# print(f)  # [1, 3, 5, 2, 9]



# #tuple кортеж - це список констант, яких не можна змінювати, записуються в круглих дужках. Не можна ні додавати,
# # ні віднімати, можна підрахувати і витягнути елемент, знайти індекс елементу. Можна тільки витягнути з api

# my_tuple = (1, 2, 3, 4, 5)

# print(my_tuple) # (1, 2, 3, 4, 5)
# print(my_tuple.count(2)) # виводить к-сть 2 -  1
# print(my_tuple.index(3)) # виводить індекс числа 3  -  2

# l = list(my_tuple)  # перетворюємо кортеж в звичайний список
# print(l)  #  [1, 2, 3, 4, 5]


# #dictionary  словники (об'єкти в js)


# d = dict(name='max',age=15)
#
# print(d) # {'name': 'max', 'age': 15}
#
# c = {'name': 'max', 'age' : 15} # якщо ключ name текстового формату його теж потрібно брати в лапки, ключем
# виступає стрічка або кортеж
# print(c) # {'name': 'max', 'age': 15}

# user = {
#     'name': 'Max',
#     'age': 15,
#     'gender': 'male'
# }
# print(user)     # {'name': 'Max', 'age': 15, 'gender': 'male'}
# del user['name']   # видаляємо ключ 'name' і його значення
# print(user)     # {'age': 15, 'gender': 'male'}
# user.clear()    # очищує словник
# print(user)     # {}
# print(user.keys())  # видрукує ключі dict_keys(['name', 'age', 'gender'])
# print(user.values())    # видрукує всі значення  -  dict_values(['Max', 15, 'male'])

# print(user['name']) # в квадратних дужках вказуємо ключ, виведе його значення  -- Max
# print(user.get('name'))  # вказуємо ключ. якщо вкажемо неправильний виведе None -- Max
# print(user.get('name1', 555))  # якщо вкажемо неіснуючий ключ, можна задати новий параметр -- 555

# user['name'] = 'Ivan' # переназиваємо
# user['name'] = 'Zoriana'
# user['age'] = 38
# # user['name'] = 'Roman'
# # user['age'] = 42
# print(user)
# print(user) # {'name': 'Ivan', 'age': 15, 'gender': 'male'}

# user.copy() # створить копію, словники теж посилальний тип даних
# print(user.items()) # dict_items([('name', 'Ivan'), ('age', 15), ('gender', 'male')])
# print(list(user.keys())[0]) # конвертуємо в звичайний список і дістаємо 0 ключ -- name
# pop = user.pop('age') # за ключем можемо видалити значення
# print(pop) #  - 15
# print(user) # {'name': 'Ivan', 'gender': 'male'}
#
# pop1 = user.pop('age2', 12) # 2-гим параметром вказуємо значення, яке потрібно поставити, якщо ключ відсутній
# print(pop1) #  - 12

# popitem = user.popitem()  # видаляє з кінця
# print(popitem)  # ('gender', 'male')
# print(user)  # {'name': 'Max', 'age': 15}

# user.update({'status': True}) # оновлення списку
# user.update(status = False) # оновлення списку,  можна записати
# user |={'status': False} # ще один варіант "синтаксичний цукор"
# print(user)  #  {'name': 'Max', 'age': 15, 'gender': 'male', 'status': False}


# print(user.values()) # повертає список значень
# print(user)    # dict_values(['Max', 38, 'male'])  # {'name': 'Max', 'age': 38, 'gender': 'male'}

# setdefault_value = user.setdefault('key', 'value_my_key') # дозволяє додавати ключ якого немає і за бажанням значення.
# додає ключ, якщо такого немає, якщо ключ є він його не додає.
# print(setdefault_value) # повертає значення value_my_key
# print(user) # {'name': 'Max', 'age': 15, 'gender': 'male', 'key': 'value_my_key'}


# setdefault_value = user.setdefault('age', 'value_my_key') # якщо хочемо замінити значення в наявному ключі,
# то це значення не змігиться і залишиться попереднє значення
# print(setdefault_value) # 15
# print(user) # {'name': 'Max', 'age': 15, 'gender': 'male'}




# set - це список, який не може в собі тримати однакові значення

# l = [1, 2, 3, 4, 6, 2, 5, 4]
#
# s = set(l)    # передаємо в змінну s свій список, який тепер буде set, при цьому всі дублікати в списку видаляються
#                   # і залишаються тільки унікальні значення (без повторів)
#
# print(s)  # {1, 2, 3, 4, 5, 6}

# s = {1, 2, 3, 5, 6, 8, 1, 2, 3}  # set описується в {}
#
# print(s)  #{1, 2, 3, 5, 6, 8}

# s = set() # створюємо пустий set
# print(s) # set()
# print(type(s))      # <class 'set'>

# s = set()
#
# s.add(3)    # додаємо в set
# s.add(2)
# s.add(4)
# s.add(1)
#
# # print(s)  #  {1, 2, 3, 4} в set немає індексів, тому до них не можна достукатись
#
# pop = s.pop()   # з set дістаємо і видаляємо за допомогою методу pop дістаємо випадковий елемент
# pop1 = s.pop()
# print(pop)  # 1
# print(pop1)  # 2
# print(s)    # {3, 5, 6, 8}

# set1 = {1, 2, 3, 4, 5, 6}
# set2 = {3, 4, 5, 8, 10}

# set1.update(set2)   # приєднує сет set2 до set1
# print(set1)         #   {1, 2, 3, 4, 5, 6, 8, 10}

# set1.remove(2)      #  вилучаємо  цифру 2 з set1
# print(set1)         #  {1, 3, 4, 5, 6}

# set1.discard(2)         #  вилучаємо  цифру 2 з set1
# print(set1)             #  {1, 3, 4, 5, 6}


# print(set1.issuperset(set2))       #  чи є в set1 всі елементи які є в set2  # False  # оскільки в set1 є 3, 4, 5,
                                        #   # але немає 8 і 10
#
# set3 = {1, 2 , 3}
# print(set1.issuperset(set3))       #  чи є в set1 всі елементи які є в set3  # True  # оскільки в set1 є 1, 2, 3
#
# print(set1.isdisjoint(set2))        # перевіряє чи в set1 та в set2 немає спільних елементів, тоді True, якщо
#                                       #спільні елементи є тоді  False
#
# print(set1.intersection(set2))     # повертає спільні елементи, які є між двома set отримується новий set # {3, 4, 5}
# print(set1.difference(set2))        # # повертає відмінні елементи, які є в set1 і немає в set2
#                                       #отримується новий set # {1, 2, 6}
#
# set1.add(11)            #додасть в set1 11
# set1.add(3)             # якби в set1 не було 3, то вона б додалась
# print(set1)             # {1, 2, 3, 4, 5, 6, 11}


#       # string стрінга, стрічка, пишуться в подвійних або одинарних лапках "str" або в 'str'
# string1 = "text"
# string2 = 'text'
# string = 'name = "Vasyl"'       #   name = "Vasyl"
# string = 'name = \'Vasyl\''       #   name = 'Vasyl'  одинарні лапки в одинарних, тоді екранується за допомогою \

# print(string)

# st = "*"*50
#
# print(st)       #   **************************************************


# name = 'Max'
# age = 18
# weight = 70.5
#
# string = 'Hello, my name is Max. I am 18 and my weight 70.5 kg' # деякі параметри винесемо в змінні
#             # виведе Hello, my name is Max. I am 18 and my weight 70.5 kg
# string = 'Hello, my name is '+name+ ' I am ' + str(age) + ', and my weight ' +str(weight) + 'kg'
#                                 #int мусемо перевести в str
#          # Hello, my name is Max I am 18, and my weight 70.5kg
# string = 'Hello, my name is %s. I am %d and my weight %f kg' %(name, age, weight)   # %s -string, %d-digital, %-float
#                         # Hello, my name is Max. I am 18 and my weight 70.500000 kg
# string = 'Hello, my name is {}. I am {} and my weight {} kg'.format(name, age, weight)
#                         # Hello, my name is Max. I am 18 and my weight 70.5 kg
# string = 'Hello, my name is {name}. I am {age} and my weight {weight} kg'.format(name=name, age=age, weight=weight)
#                         # Hello, my name is Max. I am 18 and my weight 70.5 kg
# string = f'Hello, my name is {name}. I am {age} and my weight {weight} kg'
#                         # Hello, my name is Max. I am 18 and my weight 70.5 kg
#
# print(string)

# print(string.index('l'))    # виведе під яким індексом буква l  резул 2
# print(string.index('l', 3,10)) # під яким індексом буква l в діапазоні з 3 по 10 резул 3. Якщо не знайде буде помилка
# print(string.find('l', 3,10)) # під яким індексом буква l в діапазоні з 3 по 10 резул 3. Якщо не знайде видасть
                                # # не помилку, а -1
# print(string.count('l'))    # виведе к-сть l в стрічці, рез 2

# string = 'hello my name'
# string = string.capitalize()    # першу букву в речені робить великою  Hello my name
# string = string.upper()    # всі букви зробить великими  HELLO MY NAME
# string = string.lower()    # всі букви зробить малими буквами  hello my name
# string = string.islower()    # повертає true або false якщо вони маленькі
# string = string.isupper()    # повертає true або false якщо вони великі
#
#
# print(string)

# print('hello world'.title()) # перші букви робить великими  Hello World
# print('HEllo World'.swapcase()) # які були великими стають малими і навпаки heLLO wORLD
# print('HEllo'.isalpha()) # перевіряє чи це букви  True
# print('123'.isnumeric()) # перевіряє чи це цифри  True
# print('123'.isdigit()) # перевіряє чи це цифри  True
# print('123bgh'.isalnum()) # перевіряє чи це букви і цифри  True
# print('hello'.endswith('lo')) # перевіряє чи закінчується на lo  True
# print('hello'.startswith('he')) # перевіряє чи починається на he  True
#
# print('     ghfjf   '.strip())          # забирає всі зайві прогалини       ghfjf
# print('aa     ghfjf   bb'.strip('ab'))          # забирає всі зайві a і b            ghfjf
# print('aa     ghfjf   bb'.rstrip('ab'))          # забирає справа всі зайві a і b    aa     ghfjf
# print('aa     ghfjf   bb'.lstrip('ab'))          # забирає зліва всі зайві a і b       ghfjf   bb
# print('hello world'.split())          # заганяє стрічку в список  ['hello', 'world']
#
# print(list('hello world'))      # отримуємо список з букв двох слів

# print('hello is hello'.partition('is'))     # partition ділить стрічку на 3 частини: до сепаратора, сепаратор
#                                             # і після сепаратора. Рез кортеж ('hello ', 'is', ' hello')

# print('hello'[::2])     # зріз з кроком 2   рез   hlo
#
# strs = ['hello', 'world']
#
# join =' '.join(strs)
# join1 ='-'.join(strs)
#
#
# print(join)         #  отримаємо hello world
# print(join1)         #  отримаємо hello-world


# #вбудовані ф-ції
# print(min(8, 25, -45,  1, 3))       # видає мін значення, рез - - 45
# print(max(8, 25, -45,  1, 3))       # видає мін значення, рез - 25
# print(sorted([1, 3, 2, 25, -5]))     # поверне новий масив за зростанням [-5, 1, 2, 3, 25]
# print(sorted([1, 3, 2, 25, -5], reverse=True))     # поверне новий масив зі спаданням [25, 3, 2, 1, -5]
# print(pow(2, 3))   #  піднесення до степеня 2 в 3 степенеі, рез 8


#  функції
# ф-ції створюються за допомогою def називають наприк name_of_  (сней кейс)

# def func(): # аргументи можна передавати або ні, тіло ф-ції пишем на 1 tab
#     print('hello')
#
# func()      # hello
#
# def func1(a, b, c):
#     print(a, b, c)
#
# func1(1, 2, 3)      #  1 2 3
#
# def func2(*args):       # невизначена к-сть параметрів
#     print(args)
#
# func2(21, 22, 23)       # 21  22  23
#
#
# def func3(d, e, *args):
#     print(d, e, args)
#
# func3(-1, -2, 31, 32, 33)       # -1 -2 (31, 32, 33)
#
#
# def func4(f, g, *args, **kwargs):       # kwargs -іменовані параметри - зробиться словник
#     print(f, g)                     #  1 2
#     print(args)                     # (41, 42, 43)
#     print(kwargs)                   #  {'name': 'Max', 'age': 15}  словник
#
#
# func4(1, 2, 41, 42, 43, name='Max', age=15)










# 1.31.00
