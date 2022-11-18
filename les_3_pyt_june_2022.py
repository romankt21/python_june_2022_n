#   #  класи
#   #   в python є поля класу і поля екземпляру класу
#   #   конструктор представлений у вигляді звичайної ф-ції, яка починається і закінчується
#   # двома нижніми підкресленнями __ посередині init
#   # від слова initialization - ініціалізація

# class User:
#     count = 8      # поле класу
#
#     def __init__(self, name, age):  # __init__ - конструктор, self це те саме що в js this -
#                                       # посилання на екземпляр класу (на самого на себе),
#                                       # можна вводити додаткові поля в дужки (self, name, age)
#         self.name = name        # створюємо property власність, все що не прописано через слово
#                                   # self це не відноситься до полів самого класу
#         self.age = age


# print(User.count)  # щоб звернутись до полів самого класу пишемо User ставимо крапку і бачимо count

# user = User('Max', 15)      #  створюємо екземпляр класу user: пишемо User (наш клас), а в дужках прописуємо поля,
#                               # які потраплять в init, але без self і створюємо змінну user
# print(user.age)            #  звертаючись до змінної user можна звернутись до своїх полів: name та age.
#                               # До полів класу - count можна звернутись через клас User
# print(user.name)

# user1 = User('Max', 15)         # результат 8
# user2 = User('Max', 15)         # результат 8
#
# print(user1.count)      # зробимо некоректно звертаємось до поля екземпляр класу user1 до
# print(user2.count)
#
# User.count = 10     #   звертаємось до класу User і count, перепризначимо на 10
#
# print(user1.count)      # результат 10
# print(user2.count)      # результат 10, змінна count одна на всі екземпляри класу


# class User:
#     count = 8
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):      # дандер методи або magic методи, ці методи відповідають за те як екземпляр класу
#                               # має себе поводити, має передати стрічку
#         return f'{self.name}-{self.age}'    # будмето повертати name та age
#
#     def __repr__(self):     # метод str використовують в парі з методом repr (representation)
#         return f'{self.name}-{self.age}'       # переважно повертають те що й в попередньому методі
#
#
#
# user = User('Ivan', 15)
# user.name = 'Zoriana'       # перейменуємо на Zoriana
# print(user.name)
# print(user)           # результат Zoriana. Вивести всього user неможливо, потрібно вище створити нові ф-ції.
#                       # Коли створили __str__ і вказали в return, вказали, що і як повертати, можемо друкувати user.
#                        # коли створені ф-ції рез Zoriana-15


# users = [User('Kateryna', 15), User('Demian', 5)]
# print(users)            # [Kateryna-15, Demian-5]

# user.house = 88     # це додасть поле house до екземплярів класу
# print(user.house)      # рез 88

# users = [User('Kateryna', 15, 88)]
# print(users)                            # видасть помилку, house не записало

# del user.name
# print(user)         # видає помилку, оскільки поля name вже немає

# class User:
#
#     __slots__ =   ('name', 'age')          # дандер метод slots, в ньому прописуємо об'єкт, який ітерується,
#                                           # що в ньому може бути: name та age. Слоти показують поля, які мають бути
#                                           # і економлять оперативну пам'ять
#     count = 8
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#


#   #  приватність
# class User:
#     __count = 9     # модифікатор приватності визначається двома нижніми підкресленнями __ і прописується
#              # змінна  __count. Ці два підкреслення означає, що цією змінною можу користуватись лише в середині класу.
#
#     def __init__(self, name):
#         self.__name = name
#
#
# user = User('Max')          #створюємо екземпляр класу user і передаємо сюди поле name
#
# print(User._User__count)        # так записом можемо доступитися до приватної змінної count, результат: 9
# print(user._User__name)          # так записом можемо доступитися до приватної проперті name, результат: Max.
#                                   # Це зроблено щоб інші програмісти не використовували Ваш клас

#  # Захищений protectred

# class User:
#     __count = 9
#
#     def __init__(self, name):
#         self._name = name      # protected з одним підкресленням, так само як приватність бачить тільки в свому класі,
#                                   # але можна бачити і в нащадках класу
#
# user = User('Max')


# # Наслідування

