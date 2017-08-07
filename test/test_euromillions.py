"""Tests for euromillions"""

import unittest
from euromillions import euromillions

class Tests(unittest.TestCase):
    """Tests for euromillions module"""

    def setUp(self):
        self.data = euromillions.Euromillions()

    def test_results(self):
        """Test Euromillions.get_results()"""
        self.assertTrue(len(self.data.get_results()) > 20, len(self.data.get_results()))


    def test_latest(self):
        """Test Euromillions.get_latest_draw()"""
        self.assertTrue(len(self.data.get_latest_draw()) is 1,len(self.data.get_latest_draw()))
