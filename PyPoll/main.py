import csv

# create variables
election_file_path = "PyPoll\Resources\election_data.csv"
total_votes = 0
candidates = []
candidate_votes = []

# open the file
with open(election_file_path) as election_file:
    csv_file = csv.reader(election_file)
    next(csv_file)  # skips a row in the file ( first row =header row)
    # read a row in the file
    for row in csv_file:
        # add to total votes
        total_votes += 1
        # "Ballot ID,County,Candidate"
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        # check to see if the candidate exists
        if candidate not in candidates:
            # add to list if they haven't been added to the list
            candidates.append(candidate)
            candidate_votes.append(1)  # add the first vote
        else:  # candidate is in list
            candidate_id = candidates.index(candidate)
            candidate_votes[candidate_id] += 1
# done reading the file

# print the results to screen
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for candidate in candidates:
    current_candidate_votes = candidate_votes[candidates.index(candidate)]
    current_vote_pct = (current_candidate_votes / total_votes) * 100
    print(
        f'{candidate}: {round(current_vote_pct,3)}% ({current_candidate_votes})')
print('-------------------------')
print(f'Winner: {candidates[candidate_votes.index(max(candidate_votes))]}')
print('-------------------------')

# print the results to file
out_file_path = "PyPoll\election_results.txt"
with open(out_file_path, 'w') as file_out:
    file_out.write('Election Results\n')
    file_out.write('-------------------------\n')
    file_out.write(f'Total Votes: {total_votes}\n')
    file_out.write('-------------------------\n')
    for candidate in candidates:
        current_candidate_votes = candidate_votes[candidates.index(candidate)]
        current_vote_pct = (current_candidate_votes / total_votes) * 100
        file_out.write(
            f'{candidate}: {round(current_vote_pct,3)}% ({current_candidate_votes})\n')
    file_out.write('-------------------------\n')
    file_out.write(
        f'Winner: {candidates[candidate_votes.index(max(candidate_votes))]}\n')
    file_out.write('-------------------------\n')
# end here
