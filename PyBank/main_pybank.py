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

        if profit_loss != 0:
            change = int(row[1]) - profit_loss
            
            if change > greatest_increase :
                greatest_increase = change
                greatest_inc_month = row[0]
            
            if change < greatest_loss :
                greatest_loss = change
                greatest_loss_month = row[0]

            changes.append(change)
        
        if row[0] != month :
            month = row[0]
            total_months += 1
        
        profit_loss = int(row[1])
        total_p_l += profit_loss
        
    average_change = round(statistics.mean(changes), 2)  
    
    print ("Financial Analysis\n----------------------------")
    print(f"Total Months: {total_months}")
    print (f"Total: {total_p_l}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in profits: {greatest_inc_month} (${round(greatest_increase, 2)})" )
    print(f"Greatest Decrease in Profits: {greatest_loss_month} (${round(greatest_loss, 2)})" )
        #print (row)
        # Add title
        #title.append(row[1])

        # Add price
        #price.append(row[4])

        # Add number of subscribers
        #subscribers.append(row[5])


# Zip lists together
##cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
#output_file = os.path.join("web_final.csv")

#  Open the output file
#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)

    # Write the header row
    #writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     #"Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    #writer.writerows(cleaned_csv)
