# # * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os
import csv

poll_data = os.path.join("election_data.csv")

VoterID = []
County = []
Candidate = []

with open(poll_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(csvreader)

    for row in csvreader:
        VoterID.append(int(row[0]))
        County.append(str(row[1]))
        Candidate.append(str(row[2]))
    
# #   * The total number of votes cast
    
        total_votes = str(len(VoterID))

# #   * A complete list of candidates who received votes
# candidates = ["Khan", "Correy", "Li", "O'Tooley"]
# print(candidates)

Khan_votes = []
Correy_votes = []
Li_votes = []
OTooley_votes = []

# #   * The total number of votes each candidate won

for names in Candidate:
    if names == "Khan":
        Khan_votes.append(names) 
    elif names == "Correy":
        Correy_votes.append(names)
    elif names == "Li":
        Li_votes.append(names) 
    else:
        OTooley_votes.append(names)
        
 

# # #   * The percentage of votes each candidate won
    percent_khan_votes = ((int(len(Khan_votes)))/(int(total_votes)))*100
    percent_correy = (((float(len(Correy_votes)))/(float(total_votes))))*100
    percent_li = ((float(len(Li_votes)))/(float(total_votes)))*100
    percent_otooley = ((float(len(OTooley_votes)))/(float(total_votes)))*100


# # * As an example, your analysis should look similar to the one below:
#   ```text


print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")  
print(f"Khan: {round(percent_khan_votes)}.000% ({str(len(Khan_votes))})")   
print(f"Correy: {round(percent_correy)}.000% ({str(len(Correy_votes))})") 
print(f"Khan: {round(percent_li)}.000% ({str(len(Li_votes))})") 
print(f"Khan: {round(percent_otooley)}.000% ({str(len(OTooley_votes))})") 
print("----------------------------")  

# #   * The winner of the election based on popular vote.

a = (len(Correy_votes))
b = (len(Li_votes))
c = (len(OTooley_votes))
d = (len(Khan_votes))

if (a > b) and (a > c) and (a > d):
    print("Winner: Correy")
elif (b > a) and (b > c) and (b > d):
    print("Winner: Li")
elif (c > a) and (c > b) and (c > d):
    print("Winner: O'Tooley")
else:
    print("Winner: Khan")

#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export 