import unittest
from algo import find_max
from read_file import read_file


class TestFoundSequences(unittest.TestCase):

    def test_output_1(self):
        out_file = 'D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\out\\out1'
        array = read_file('D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\data\\data1')[1]
        word_num = read_file('D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\data\\data1')[0]
        paths = {}
        self.assertEqual(find_max(array, paths, out_file, word_num), 6, 'An error occurred while processing your '
                                                                         'request')

    def test_output_2(self):
        out_file = 'D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\out\\out2'
        array = read_file('D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\data\\data2')[1]
        word_num = read_file('D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\data\\data2')[0]
        paths = {}
        self.assertEqual(find_max(array, paths, out_file, word_num), 4, 'An error occurred while processing your '
                                                                        'request')

    def test_output_3(self):
        out_file = 'D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\out\\out3'
        array = read_file('D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\data\\data3')[1]
        word_num = read_file('D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\data\\data3')[0]
        paths = {}
        self.assertEqual(find_max(array, paths, out_file, word_num), 1, 'An error occurred while processing your '
                                                                        'request')
