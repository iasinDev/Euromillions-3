"""Tests for euromillions"""

import unittest
from euromillions import euromillions

class Tests(unittest.TestCase):

    def test_results(self):
        status = True
        try:
            euromillions.get_results()
            euromillions.get_latest()
        except Exception:
            status = False
        self.assertTrue(status, 'Failed completion')