# class Human:        # будь який клас наслідується від класу object
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class User(Human):          # створюємо клас User і успадкуємо його від класу Human
#     def __init__(self, name, age, house):      # якщо на init натиснути alt enter, він відразу запропонує створити в
#                                                # наступному рядку супер клас. Ми успадкували від Human його property:
#                                                # name і age і в суперконструкторі викликав його init (рядок нижче),
#                                                # Звичайним способом можемо додати ще property: house то написавши
#                                                # house і натиснувши alt enter після суперконструктора наступним
#                                                # рядком буде self.house
#         super().__init__(name, age)             # викликали init
#         self.house = house
#
#
# user = User('Max', 15, 88)                   # створюємо екземпляри класу User, які вимагають поля name, age та house
#
# print(user.name)                          # Max
# print(user.age)                           # 15
# print(user.house)                         # 88

#  #  в python може бути множинне наслідування, до попереднього прикладу додамо клас Tools

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Tools:
#     def greeting(self):         # метод greeting  буде друкувати Hello
#         print('Hello')
#
#
# class User(Human, Tools):              # клас User буде наслідуватись від Human та від Tools
#     def __init__(self, name, age, house):
#         super().__init__(name, age)
#         self.house = house
#
#
# user = User('Max', 15, 88)
#
# print(user.greeting())                  # від екземпляру класу user можна достукатись до методу greeting, рез Hello
#
# print(user.name)
# print(user.age)
# print(user.house)


# # інкапсуляція  ми можемо доступитися до наших змінних через якісь методи (сеттери, геттери)

# class User:
#     def __init__(self, name):   # створимо нову пропертю
#         self.__name = name
#
#     def set_name(self,new_name):   #  створимо метод, метод це ф-ція в межах класу. цей метод буде приймати нове ім'я
#                                  # Щоб працювати з __name потрібнл мати можливість вивести, змінити і видалити змінну
#         self.__name = new_name            # від self буде звертатись до name і він буде дорівнювати new_name
#
#     def get_name(self):
#         return self.__name                  # метод буде витягати name
#
#
#     def delete_name(self):
#         del self.__name                  # метод буде видаляти name
#
#
# user = User('Max')                          # створюємо екземпляр клас
#
#
#                                            #   #   я не маю доступу до свого name приватного, але маю доступ
#                                                 # # до трьох методів, які можуть його змінити
#
# print(user.get_name())                  #  рез Max
# user.set_name('Ira')
# print(user.get_name())                  #  рез Ira
# user.delete_name()
# print(user.get_name())                  # помилка, поля name вже немає


# # покращимо нашу інкапсуляцію

# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __set_name(self, new_name):
#         self.__name = new_name
#
#     def __get_name(self):
#         return self.__name
#
#    def __delete_name(self):
#         del self.__name
#
# name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)  # в ф-цію property встановлюють методи,
#                                                                       # які відповідають за ту чи іншу дію
#
#
# user = User('Max')  # в нас не буде доступів ні до методів ні до змінної
# print(user.name)            # рез Max
#
# user.name = 'Ira'
# print(user.name)            # рез Ira

# del user.name
# print(user.name)            # видає помилку, бо поля name немає


#  # ще більше вдосконалимо: кожну ф-цію назвемо name
# class User:
# #     def __init__(self, name):
# #         self.__name = name
# #
# #     @property  # за допомогою декоратора @property, ф-ція name стає декоратором, @property ставимо перед гетером
# #     def name(self):
# #         return self.__name
# #
# #     @name.setter
# #     def name(self, new_name):
# #         self.__name = new_name
# #
# #     @name.deleter
# #     def name(self):
# #         del self.__name
# #
# #
# # user = User('Max')  # рез Max
# # print(user.name)
# #
# # user.name = 'Ira'
# # print(user.name)  # рез Ira
# #
# # del user.name
# # print(user.name)  # видає помилку, бо поля name немає


#   #  представлення днієї суті за рахунок іншої

