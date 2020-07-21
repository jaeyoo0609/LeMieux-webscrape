import csv

desCity = input('Desired State: ')

with open(desState + 'cities.csv') as csvfile:
    readCSV = csv.reader(csvfile)

    for row in readCSV:
        print(row[0])
