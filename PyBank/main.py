import os
import csv

csvpath = os.path.join("Resources", "data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    
    
