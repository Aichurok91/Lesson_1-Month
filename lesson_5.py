# Циклы for, while
# 1 ден 1000ге чейинки цифраларды жазып ыгаруу учун
# for numbers in range(1000):
#     print(numbers)

# for py in range(1,10001):
#     print("Python", py)

# numbers = [10, 5, 6, 54, 41, 52, 78, 8, 15, 3, 90, 99]
# print(type(numbers))
# for num in numbers:
#     # print(type(num))
#     if num %2 == 0:
#         print(num, "четный")
#     else:
#         print(num, "нечетный")

# mentors = ("Syimik", "Zhanysh", "Nuris", "Kudbuhon")
# print(mentors)
# for mentor in mentors:   #интерация по циклу for
#     print("Здравствуйте", mentor)

# name = "Aichurok"
# for n in name:
#     print(n)

# nums = []  #пустой список
# print(nums)
# for num in range(100, 151, 2):
#     nums.append(num)
# print(nums)

# while True:
#     print("Geeks")

# num1 = 10
# num2 = 30
# while num2 > num1:
#     num1 += 2
#     print(num1)

# n = 0
# while True:
#     n +=1
#     # n += n+1
#     print("Geeks", n)
#     if n == 20000:
#         print("STOP")
#         break # break заставляет прервать цикл досрочно
#     elif n == 19998:
#         print("CONTINUE")
        # continue #continue  продолжает цикл без остоновки

# import random
# letters = "qwertyuiopasdfghjklzxcvbnm123456789"

# result = ""
# len_password = int(input("Длина пароля:"")
# for i in range(len_password):
#     random_letter = random.choice(letters)
#     result += random_letter
# print(result)

# import random
# cities = ["Osh", "Bishkek", "Naryn", "Batken", "Talas"]
# random_city = random.choice(cities)
# n = 0
# while True:
#     user_city = input("Город: ")
#     if random_city == user_city:
#         print("Вы выиграли")
#         break
#     elif n == 3:
#         print("y вас закончились попытки")
#         break
#     else:
#         n +=1
#         print("Неправильно, y вас", 3 - n, "попыток")
        


# import random
# cities = ["Osh", "Bishkek", "Batken", "Naryn", "Talas"]
# random_city = random.choice(cities)
# n = 0
# while True:
#     if n == 3:
#         print("У вас закончились попытки")
#         break 
#     user_city = input("Город: ")
#     if random_city == user_city:
#         print("Вы выиграли!")
#         break 
#     else:
#         n += 1
#         print("Неправильно, у вас", 3 - n, "попыток")
