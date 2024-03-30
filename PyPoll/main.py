import csv
# Needed:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# start here
# create variables
election_file_path = "PyPoll\Resources\election_data.csv"
total_votes = 0

# open the file
with open(election_file_path) as election_file:
    csv_file = csv.reader(election_file)
    next(csv_file)  # skips a row in the file ( first row =header row)
    # read a row in the file
    for row in csv_file:
        # add to total votes
        total_votes += 1


# print the results to screen
print(total_votes)
# print the results to file


# end here

# example output
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
