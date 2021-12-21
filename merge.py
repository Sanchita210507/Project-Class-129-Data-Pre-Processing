import csv
import pandas as pd

dataset1 = []
dataset2 = []

with open("bright_stars.csv", "r", encoding='utf8') as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        dataset1.append(i)

with open("unit_converted_stars.csv", "r", encoding='utf8') as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        dataset2.append(i)

header1 = dataset1[0]
starsData1 = dataset1[1:]

header2 = dataset2[0]
starsData2 = dataset2[1:]

headers = header1 + header2

starsData = []

for i in starsData1:
    starsData.append(i)

for i in starsData2:
    starsData.append(i)

with open("totalStars.csv", "w", encoding='utf8') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(starsData)

df = pd.read_csv('totalStars.csv')
df.tail(8)
    