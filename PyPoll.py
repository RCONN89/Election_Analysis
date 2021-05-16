import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

        # Read the file object with the reader function
        file_reader = csv.reader(election_data)
        # Read the header row.
        headers = next(file_reader)
        # Print each row in the CSV file.
        for row in file_reader:
            total_votes += 1 
        # Print the candidate name from each row.
            candidate_name = row[2]
        # If candidate doesn't match any existing candidate, add them.
            if candidate_name not in candidate_options:
                # Add it to the list of candidates.
        # Add the candidate name to the cadidate list.
                candidate_options.append(candidate_name)
                # Begin tracking that candidate's vote count.
                candidate_votes[candidate_name] = 0
                # Add a vote that candidate's count.
            candidate_votes[candidate_name] += 1
        
    # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
        
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate throught the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}\n")
        # 4. Print the candidate name and the percentage of votes.
        print(candidate_results)
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true set winning = votes and winning_percent = voting_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
# Save the winning results to the text file
    txt_file.write(winning_candidate_summary)
    # print(winning_candidate_summary)
    # The data we need to retrieve.
    # 1. The total number of votes cast.
    # 2. A complete list of candidates that received votes.
    # 3. The percentage of votes each candidate won.
    # 4. The total number of votes each candidate won.
    # 5. The winner of the election based on popular vote.