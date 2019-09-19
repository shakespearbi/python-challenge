#This is main.py in PyPoll
import os
import csv

#creating path
election_csv_path = os.path.join("Resources", "election_data.csv")

#set number of votes cast to 0
tot_votes = 0
#set popular vote to 0
max_vote = 0
#default for winner
winner = ""

# Initialize empty dictionaries
election_dict = {}


with open(election_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #skip header
    next(csv_reader,None)
    
    for row in csv_reader:
        #assign candidate name
        cand = row[2]
        #increment votes cast
        tot_votes += 1
        #checks to see if candidate name is a key in dictionary
        if cand in election_dict.keys():
            # increment vote count for candidate
            election_dict[cand] += 1
        else:
            # set voter count to 1
            election_dict[cand] = 1
    print("Election Results")
    print("-"*30)
    print(f'Total Votes: {tot_votes}')
    print("-"*30)
    for k,v in election_dict.items():
        print(f'{k}: {round(v*100/tot_votes,3)}% ({v})')
        #Find winner
        if max_vote < v:
            max_vote = v 
            winner = k     
    print("-"*30)
    print(f'Winner: {winner}')
    print("-"*30)


