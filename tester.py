import requests
import json
import csv

with open('testerfile.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['city'])

    f = open('cities.json')
    data = json.load(f)

    for city in data:
       location = city['city'] 
       thewriter.writerow([location])

    f.close()