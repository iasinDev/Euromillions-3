import csv
from pprint import pprint


#https://www.national-lottery.co.uk/results/euromillions/draw-history/csv

results = {}
with open("results.csv","r") as f:
    reader = csv.reader(f)
    data = list(reader)
    row_count = len(data)
    for i in range(0,row_count):
        if i != 0:
            drawDate = data[i][0]
            balls = [data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]]
            luckyStars = [data[i][6],data[i][7]]
            millionaireMaker = data[i][8]
            drawNumber = data[i][9]
            results[drawDate] = {"Balls": balls,"Lucky Stars": luckyStars,"Millionaire Maker": millionaireMaker, "Draw Number": drawNumber}
pprint(results)
