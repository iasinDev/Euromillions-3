import json
import csv
import sys, getopt
import requests


#DrawDate,Ball 1,Ball 2,Ball 3,Ball 4,Ball 5,Lucky Star 1,Lucky Star 2,UK Millionaire Maker,DrawNumber


#r = requests.get('https://www.national-lottery.co.uk/results/euromillions/draw-history/csv')
#print(r.content)


f = open( 'sample.csv', 'r' )
reader = csv.DictReader( f, fieldnames = ( "DrawDate","Ball 1","Ball 2","Ball 3","Ball 4", "Ball 5", "Lucky Star 1", "Lucky Star 2", "UK Millionaire Maker", "DrawNumber" ) )
out = json.dumps( [ row for row in reader ], indent=4 )
print(out)
