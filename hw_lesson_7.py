# # Задача1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

#Задача2
#Дан словарь с числовыми значениями. numbers = {‘num_1’ : 1, ‘num_2’ : 2, ‘num_3’ :3, ‘num_100’ : 100}
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' :3, 'num_100' : 100}
# result = {}
# for key, valuve in numbers.items():
#     result[key] = valuve*5
# print(result)

# Задача3
# Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Умножьте его age на 2 раза
# student = {'name' : 'Askhat', 'age' : 17}
# num = 2
# for age in student:
#     age = num * student['age']
# print(age)

# Задача4
# # Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17, ‘color’ : ‘White’}. Обновите age в 16
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = "16"
# print(student)

# Задача5
#  Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Удалите ключ и значение age
# student = {'name': 'Askhat', 'age' : 17}
# student.pop('age','17')
# print(student)

# Задача6
# Есть словарь student = {‘name’ : ‘Askhat’}. Добавьте новый ключ(address) и значение(Западный Анар)''
# student = {'name' : 'Askhat'}
# student.setdefault('Address', 'Западный Анар')
# print(student)

# Задача7
# Напишите функцию, которая принимает фразу, и возвращает его сокращенную
# форму. Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest
# -- FYI и т.п
# def fraza():
#     user = input("Введите фразу: ")
#     user1 = user.split() 
#     a = []
#     for word in user1:
#         a.append(word[0].upper())
#     b = "".join(a)
#     print(b)
# fraza()

# Задача8
# Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
# фразе было использовано.
# Например: “Money, money, money, it’s always sunny, in the richmen’s world”. money: 3, it’s:
# 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.

# def valut():
#     valut = "Money, money, money, it's always sunny, in the richmen's world".lower()
#     print("money:", valut.count("money"))
#     print("it's:", valut.count("it's"))
#     print("always:", valut.count("always"))
#     print("sunny:", valut.count("sunny"))
#     print("in:", valut.count("in"))
#     print("the:", valut.count("the"))
#     print("richmen's:", valut.count("richmen's"))
#     print("world:", valut.count("world"))
valut()

# Задача9
# Напишите функцию, которая принимает слово и возвращает True, если слово
# изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False.
# def isogram(word):
#     unique_letters = set()
#     for letter in word:
#         if letter in unique_letters:
#             return False
#         unique_letters.add(letter)
#     return True
# word1 = "hello" 
# word2 = "world"
# word3 = "algorithm"
# print(isogram(word1))  
# print(isogram(word2)) 
# print(isogram(word3))

# Задача10
# Напишите функцию где мы передаем через аргументы число n как целое integer, надо вывести целое число в перевернутом виде например: n = 27, тогда перевёрнутое
# n это 72
# def n(a):
#     a_n = int(str(a)[::-1])
#     print(a_n)
# n(2745)

# Д.Задача11
# 11) Напишите функцию -- чат-бот с бесконечным циклом, который
# a. Всегда отвечает “Конечно!” на любой вопрос
# b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же духе!” Если
# вызвал функцию, но ничего не передал.
# d. В любых других случаях, отвечает “ну и что

# def user(): 
#     while True:
#         user = input("Можете задать вопрос: ")
#         if user.find("?")>=0:
#             print("Конечно!")
#         elif user.find("!")>=0:
#             print("Успокойся")
#         elif user == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("ну и что")
# user()


