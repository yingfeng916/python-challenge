import os
import csv

total_months = 0
previous_value = 0
sum_of_change = 0
total_profit_loss = []
average_change = []
max_change = []
min_change = []


csvpath = os.path.join("Resources", "data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for line in csvreader:
        total_months += 1
        total_profit_loss.append(int(line[1]))
        if previous_value != 0:
            average_change.append([line[0], int(line[1]) - previous_value])
        previous_value = int(line[1])

    max_change = average_change[0]
    min_change = average_change[0]
    
    for line in average_change:
        sum_of_change += line[1]
        if max_change[1] < line[1]:
            max_change = line
        elif min_change[1] > line[1]:
            min_change = line

       
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(sum(total_profit_loss)))
print("Average Change: " + "$" + str(round((sum_of_change)/len(average_change), 2)))
print("Greatest Increase in Profits: " + str(max_change[0]) + " $" + "(" + str(max_change[1]) + ")")
print("Greatest Decrease in Profits: " + str(min_change[0]) + " $" + "(" + str(min_change[1]) + ")")

txtpath = os.path.join("Financial Analyst.txt")
txtFile = open(txtpath, "w")
   
print("Financial Analysis", file=txtFile)
print("------------------------", file=txtFile)
print("Total Months: " + str(total_months), file=txtFile)
print("Total: " + "$" + str(sum(total_profit_loss)), file=txtFile)
print("Average Change: " + "$" + str(round((sum_of_change)/len(average_change), 2)), file=txtFile)
print("Greatest Increase in Profits: " + str(max_change[0]) + " $" + "(" + str(max_change[1]) + ")", file=txtFile)
print("Greatest Decrease in Profits: " + str(min_change[0]) + " $" + "(" + str(min_change[1]) + ")", file=txtFile)
txtFile.close()
    
