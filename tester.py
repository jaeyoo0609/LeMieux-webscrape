import requests
import json
import csv

while True:
    userInput = input('Desired state: ')

    with open(userInput + 'cities.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)

        f = open('cities.json')
        data = json.load(f)

        for city in data:
            if city['state'] == userInput:
                thewriter.writerow([city['city']])

        f.close()

        answer = input('Again?(y/n): ')
        if answer == 'y':
            continue
        else:
            print('Done.')
            break