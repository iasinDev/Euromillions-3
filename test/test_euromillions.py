"""Tests for euromillions"""

import unittest
from Euromillions import euromillions

class Tests(unittest.TestCase):

    def test_url(self):
        """Test url is valid"""
        src = euromillions._get_source()
        status = src.getcode()
        self.assertEqual(status, 200)


    def test_data_is_dict(self):
        """Test lottery data is dict"""
        status = True
        for i in euromillions._transform_csv():
            if not isinstance(i, dict):
                status = False
        self.assertTrue(status, "csv data is not a dict")

    def test_results(self):
        status = True
        try:
            euromillions.get_results()
            euromillions.get_latest()
        except Exception:
            status = False
        self.assertTrue(status, 'Failed completion')
