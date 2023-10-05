#Исключение
#try, except
# try: 
#     num1 = 10
#     num2 = 0
#     print(num1/num2)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# while True:
#     try:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         print(f"Результат после сложения: {num1+num2}")
#         print(f"Результат после вычитания: {num1-num2}")
#     except ValueError:
#         print(f"Введите число!!!")

#set, frozenset
# num = {2, 3, 4, 5, 6, 1, 3,}
# print(num)
# print(type(num))
# не имеет дубликатов
# не имеет структуры и порядка
# не может использовать индексы  и срезы
# изменяемых тип данных

# name = {"Ainazik", "Bibisara", "Dior", "Nuris"}
# print(name)

# num = {1, 5, 6, 8, "1"}
# print(num)

# try:
#     num = {1,2,3,4,5,6,7,8}
#     print(num[3])
# except:
#     print("Set() Не можеть использовать индексы и срезы")

# num = {1,2,3,4}
# num.add(5)
# num.add(5)
# print(num)
# num.remove(2)
# print(num)

# names = frozenset(["Aichurok", "Duria", "Naima", "Nazgul"])
# print(type(names))
# print(names)
# names.add("Maha")
# names.remove("Naima")
# print(names)
