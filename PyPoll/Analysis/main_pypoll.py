import os
import csv
import statistics

pypoll_csv = os.path.join("Resources", "Lessons_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")

# Set up objects and variables for the data
total_votes_cast = 0
candidates = {}

# with open(pypoll_csv, newline='', encoding='utf-8') as csvfile:
with open(pybank_csv, newline='') as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter=",")

    # Read the header
    csv_header = next(pypoll_reader)
    print(f"CSV Header: {csv_header}")

    # Loop through the data
    for row in pybank_reader:

        # This next block loops through, and scans for greatest increase and greatest loss. It also calculates
        # the change from one month to the next and records that change in a list that I will use later to 
        # calculate average change. 

        # Note that the next line below, "if profit_loss != 0:" is intended to skip these operations for the 
        # first line of data, because there can be no comparison for change. 
        
        if row[2] not in candidates:
            candidates[row[2]] = 1
        
        else:
            candidates[row[2]] += 1
        
        total_votes_cast += 1


    # With the changes in a list, calculating average is easy with statistics.mean(). Note that I imported
    # statistics at the beginning of this script with the other imports.   
    average_change = round(statistics.mean(changes), 2)  
    
    # Finally, the print statements for the report:
    print ("Election Results\n-------------------------")
    print(f"Total Votes: {total_votes_cast}")
    print("-------------------------")
    print (candidates)
    
    #for item in candidates


    # Finally, this last section is to print to a text file:

# Set variable for output file
#output_file = os.path.join("Analysis", "analysis_pybank.txt")

# Open the output file
#output_file = open(output_file, "w", newline="")

# Print statements for the text file
#output_file.write("Financial Analysis\n----------------------------\n")
#output_file.write(f"Total Months: {total_months}\n")
#output_file.write(f"Total: ${total_p_l}\n")
#output_file.write(f"Average Change: ${average_change}\n")
#output_file.write(f"Greatest Increase in profits: {greatest_inc_month} (${round(greatest_increase, 2)})\n" )
#output_file.write(f"Greatest Decrease in Profits: {greatest_loss_month} (${round(greatest_loss, 2)})" )
    
