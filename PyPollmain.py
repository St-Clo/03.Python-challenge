import os
import csv

# Path
election_data_csv = os.path.join("Resources","election_data.csv")

# Variables
total_votes = 0 
total_candidates = 0 
vote_count = []
candidatelist = []
unique_candidate = []
vote_percentage = []
winning_candidate = ""
winning_count = 0 

# open file 
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

# Count he total number of votes
    for row in csvreader:
      total_votes = total_votes + 1
      candidatelist.append(row[2])

# Unique candidates 
    for x in set(candidatelist):
      unique_candidate.append(x)
      y = candidatelist.count(x)
      vote_count.append(y)
   
      z = (y/total_votes)*100
      vote_percentage.append(z)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
   
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_votes))
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percentage[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Note to TA: I could not figure out how to print the txt file, so i look up for this step in Google and other sources 

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
