# pypoll draft

import os
import csv
import operator

# locate file
fname = "UTAUS201901DATA3/homework-instructions/03-Python/Instructions/PyPoll/Resources/election_data.csv"

# create variables and lists

votes = 1
candidates = []
tally = []
percentage = []
vote_1 = 0
vote_2 = 0
vote_3 = 0
vote_4 = 0


#open file
with open(fname, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        
        # add an index column to determine total votes
        votes += 1
        name = row[2]
        
        # find the unique candidates
        
        if name not in candidates:
            candidates.append(name)
            
        # add up the number of votes per candidate
        if name == candidates[0]:
            vote_1 += 1
            percent_1 = "{0:.0%}".format(vote_1 / votes)
        elif name == candidates[1]:
            vote_2 += 1
            percent_2 = "{0:.0%}".format(vote_2 / votes)
        elif name == candidates[2]:
            vote_3 += 1
            percent_3 = "{0:.0%}".format(vote_3 / votes)
        elif name == candidates[3]:
            vote_4 += 1
            percent_4 = "{0:.0%}".format(vote_4 / votes)
    
    # add tallied votes to tally list
    tally.append(vote_1)
    tally.append(vote_2)
    tally.append(vote_3)
    tally.append(vote_4)
    
    # add percentages to the list and format in %
    percentage.append(percent_1)
    percentage.append(percent_2)
    percentage.append(percent_3)
    percentage.append(percent_4)
    
    #create variable for candidates
    candidate_1 = candidates[0]
    candidate_2 = candidates[1]
    candidate_3 = candidates[2]
    candidate_4 = candidates[3]
    
# determine the winner
win = max(percentage)
win_i = percentage.index(win)
winner = candidates[win_i]

# create zip file for all the lists
summary = zip(candidates, percentage, tally)

# print out the data
print("Election Results")
print("-------------------------")
print(f'Total Votes: {votes}')
print("-------------------------")
print(f'{candidate_1} : {percent_1} ({vote_1})')
print(f'{candidate_2} : {percent_2} ({vote_2})')
print(f'{candidate_3} : {percent_3} ({vote_3})')
print(f'{candidate_4} : {percent_4} ({vote_4})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

#--------------------------------------------------------------------

# save output file to not overwrite current file
output = "Homework/python-challenge/pypoll/output.csv"

# open output file
with open(output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    
    #add title
    writer.writerow(['Election Results'])
    writer.writerow("")
    writer.writerow(['Total Votes:', votes])
    writer.writerow("")
    # add in header
    writer.writerow(["Candidate", "Percentage", "Total Votes"])
    
    # load data
    writer.writerows(summary)
    writer.writerow("")
    writer.writerow(['Winner: ', winner])
    
    
final = "03-Python/Instructions/PyPoll/Resources/output.csv"

