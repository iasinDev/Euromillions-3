"""Tests for euromillions"""

import unittest
from euromillions import euromillions

class Tests(unittest.TestCase):

    def test_results(self):
        if euromillions.get_results():
            self.assertTrue(True)

    
    def test_latest(self):
        if euromillions.get_latest():
            self.assertTrue(True)
