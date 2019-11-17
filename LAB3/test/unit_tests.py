import unittest
from find_cycle import check_cycle
from read_file import read_file


class TestFoundSequences(unittest.TestCase):

    def test_output_1(self):
        graph = read_file("D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB3\\resources\\data1")[0]
        vertex_num = read_file("D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB3\\resources\\data1")[1]
        self.assertEqual(check_cycle(graph, vertex_num, 0), [0, 5, 10], 'An error occurred while processing your '
                                                                        'request')

    def test_output_2(self):
        graph = read_file("D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB3\\resources\\data2")[0]
        vertex_num = read_file("D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB3\\resources\\data2")[1]
        self.assertEqual(check_cycle(graph, vertex_num, 8), False, 'An error occurred while processing your '
                                                                   'request')

    def test_output_3(self):
        graph = read_file("D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB3\\resources\\data3")[0]
        vertex_num = read_file("D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB3\\resources\\data3")[1]
        self.assertEqual(check_cycle(graph, vertex_num, 20), [20, 127, 131, 154, 46, 70, 73, 163, 125, 98],
                         'An error occurred while processing your '
                         'request')
