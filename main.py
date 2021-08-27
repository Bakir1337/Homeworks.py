
# GIT. Контроль версий

# !!! Все неизвестные команды нужно гуглить

# 0. Создайте репозиторий на GitHub с названием MyRepo

# 1. Откройте терминал
ctrl + alt + T

# 2. Откройте документацию гит в терминале специальной командой.
#  Покопайтесь в ней :)
git help

# 3. Создайте папку test на рабочем столе,
# После создайте в вашей папке test файл main.py и напишите в нем функцию которая выдает в консоль 'Hello World!'
# Затем перейдите в папку через терминал
# Для того чтобы добавить файл в репозиторий на гитхаб, инициализируйте локальный репозиторий.
cd Desktop
mkdir test
cd test
touch main.py
git init
git remote add origin url

# 4. Затем скажите Git добавить копии содержимого всех файлов в текущей папке в локальный репозиторий
git add .

# 5. Эти копии теперь хранятся во временной промежуточной области, которую Git называет «индексом». Для того чтобы содержимое индекса в репозитории перевести из промежуточной области в постоянное хранилище создайте commit
git commit -m "imma nigga and whiteguy"

# 6. Выведите статус работы с гитом в терминал
git status

# 7. C помощью специальной команды посмотрите историю изменений (логов)
git log


# 8. Создайте новую ветку mybranch через терминал.
git branch mybranch

# 9. Переключитесь на новую ветку mybranch. Проверьте статус
git checkout mybranch

# 10. Измените код в вашем файле main.py
# Теперь ваша функция должна выводить "Python is awesome!"
# in python
print(""Python is awesomee!"")

# 11. Создайте новый коммит с комментарием "исправил функцию, добавил новое сообщение".
git add .
git commit -m "исправил функцию, добавил новое сообщение!"

# 12. Переключитесь назад на ветку master и проверьте есть ли изменения которые вы совершили на ветке mybranch
git checkout master
git log mybranch

# 13. На данный момент две ветки отличаются. Соедините их командой merge

git add .
git commit -m "Commit before merging"
git merge mybranch

# 14. Запуште ваш файл к себе на репозиторий MyRepo

git push origin master




"""
1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.
"""
# class Class1:
   
#     def get_fruits(self):
#        print('You must not eat these')
        

#     def get_mandarin(self):
#         print('Great choice')
# class Class2(Class1):
    
#     def vegetables(self):
#         print('You should eat healthy food')
#     def carrot(self):
#           print('It is healty for teeth')
# healthy_food = Class2()
# healthy_food.get_fruits()
# healthy_food.get_mandarin()
# healthy_food.vegetables()
# healthy_food.carrot()
"""
2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.
"""
# class A:

#     def method1(self):
#         print('Основной функционал')

# class B(A):
    
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# word = B()
# word.method1()
"""
3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
append, который будет принимать строку и добавлять её в конец исходной
pop, который удаляет из строки последний элемент и возвращает его.
Пример:
# example = MyString('String')
# example.append('hello')
# print(example) -> 'Stringhello'
# print(example.pop()) -> 'o'
# print(example) -> 'Stringhell'
"""
# class MyString(str):

#     def __init__(self, string):
#         self.string = string

#     def append(self, new_word):
#         self.string += new_word

#     def pop(self): 
#         self.elem = self.string[-1]
#         self.string = self.string[:-1]
#         return self.elem
    
#     def __str__(self):
#         return self.string

# sample = MyString('Just do it')
# sample.append('--> Nike')

# print(sample.pop())
# print(sample)
"""
4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.
"""
# class MyDict(dict):
#     def get(self,key,default='Are you kidding?'):
#         return super().get(key,default)

# my_dict1 = MyDict({'g':8,'k':0})
# print(my_dict1.get('m'))
"""
5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.
Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.
Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
"""
# class Person:
    
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
        

#     def display(self):
#         return f'Info: {self.name} {self.last_name}, Age: {self.age}'

# class Student(Person):
    
#     def __init__(self, name, last_name, age, faculty, id_num):
#         super().__init__(name, last_name, age)
#         self.faculty = faculty
#         self.id_num = id_num

#     def display_student(self):
#         return f'Info студента: {self.name} {self.last_name}, Age: {self.age}, ID: {self.id_num}, Faculty {self.faculty}'


# p = Person(name='Melissa', last_name='Gilbert', age=19)
# print(p.display())
# s = Student(name='Nina', last_name='Mikson', age=20, id_num=986574, faculty = 'phylology')
# print(s.display_student())
"""
6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.
"""
# class ContactList(list):

#     def __init__(self, name_cont):
#         self.name_cont = name_cont

#     def seek(self, name):
#         self.name = name
#         list_ = []
#         for i in self.name_cont:
#             if name == i:
#                 list_.append(i)
#         return list_
        
        
# contacts = ContactList(['Chynara', 'Bektur', 'Marat', 'Zaure', 'Akyw'])
# print(contacts.seek('Bektur'))
