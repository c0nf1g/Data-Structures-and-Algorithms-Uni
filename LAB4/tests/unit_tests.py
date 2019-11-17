import unittest
from find_order import dfs
from read_file import read_file


class TestFoundSequences(unittest.TestCase):

    def test_output_1(self):
        order_list = []
        graph = read_file("D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB4\\resources\\data1")
        visited = {k: False for k in graph}
        self.assertEqual(dfs("visa", graph, visited, order_list), ['birthcertificate',
                                                                   'nationalpassport',
                                                                   'militarycertificate',
                                                                   'foreignpassport',
                                                                   'creditcard',
                                                                   'hotel',
                                                                   'bankstatement',
                                                                   'visa'], 'An error occurred while processing your '
                                                                            'request')

    def test_output_2(self):
        order_list = []
        graph = read_file("D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB4\\resources\\data2")
        visited = {k: False for k in graph}
        self.assertEqual(dfs("visa", graph, visited, order_list), ['foreignpassport', 'visa'],
                         'An error occurred while processing your '
                         'request')
