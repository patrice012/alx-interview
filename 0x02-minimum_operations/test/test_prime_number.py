#!/usr/bin/python3
"""
Main file for testing
"""

import unittest
import sys

sys.path.append("../../0x02-minimum_operations")
primeFactorization = __import__("0-minoperations").primeFactorization


class TestPrimeFactorization(unittest.TestCase):
    """
    Unit tests for minOperations
    """

    def test_positive_numbers(self):
        elements_to_test = [1, 12]
        excepted_results = [[], [2, 2, 3]]

        for element, result in zip(elements_to_test, excepted_results):
            with self.subTest(element=element, result=result):
                self.assertEqual(primeFactorization(element), result)


if __name__ == "__main__":
    unittest.main()
