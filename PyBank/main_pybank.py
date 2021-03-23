import os
import csv
import statistics

pybank_csv = os.path.join("Resources", "Lessons_03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv")

# Set up lists and variables for the data
total_months = 0
month = 'x'
changes = []
greatest_increase = 0
greatest_loss = 0
profit_loss = 0
total_p_l = 0



# with open(pybank_csv, newline='', encoding='utf-8') as csvfile:
with open(pybank_csv, newline='') as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=",")

    # Read the header
    csv_header = next(pybank_reader)
    print(f"CSV Header: {csv_header}")

    # Loop through the data
    for row in pybank_reader:

        # This next block loops through, and scans for greatest increase and greatest loss. It also calculates
        # the change from one month to the next and records that change in a list that I will use later to 
        # calculate average change. 

        # Note that the next line below, "if profit_loss != 0:" is intended to skip these operations for the 
        # first line of data, because there can be no comparison for change. 
        if profit_loss != 0:
            change = int(row[1]) - profit_loss
            
            if change > greatest_increase :
                greatest_increase = change
                greatest_inc_month = row[0]
            
            if change < greatest_loss :
                greatest_loss = change
                greatest_loss_month = row[0]

            # Change values are appended to list here
            changes.append(change)
        
        # This is the month counter
        if row[0] != month :
            month = row[0]
            total_months += 1
        
        # This next block resets the profit_loss value, to compare with next time through the loop.
        profit_loss = int(row[1])

        # And this keeps summing the profit-losses
        total_p_l += profit_loss

    # With the changes in a list, calculating average is easy with statistics.mean(). Note that I imported
    # statistics at the beginning of this script with the other imports.   
    average_change = round(statistics.mean(changes), 2)  
    
    # Finally, the print statements for the report:
    print ("Financial Analysis\n----------------------------")
    print(f"Total Months: {total_months}")
    print (f"Total: {total_p_l}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in profits: {greatest_inc_month} (${round(greatest_increase, 2)})" )
    print(f"Greatest Decrease in Profits: {greatest_loss_month} (${round(greatest_loss, 2)})" )