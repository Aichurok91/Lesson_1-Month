#Задача1
# Задача о делении на ноль: Напишите программу, которая запрашивает у пользователя два числа 
# и пытается поделить первое число на второе. Используйте блок try-except для обработки 
# возможной ошибки деления на ноль.

# num1=int(input("Введите первое число: "))
# num2=int(input("Введите второе число: "))
# try: 
#        print(num1/num2)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")


# Задача2
# Задача о преобразовании строки в число: Запросите у пользователя ввод строки, 
# которая представляет собой число. Попробуйте преобразовать эту строку в число 
# с помощью функции int() или float(). Используйте блок try-except, чтобы обработать 
# исключение, которое возникает, если введенная строка не является числом.
# try:
#     user_input = input("Введите строку, представляющую число: ")
#     number = float(user_input)   
#     print("Вы ввели число:", number)
# except ValueError:
#     print("Ошибка: Введенная строка не является числом.")


# Задача3
# Напишите программу, которая принимает на вход текстовую строку и выводит 
# количество уникальных слов в этой строке. Используйте как set, так и frozenset 
# для выполнения этой задачи.

# text = "количество уникальных слов в этой строке"
# words = set(text.split())
# unique_words = len(words)
# print("Количество уникальных слов:", unique_words)



# Доп.задание

# Напишите программу, которая находит общие элементы в двух списках и выводит их с использованием set и frozenset. 
# Затем выведите результаты на экран.
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# set1 = set(list1)
# set2 = set(list2)
# common_elements = set1.intersection(set2)
# print("Общие элементы, используя set:", common_elements)
# frozen_set1 = frozenset(list1)
# frozen_set2 = frozenset(list2)
# frozen_common_elements = frozen_set1.intersection(frozen_set2)
# print("Общие элементы, используя frozenset:", frozen_common_elements)

