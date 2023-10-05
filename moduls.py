# Модули - это Python файл
# В Pythonмодули можно импортировать 3 способами
# 1 - импортировать сам модуль
# import lesson_8 #без окончания .ру
# print(lesson_8.hello()) #вызываем функцию из модули Lesson_8
# print(lesson_8.three_add(10, 10, 10))

# 2 - импортировать отдельные определения из модуля
# from lesson_8 import hello
# print(hello()) #вызываем функции из другого модуля Python

# from lesson_8 import hello, three_add
# print(three_add(10, 10, 10))

# 3 - импортировать все содержимое модуля сразу 
# from lesson_8 import * #оператор (*) означает все(весь)
# print(hello())
# print(three_add(5, 5, 5))