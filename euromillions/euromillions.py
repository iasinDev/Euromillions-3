"""Retrieve Euromillion results from the national lottery."""
import csv
from urllib.request import urlopen
from datetime import datetime
import codecs

class Euromillions:
    """The base class for all methods."""

    def __init__(self):
        self.src = self._get_source()
        self.raw_data = self._transform_csv()
        self.data = self._parse_results()

    @staticmethod
    def _get_source():
        root = "https://www.national-lottery.co.uk"
        path = "/results/euromillions/draw-history/csv"
        url = f'{root}{path}'
        return urlopen(url)

    def _transform_csv(self):
        return csv.DictReader(codecs.iterdecode(self.src, 'utf-8'))

    @staticmethod
    def _clean_row(row):
        return {
            'draw_date': datetime.strptime(row['DrawDate'], "%d-%b-%Y").date(),
            'balls': [
                row['Ball 1'],
                row['Ball 2'],
                row['Ball 3'],
                row['Ball 4'],
                row['Ball 5']
                ],
            'stars': [row['Lucky Star 1'], row['Lucky Star 2']],
            'miillionaire_maker': row['UK Millionaire Maker'].split(','),
            'draw_number': row['DrawNumber']
            }

    def _parse_results(self):
        """The main function that pulls the results."""
        results = []
        for i in self.raw_data:
            results.append(self._clean_row(i))
        return results

    def get_results(self):
        """Return all gathered results"""
        if len(self.data) > 10:
            return self.data

    def get_latest_draw(self):
        """Return latest draw"""
        if len(self.data) > 10:
            return [self.data[0]]
