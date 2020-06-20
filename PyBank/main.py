import os
import csv

total_months = 0
previous_value = 0
total_profit_loss = []
average_change = []




csvpath = os.path.join("Resources", "data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for line in csvreader:
        total_months += 1
        total_profit_loss.append(int(line[1]))
        if previous_value != 0:
            average_change.append(int(line[1]) - previous_value)
        previous_value = int(line[1])
        
        
    
       
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(sum(total_profit_loss)))
    print("Average Change: " + "$" + str(round(sum(average_change)/len(average_change), 2)))
    print("Greatest Increase in Profits: " + "$" + str(max(average_change)))
    print("Greatest Decrease in Profits: " + "$" + str(min(average_change)))
