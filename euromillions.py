import csv
from pprint import pprint
import urllib2
import datetime

def getResults():
    results = []
    r= urllib2.urlopen("https://www.national-lottery.co.uk/results/euromillions/draw-history/csv")
    reader = csv.reader(r)
    data = list(reader)
    row_count = len(data)
    for i in range(0,row_count):
        if i != 0:
            drawDate = datetime.datetime.strptime(data[i][0], "%d-%b-%Y").date()
            balls = [data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]]
            luckyStars = [data[i][6],data[i][7]]
            millionaireMaker = data[i][8]
            drawNumber = data[i][9]
            result = {"DrawDate": drawDate, "Balls": balls,"LuckyStars": luckyStars,"MillionaireMaker": millionaireMaker, "DrawNumber": drawNumber}
            results.append(result)
    return results
