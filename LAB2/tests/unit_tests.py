import unittest
from lngkpok import find_sequence


class TestFoundSequences(unittest.TestCase):

    def test_output_1(self):
        array = [0, 0, 1, 2, 4, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(find_sequence(array), 14, 'An error occurred while processing your '
                                                                         'request')

    def test_output_2(self):
        array = [0, 0, 5, 5, 5, 6, 6, 6]
        self.assertEqual(find_sequence(array), 4, 'An error occurred while processing your '
                                                        'request')

    def test_output_3(self):
        array = [0, 0, 10, 15, 50, 14, 9, 12, 40]
        self.assertEqual(find_sequence(array), 7, 'An error occurred while processing your '
                                                        'request')

    def test_output_4(self):
        array = [0, 0, 0]
        self.assertEqual(find_sequence(array), 3, 'An error occurred while processing your '
                                                  'request')

    def test_output_5(self):
        array = [1, 1, 1, 3, 3, 2, 2]
        self.assertEqual(find_sequence(array), 3, 'An error occurred while processing your '
                                                  'request')
#
