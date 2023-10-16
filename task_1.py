class AverageInNumLists():

    def __init__(self):
        self

    def find_average_in_num_list(self, list1):
        try:
            return round(sum(list1) / len(list1), 2)

        except ZeroDivisionError:
            raise ZeroDivisionError("List is empty")

        except TypeError:
            raise TypeError("Incorrect input data")

    def compare_averages(self, average1, average2):
        try:
            if average1 > average2:
                return "Первый список имеет большее среднее значение"
            elif average1 < average2:
                return "Второй список имеет большее среднее значение"
            else:
                return "Средние значения равны"

        except TypeError:
            raise TypeError("Incorrect average result")
