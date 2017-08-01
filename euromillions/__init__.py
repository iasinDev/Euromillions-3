"""Retrieve Euromillion results from the national lottery."""

import csv
from urllib.request import urlopen
from datetime import datetime
import codecs

def get_results():
    """The main function that pulls the results."""
    results = []
    response = urlopen(
        "https://www.national-lottery.co.uk/results/euromillions/draw-history/csv"
        )
    data = csv.DictReader(codecs.iterdecode(response, 'utf-8'))
    for i in data:
        pretty_date = datetime.strptime(i['DrawDate'], "%d-%b-%Y").date()
        results.append({
           'draw_date': pretty_date,
           'balls': [i['Ball 1'], i['Ball 2'], i['Ball 3'], i['Ball 4'], i['Ball 5']],
           'stars': [i['Lucky Star 1'], i['Lucky Star 2']],
           'miillionaire_maker': i['UK Millionaire Maker'].split(','),
           'draw_number': i['DrawNumber']
       })

    return results

if __name__ == '__main__':
    print(get_results())
