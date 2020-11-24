import unittest
from main import count_elements_in_string, get_pow_arr
from random import randint

class MyTestCase(unittest.TestCase):
    def test_element_is_one(self):
        self.assertEqual(count_elements_in_string("1111", 1), 4)

    def test_one_element(self):
        self.assertEqual(count_elements_in_string("11111110100010001", 19), 1)

    def test_from_task(self):
        self.assertEqual(count_elements_in_string("101101101",  5), 3)
        self.assertEqual(count_elements_in_string("1111101", 5), 1)
        self.assertEqual(count_elements_in_string("110011011", 5), 3)
        self.assertEqual(count_elements_in_string("10011101111010010011111011001110010100011110010111001000110011101111"
                                                  "0100100111110110011100101000110010110000111100101110010001", 7), 5)

