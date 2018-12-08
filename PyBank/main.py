import os
import csv

budget_csv = os.path.join("..", "budget_data.csv")
#print(budget_csv)

countMonths=0
total = 0
total_change = 0

with open(budget_csv, newline="") as csvfile:

    #reads the file into a list
    csvreader = csv.reader(csvfile, delimiter=',')

    #skips the header
    next(csvfile, None)
    
    #iterate through the rows
    for row in csvreader:
        
        countMonths = countMonths + 1
        total = total + int(row[1])
        
        #for the first row, set the amount to variable last amount
        if countMonths == 1:
            last_amount = int(row[1])

        #we want to skip calculating the change for the first iteration, otherwise
        if countMonths != 1:
            #calculate change from last amount to current amount
            change = last_amount - int(row[1])
            #add the delta to the a total delta variable
            total_change = total_change + change
            #reset last amount to the current value
            last_amount = int(row[1])
          #  last_change = change

           # if change 

#calculate the total changes divided by the number of months
change_mean = total_change / countMonths

print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(countMonths ))
print("Total: " + str(total))
print("Average Change: " + str(change_mean))

