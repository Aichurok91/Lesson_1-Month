#Задача1
# for py in range(1,6):
#      print("№", py, 0)

#Задача2
# numbers = []
# for py in range(1,101):
#      numbers.append(py)
# print(numbers)

#Задача3
# for py in range(1,497):
#     if py %2 == 0:
#       print(py, "четный")

#Задача4
# numbers = list(range(1,1001))
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# # print(sum(numbers))

# #Задача5
# numbers = []
# for py in range(1,101):
#     numbers.append(0)
# print(numbers)

# Задача6
# Создайте кортеж it_company = (‘Google’, ‘Amazon’, ‘Microsoft’) вам
# нужно превратить кортеж в список и добавить новое значение ‘Tesla’,
# затем превращаете список обратно в кортеж

# it_company = ('Google', 'Amazon', 'Microsoft')
# a = list(it_company)
# print(it_company)
# a.append('Tesla')
# print(tuple(a)) 

# # Задача7
# Из 1 задания попробуйте вывести индекс 'Amazon'
# it_company = ('Google', 'Amazon', 'Microsoft')
# print(it_company.index("Amazon"))

# задача8
# Из 1 задания обновите значение ‘Google’ на ‘Apple’ любыми способами
# it_company = ('Google', 'Amazon', 'Microsoft')
# a = list(it_company)
# a[0] = 'Apple'
# print(tuple(a))

# Задача9
# Из 1 задания сделайте срез ‘Apple’ до ‘Microsoft’
# it_company = ['Apple', 'Amazon', 'Microsoft']
# print(it_company[0:3])

# Задача10
# Есть кортеж text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other',
# 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the',
# 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your',
# 'appetite', 'with', 'our', 'Python', '3', 'overview') вам нужно посчитать сколько
# раз встречается слово python

# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other',
# 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the',
# 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your',
# 'appetite', 'with', 'our', 'Python', '3', 'overview')
# print(text_tuple.count('Python'))

# ДОП ЗАДАНИЕ:
# Задача11
# Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на
# # экран. Решите задачу, используя только две переменные.
# name = input("Сиздин атыңыз: ")
# surname = input("Сиздин фамилияңыз: ")
# print(f"Сиздин атыңыз: {surname}")
# print(f"Сиздин фамилияныз: {name}")

# # Задача12
# Создайте бесконечный цикл. Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен" и остановите цикл,иначе "Извините, пользование данным ресурсом только с 18 лет" и
# # запросите заново.
# while True:
    # age = int(input("Ваш возраст: "))
    # if age >= 18:
    #     print("Доступ разрешен")
    #     break
    # else:
    #     print("Извините, пользование данным ресурсом только с 18 лет")