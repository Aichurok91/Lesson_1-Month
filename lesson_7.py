#Dictionary словари
# типы данных: list, integer, tuple, bool, set, frozenset, float, str/
# student= {"name":"Aichurok", 'age': 32}
# print(type(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('language', 'python') #метод для добавления в список
# print(student)
# student.pop('age') #метод для удаления из списка по ключу
# print(student)
# student['language'] = "Java" #Синтаксис для обновления значения по ключу
# print(student)
# print(student.keys()) #метод для получения ключей из словаря
# print(student.values()) #метод для получения значений из словаря
# print(student.items()) #метод для получения ключи и значения за раз

# geeks = {'name': 'Geeks', "count_students": 340, 'address': "Amatova 1B"}
# print(geeks)
# # for geek in geeks.items():
# #     print(geek)
# for key, value in geeks.items():
#     print(key, value)

# dct = {}
# print(type(dct))

# contact = {'MCHS': 112}
# while True:
#     command = input("1 - посмотреть, 2 - добавить, 3- удалить, 4 - обновить:")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("Имя: ")
#         add_number = input("Номер: ")
#         contact.setdefault(add_name, add_number)
#         print("Контакт", add_name, "Успешно добавлен")
#     elif command == "3":
#         remove_name = input("Кого удалить? ")
#         contact.pop(remove_name)
#         print("Контакт", remove_name, "Успешно удален")
#     elif command == "4":
#         update_name = input("Кого обновить? ")
#         update_number = input("Новый номер: ")
#         contact[update_name] = update_number
#         print("Номер контакта", update_name, "успешно обнавлен на", update_name)
#     else:
#         print("Такой команды нету")

# unctions - функции
# def hello():
#     print("Hello World")
# hello()

# def wellcome():
#     name = input("Имя: ")
#     print("Привет", name)
# wellcome()

# def add():
#     num1 = int(input("Первое число: "))
#     num2 = int(input("Второе число: "))
#     print(num1+num2)
# add()

# def mult(num1, num2): #num1 num 2 является параметром функции mult
#     print(num1 + num2)
# mult(5, 3) #числа 5 и 3 являются аргументами функции
# mult(100, 200)

# def div(num1, num2):
#     try:
#         print(num1 / num2)
#     except ZeroDivisionError:
#         print("На ноль делть нельзя")
# div(81,3)
# div(100,0)