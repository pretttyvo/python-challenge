#PyBank

import os
import csv
import operator

# open the file
fname= "UTAUS201901DATA3/homework-instructions/03-Python/Instructions/PyBank/Resources/budget_data.csv"

# starting the indexes at zero
index = 0
total = 0
count1 = 867884
increase = 0
decrease = 0

# list for changes
delta = []

# print the file
with open(fname, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print header
    header = next(csvreader)
    # add index column to header
    header.insert(0,'Index')
    # loop over each row
    for row in csvreader:
        # add numbering to index
        index = index + 1
        # add index numbering into the column
        row.insert(0, index)
        # calculate the net sum
        total = total + float(row[2])
        count2 = float(row[2])
        change = count2 - count1
        delta.append(change)
        count1 = float(row[2])
        if change > increase:
            increase = change
            inc_date = row[1]
        elif change < decrease:
            decrease = change
            dec_date = row[1]
    # create variable for months
    months = index
    # add up the total
    net = total
    # create variable for net total
    changes = sum(delta)
    # calculate the average
    average = round((changes / (months-1)),2)
# print title
print(f'Financial Analysis')
print(f'-------------------------------------------')
# print total months
print(f'Total months: {months}')
# print total net
print(f'Total: ${net}')
# print average
print(f'Average change: ${average}')
# print the max increase
print(f'Greatest Increase in Profits: {inc_date} ({increase})')
# print the max decrease
print(f'Greatest Decrease in Profits: {dec_date} ({decrease})')

# output data into a separate file

# determine file location
output = "Homework/python-challenge/pybank/Data.Output.csv"
# write into file
with open(output, 'w', newline='') as csvfile:
    # initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    # write data
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow('')
    csvwriter.writerow(['Total months:', months])
    csvwriter.writerow(['Total:', net])
    csvwriter.writerow(['Average change:', average])
    csvwriter.writerow(['Greatest Increase in Profits:', inc_date, increase])
    csvwriter.writerow(['Greatest Decrease in Profits:', dec_date, decrease])

