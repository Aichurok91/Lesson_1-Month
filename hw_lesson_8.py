# Задача1

# Дайте пользователю ввести две отметки времени вместе с секундами.
# Ваша программа должна найти разницу между двумя отрезками времени и
# вывести на экран в секундах.
# Условие: Первая отметка должна быть раньше по времени чем вторая.
# Пример:
# 1-ввод: 10:00:30
# 2-ввод: 15:05:09
# Ответ: 18 279 секунд разница

from datetime import datetime

def get_time_difference():
    time_str1 = input("Биринчи убакытты жазыныз (HH:MM:SS): ")
    time_str2 = input("Экинчи убакытты жазыныз (HH:MM:SS): ")

    time_format = "%H:%M:%S"
    try:
        time1 = datetime.strptime(time_str1, time_format)
        time2 = datetime.strptime(time_str2, time_format)
    except ValueError:
        print("Туура эмес: Убакыттын форматы туура эмес жазылган. Колдонунуз HH:MM:SS.")
        exit()
        

    if time1 > time2:
        print("Туура эмес: Биринчи убакыт экинчи убакыттан алдын болушу керек.")
    else:
        time_difference = time2 - time1
        seconds_difference = time_difference.total_seconds()
        print(f"Ответ: {int(seconds_difference)} секунд айырма.")
get_time_difference()

# Задача2
# Напишите функцию которая принимает имя и также его 5 оценок и выводит
# среднее значение его оценок
def a(name, grades):
    b = sum(grades)/len(grades)
    print(f"Cреднее значение оценок для {name}: {b}")

a("Aichurok", [4,5,5,3,4])


# ДОП ЗАДАНИЕ:
# Задача3
# Эти две функции вызовите на другом файле (moduls_8.py) с 3 способами
# импорта