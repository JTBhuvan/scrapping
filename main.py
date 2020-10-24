import csv

data=[]

with open('dataset.csv','r')as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)

headers=data[0]
planetdata=data[1:]

for dataPoint in planetdata:
    dataPoint[2]=dataPoint[2].lower()

planetdata.sort(key=lambda planetdata: planetdata[2])
with open('datasetSorted.csv','a+')as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)