# class Shape:
#     def area(self):    # якщо блок пустий, то пишеться pass - це заглушка або ставиться ...
#         pass
#
#     def perymetr(self):
#         pass
#
# class Triangle(Shape):           # клас  Triangle буде успадковуватись від класу Shape
#     def __init__(self, a, b, c):    # створю проперті a, b, c та філди для них
#         self.a = a
#         self.b = b
#         self.c = c
#                       # натиснувши ctrl + o отримаємо класи від яких я успадковувався, вибираємо 2батьківських методи
#
#     def area(self):
#         return self.a*self.b/2
#
#     def perymetr(self):
#         return self.a + self.b + self.c
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#
#     def perymetr(self):
#         return self.a * 2  +  self.b * 2
#
# shapes:list[Shape] = [Triangle(1, 2, 3), Rectangle(3, 4)]     # створимо змінну shapes - це буде список Shape.
#                                                             # Трикутник і прямокутник успадковуються від Shape.
#                                                             # Вводимо сторони трикутника і прямокутника
# for shape in shapes:            # перебиремо shape
#     print(shape.area())         # рез 1.0  12
#     print(shape.perymetr())     # рез 6    14



#                # в нас немає примусовості реалізовувати дії  в класі Shape і це може вплинути на коректність роботи
#                # в таких випадках використовуються абстрактні класи. імпортуємо з бібліотеки abc -abstract basic clas



# from abc import ABC, abstractmethod
#
# class Shape(ABC):          # створюємо клас Shape, який успадкується від ABC
#     @abstractmethod             # створюємо абстрактметод
#     def area(self):         # це буде метод area
#         pass                # він буде пустим
#
#     @abstractmethod
#     def perymetr(self):
#         pass
#
#              ## абстрактний метод від звичайного відрізняється тим, що екземпляр абстрактного класу не можна створити
# class Triangle(Shape):       # створюємо клас, який буде успадковуватись від Shape. Якщо ми успадковуємся від
#     def perymetr(self):      # # абстрактного класу ми повинні або створити абстрактний клас або перенести до нового
#         pass                 # класу - Triangle всі методи від класу який успадковується від Shape. Виділивши  Triangle
#                              # та натиснувши Alt Enter отримаємо 2 пропозиції: зробити клас абстрактним
#     def area(self):          # або імплеиентувати абстрактні методи, потрібно імплеиентувати всі методи
#         pass                # будь який клас, який успадкується від shape буде мати і perymetr і area
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#
#     def area(self):
#         return self.a*self.b/2
#
#     def perymetr(self):
#         return self.a + self.b + self.c
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#
#     def perymetr(self):
#         return self.a * 2  +  self.b * 2
#
# shapes:list[Shape] = [Triangle(1, 2, 3), Rectangle(3, 4)]
#
#
# for shape in shapes:
#     print(shape.area())                   # рез 1.0  12
#     print(shape.perymetr())          # рез 6    14



#  #  статичні і клас методи


# class User:
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __set_name__(self, new_name):       # всі методи екземпляру класу приймають в себе self, щоб ми могли
#        self.name = new_name                 # звертатись до пропертів self.name та self.age. Це звичайний метод класу
#
#                                             #  # є ще клас-методи і стать-методи
#
#     def get_count(self):
#         return User.count
#
# user = User('Max', 15)
#
# print(user.get_count())               # рез 0.
                                        # Некоректно використовувати екземпляр класу при роботі з змінними класу,
                                        # тому перед гетером поставимо @classmethod



# class User:
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __set_name__(self, new_name):       # всі методи екземпляру класу приймають в себе self, щоб ми могли
#        self.name = new_name                 # звертатись до пропертів self.name та self.age. Це звичайний метод класу
#
#                                             #  # є ще клас-методи і стать-методи
#     @classmethod
#     def get_count(cls):                 # cls - це скорочення від клас
#         return cls.count
#
# user = User('Max', 15)
#
# # print(User.get_count())                 # в класу User, викликаємо клас-метод get_count()
#
#  # можемо встановити нове ім'я, але коли працюємо з елементами класу з його зміннимиТо використовуємо клас метод
#  # і те що наведено нижче не робимо

# class User:
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def set_name(self, new_name):
#        self.name = new_name
#
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# user = User('Max', 15)
# print(User.set_name(user, 'Ira'))
#
# print(user.name)

# 53.20

# 48.34


# 38.19
# 11,5

# 21.06

# 29.32
