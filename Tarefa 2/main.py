import csv

with open('userprofile.csv','r') as arquivo:
    reader = csv.DictReader(arquivo,delimiter=',')
    for coluna in reader:
        print(coluna['smoker'])