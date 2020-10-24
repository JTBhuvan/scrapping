import csv
data1=[]
data2=[]

with open('datasetSorted.csv','r')as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data1.append(row)

with open('final.csv','r')as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data2.append(row)

headers1=data1[0]
planetdata1=data1[1:]

headers2=data2[0]
planetdata2=data2[1:]

headers=headers1+headers2

planetdata=[]

for index,datarow in enumerate(planetdata2):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open('final.csv','a+')as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)