import os
import csv

pypoll_csv = os.path.join("Resources", "Lessons_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")

# Set up objects and variables for the data
total_votes_cast = 0
candidates = {}

# with open(pypoll_csv, newline='', encoding='utf-8') as csvfile:
with open(pypoll_csv, newline='') as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter=",")

    # Read the header
    csv_header = next(pypoll_reader)


    # Loop through the data
    for row in pypoll_reader:

        # If the loop encounters a new candidate, the candidate is added to dictionary with a vote count of 1        
        if row[2] not in candidates:
            candidates[row[2]] = [1]
        
        # If candidate is already in the dictionary, the candidate's vote count is incremented by 1
        else:
            candidates[row[2]][0] += 1
        
        # Total votes cast counter
        total_votes_cast += 1
    
    # This next block calculates the percentage of total vote for each candidate. This might be overcomplicating it some. 
    # But I did it this way to be able to sort and the list of candidates by percentage later and print in that order. 
   
    for key, val in candidates.items():
        vote_pct = (val[0] / total_votes_cast)
        vote_pct = vote_pct
        val.append(vote_pct)
    
    # Then sort the candidates by percentage of total vote
    candidates_sorted = dict(sorted(candidates.items(), key=lambda item: item[1], reverse=True))
    
    # Pull out the winner from the sorted dictionary in order to print later
    winner = list(candidates_sorted.keys())[0]
    
    #Set up the output file so that I can print to it
    output_file = open(os.path.join("Analysis", "analysis_pypoll.txt"), "w", newline="")

    # Finally, it starts printing. For simplicity, I'm printing to terminal and file in parallel:
    print ("Election Results\n-------------------------")
    output_file.write("Election Results\n-------------------------\n")

    print(f"Total Votes: {total_votes_cast}")
    output_file.write(f"Total Votes: {total_votes_cast}\n")
    
    print("-------------------------")
    output_file.write("-------------------------\n")

    # A for loop to print the data candidate by candidate. From the dictionary, it's pulling out the key (the candidate),
    # and both values (total vote count and % count). Remember that the dictionary is already sorted
    for key, val in candidates_sorted.items():
        line = (f"{key}: {round(val[1]*100, 3)}00% ({val[0]})")
        print(line)
        output_file.write(f"{line}\n")
    
    #print winner
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------")
    