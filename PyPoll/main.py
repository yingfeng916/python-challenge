import os
import csv

total_votes = 0
candidate_list = []
candidate_votes = int
candidate_stats = dict()
previous_votes = 0
winner = str

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    data_list = list(csvreader)

    for line in data_list:
        total_votes += 1
        if line[2] not in candidate_list:
            candidate_list.append(line[2])
    
    txtpath = os.path.join("Election Analysis.txt")
    txtFile = open(txtpath, "w")
    print("Election Results", file=txtFile)
    print("------------------------", file=txtFile)
    print ("Total Votes: " + str(total_votes), file=txtFile)
    print("------------------------", file=txtFile)
    
    print("Election Results")
    print("------------------------")
    print ("Total Votes: " + str(total_votes))
    print("------------------------")
    
    for candidate in candidate_list:
        candidate_stats[candidate] = 0
        for votes in data_list:
            if votes[2] == candidate:
                candidate_stats[candidate] += 1
        if previous_votes == 0:
            previous_votes = int(candidate_stats[candidate])
            winner = candidate
        elif int(candidate_stats[candidate]) > previous_votes:
            previous_votes = int(candidate_stats[candidate])
            winner = candidate
    
        print(candidate + ": " + str(round((candidate_stats[candidate]/total_votes)*100, 2)) + "% " + "(" + str(candidate_stats[candidate]) + ")")
        print(candidate + ": " + str(round((candidate_stats[candidate]/total_votes)*100, 2)) + "% " + "(" + str(candidate_stats[candidate]) + ")", file=txtFile)
    print("Winner: " + winner)
    print("Winner: " + winner, file=txtFile)
    txtFile.close()
    

