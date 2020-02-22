# Import dependencies
import os
import csv

election_data = os.path.join("election_data.csv")

# Assign Variables
TotalVotes = 0
Candidates = {}
Candidate = ""
WinnerVotes = 0
WinnerName = ""

with open(election_data, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    # Calculates Total Votes, Appends Unique Name to a dictionary, counts vote for each candidate
    for row in csvreader:
        TotalVotes += 1
        if row[2] not in Candidates:
            Candidates.update([(row[2], 0)])
        if row[2] in Candidates:
            Candidate = row[2]
            Candidates[Candidate] += 1

# Identifies Number of canidates
NumberCandidates = len(Candidates)


# Prints results to terminal, iterates through the dictionary created above to generate list of canidates, as well as their % and # of votes.
print("Election Results")
print("-------------------------")
print(f"Total Votes: {TotalVotes}")
print("-------------------------")
for row in range(NumberCandidates):
    print(f"{list(Candidates.keys())[row]}: {int((Candidates[list(Candidates.keys())[row]] / TotalVotes) * 100)}% ({(Candidates[list(Candidates.keys())[row]])})")

print("-------------------------")
for row in range(NumberCandidates):
    if int(Candidates[list(Candidates.keys())[row]]) > WinnerVotes:
        WinnerVotes = int(Candidates[list(Candidates.keys())[row]])
        WinnerName = list(Candidates.keys())[row]

print(f"Winner: {WinnerName}")    
print("-------------------------")

# Prints same results to text file.
with open("MainOutput.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {TotalVotes}", file=text_file)
    print("-------------------------", file=text_file)
    for row in range(NumberCandidates):
        print(f"{list(Candidates.keys())[row]}: {int((Candidates[list(Candidates.keys())[row]] / TotalVotes) * 100)}% ({(Candidates[list(Candidates.keys())[row]])})", file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {WinnerName}", file=text_file)    
    print("-------------------------", file=text_file)