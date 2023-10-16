from unittest import TestCase
import pytest

from task_1 import AverageInNumLists


class TestAverageInNumListsCorrect(TestCase):

    average_test = AverageInNumLists()
    list1 = [67, -9, 1, -20, 22, 5]
    list2 = [8, 4, 0, -5, 10]

    def test_find_average_in_num_lists_correct_input_data(self):
        assert self.average_test.find_average_in_num_list(self.list1) == 11.0
        assert self.average_test.find_average_in_num_list(self.list2) == 3.4


class TestAverageInNumListsEmptyList(TestCase):
    average_test = AverageInNumLists()
    list_empty = []

    def test_find_average_in_num_lists_empty_list(self):
        with pytest.raises(ZeroDivisionError):
            self.average_test.find_average_in_num_list(self.list_empty)


class TestAverageInNumListsIncorrectDataList(TestCase):
    average_test = AverageInNumLists()
    list_incorrect = ['w', 'r', 'u']

    def test_find_average_in_num_lists_incorrect_data(self):
        with pytest.raises(TypeError):
            self.average_test.find_average_in_num_list(self.list_incorrect)


class TestAverageInNumListsIncorrectData(TestCase):
    average_test = AverageInNumLists()
    not_list = 2

    def test_find_average_in_num_lists_incorrect_data(self):
        with pytest.raises(TypeError):
            self.average_test.find_average_in_num_list(self.not_list)


class TestAverageInNumListsAverage1(TestCase):
    average_test = AverageInNumLists()

    def test_compare_averages_list1_average_larger(self):
        assert self.average_test.compare_averages(
            11.0, 3.4) == 'Первый список имеет большее среднее значение'


class TestAverageInNumListsAverage2(TestCase):
    average_test = AverageInNumLists()

    def test_compare_averages_list2_average_larger(self):
        assert self.average_test.compare_averages(
            3.4, 11) == 'Второй список имеет большее среднее значение'


class TestAverageInNumListsAveragesEqual(TestCase):
    average_test = AverageInNumLists()

    def test_compare_averages_equal(self):
        assert self.average_test.compare_averages(
            3.4, 3.4) == 'Средние значения равны'

class TestAverageInNumListsIncorrectAverage1(TestCase):
    average_test = AverageInNumLists()

    def test_compare_averages_incorrect_input_data(self):
        with pytest.raises(TypeError):
            self.average_test.compare_averages('a', 3.4)

class TestAverageInNumListsIncorrectAverage2(TestCase):
    average_test = AverageInNumLists()

    def test_compare_averages_incorrect_input_data(self):
        with pytest.raises(TypeError):
            self.average_test.compare_averages(3.4, 'a')

