# Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.
#
# Важно:
# Приложение должно быть написано в соответствии с принципами объектно-ориентированного программирования.
# Используйте Pytest (для Python) или JUnit (для Java) для написания тестов, которые проверяют правильность работы программы.
# Тесты должны учитывать различные сценарии использования вашего приложения.
# Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.
# Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.
from task_1 import AverageInNumLists
import random


def main():
    average_in_2_lists = AverageInNumLists()
    numbers1, numbers2 = [], []
    for i in range(random.randint(7, 10)):
        numbers1.append(random.randint(-100, 100))
        numbers2.append(random.randint(-100, 100))

    print(numbers1)
    print(numbers2)


    average1 = average_in_2_lists.find_average_in_num_list(numbers1)
    average2 = average_in_2_lists.find_average_in_num_list(numbers2)
    print(f'\nAverage in list 1 = {average1}, average in list 2 = {average2}\n')

    print(average_in_2_lists.compare_averages(average1, average2))


if __name__ == '__main__':
    main()
