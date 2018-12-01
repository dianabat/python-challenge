import os
import csv

budget_csv = os.path.join("..", "python-challenge", "budget_data.csv")
print(budget_csv)

with open(budget_csv, newline="") as csvfile:

    #reads the file into a list
    csvreader = csv.reader(csvfile, delimiter=',')

    #skips the header
    next(csvfile, None)
    
    #iterate through the rows
    for row in csvreader:
        
        countMonths = row
        print(countMonths)
        #find which rows have 5 or more grams of Fiber
        #if float(row[7]) >= 5:
            #print the name of the cereal
            #print(row[0])
