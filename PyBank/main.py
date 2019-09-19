#This is main.py in PyBank
import os
import csv

budget_csv_path = os.path.join("Resources", "budget_data.csv")

#default for greatest increase
max_diff = 0
#default value for greatest decrease
min_diff = 0
#net profit
net_total = 0 
#net change 
net_diff = 0

#empty list of dates
date = [] 
#empty list of profit/loss
revenue = []   

with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #skips header
    next(csv_reader,None)

    for row in csv_reader:
        #define date
        day = row[0]
        #add date to array
        date.append(day)

        #define budget
        budget = float(row[1])
        #add budget to list
        revenue.append(budget)
        #compute net profit
        net_total += budget

    num_month = len(date)
    print(num_month)
    print("Financial Analysis")
    print("-"*30)
    print(f'Total Months: {num_month}')
    print(f'Total: $ {net_total}')

    #Compute change over a period
    for i in range(1,num_month):

        next_rev = revenue[i]
        curr_rev = revenue[i-1]
        diff = next_rev-curr_rev 
        net_diff = net_diff + diff

    #Find greatest increase
    for i in range(1,num_month):
        next_rev = revenue[i]
        curr_rev = revenue[i-1]
        diff = next_rev-curr_rev 
        if max_diff < diff:
            max_diff = diff
            #assign date
            date1= date[i]

    #Find greatest decrease
    for i in range(1,num_month):
        next_rev = revenue[i]
        curr_rev = revenue[i-1]
        diff = next_rev-curr_rev 
        if min_diff > diff:
            min_diff = diff 
            #assign date 
            date2 = date[i]        
    
    #Average change
    print(f'Average Change: ${net_diff/(num_month-1)}')
    #Greatest increase in profit
    print(f'Greatest Increase in Profits:{date1} (${max_diff})')
    #Greatest decrease in profit
    print(f'Greatest Decrease in Profits:{date2} (${min_diff})')


         

        
