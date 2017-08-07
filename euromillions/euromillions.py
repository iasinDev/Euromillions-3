"""Retrieve Euromillion results from the national lottery."""

import csv
from urllib.request import urlopen
from datetime import datetime
import codecs

def _get_source():
    root = "https://www.national-lottery.co.uk"
    path = "/results/euromillions/draw-history/csv"
    return urlopen(f'{root}{path}')

def _transform_csv(csv_=_get_source()):
    return csv.DictReader(codecs.iterdecode(csv_, 'utf-8'))

def _clean_row(row):
    return {
        'draw_date': datetime.strptime(row['DrawDate'], "%d-%b-%Y").date(),
        'balls': [row['Ball 1'], row['Ball 2'], row['Ball 3'], row['Ball 4'], row['Ball 5']],
        'stars': [row['Lucky Star 1'], row['Lucky Star 2']],
        'miillionaire_maker': row['UK Millionaire Maker'].split(','),
        'draw_number': row['DrawNumber']
    }

def get_results():
    """The main function that pulls the results."""
    results = []
    for i in _transform_csv():
        results.append(_clean_row(i))
    return results

def get_latest():
    """Get the latest available set of results."""
    for i in _transform_csv():
        return(_clean_row(i))

if __name__ == '__main__':
    print(get_results())
    print(get_latest())
