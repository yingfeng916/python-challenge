import os
import csv

total_votes = 0
candidate_list = []
candidate_votes = int
candidate_stats = dict()
previous_votes = 0
winner = str
candidate_results = ""

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    data_list = list(csvreader)

    for line in data_list:
        total_votes += 1
        if line[2] not in candidate_list:
            candidate_list.append(line[2])
    

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
        
        votes_percentage = round((candidate_stats[candidate]/total_votes)*100, 2)
        votes_number = candidate_stats[candidate]
        candidate_results += (candidate + ": " + str(votes_percentage) + "% " + "(" + str(votes_number) + ")") + "\n"


output = "Election Results \n\
------------------------ \n\
Total Votes: " + str(total_votes) + "\n\
------------------------ \n\
"+ candidate_results + "Winner: " + winner

print(output)

txtpath = os.path.join("Election Analysis.txt")
txtFile = open(txtpath, "w")
txtFile.write(output)
txtFile.close()
    

