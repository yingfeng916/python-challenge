import os
import csv

total_months = 0
previous_value = 0
sum_of_change = 0
total_profit_loss = []
average_change_list = []
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
            average_change_list.append([line[0], int(line[1]) - previous_value])
        previous_value = int(line[1])

    max_change = average_change_list[0]
    min_change = average_change_list[0]
    
    for line in average_change_list:
        sum_of_change += line[1]
        if max_change[1] < line[1]:
            max_change = line
        elif min_change[1] > line[1]:
            min_change = line

sum_of_profit_loss = sum(total_profit_loss)
average_change = round((sum_of_change)/len(average_change_list), 2)

output = "Financial Analysis \n\
------------------------\n\
Total Months: " + str(total_months) + "\n\
Total: $" + str(sum_of_profit_loss ) + "\n\
Average Change: $" + str(average_change) + "\n\
Greatest Increase in Profits: " + str(max_change[0]) + " $" + "(" + str(max_change[1]) + ")" + "\n\
Greatest Decrease in Profits: " + str(min_change[0]) + " $" + "(" + str(min_change[1]) + ")"

#print to screen
print(output)

#write to file
txtpath = os.path.join("Financial Analyst.txt")
txtFile = open(txtpath, "w")
txtFile.write(output)
txtFile.close()
