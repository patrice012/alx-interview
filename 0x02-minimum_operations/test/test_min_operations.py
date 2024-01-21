#!/usr/bin/python3
"""
Main file for testing
"""

import unittest
import sys

sys.path.append("../../0x02-minimum_operations")
minOperations = __import__("0-minoperations").minOperations


class TestMinOperations(unittest.TestCase):
    """
    Unit tests for minOperations
    """

    def test_positive_numbers(self):
        elements_to_test = [1, 4, 12]
        excepted_results = [0, 4, 7]

        for element, result in zip(elements_to_test, excepted_results):
            with self.subTest(element=element, result=result):
                self.assertEqual(minOperations(element), result)

    def test_negative_numbers(self):
        elements_to_test = [-1, -5, -8888]

        for element in elements_to_test:
            with self.subTest(element=element):
                self.assertEqual(minOperations(element), 0)

    def test_with_decimal_numbes(self):
        elements_to_test = [1.5487, -5.778, -888.8]

        for element in elements_to_test:
            with self.subTest(element=element):
                self.assertEqual(minOperations(element), 0)


if __name__ == "__main__":
    unittest.main()
