import os
import csv

budget_data = os.path.join("budget_data.csv")

list_months = []
list_profit_loss = []
column_sum = 0 
increase_decrease = []
x = 0
final_results = []

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(csvreader)
    # for row in csvreader:
    #     print(row)
#-----------------------------------------------------------
    for row in csvreader:
        list_months.append(row[0])
        list_profit_loss.append(int(row[1]))
    
#The total number of months included in the dataset 

        total_months = str(len(list_months))
        
# # #The net total amount of "Profit/Losses" over the entire period  
        
        profit_loss = int(row[1])
        column_sum += (profit_loss)
        
# #----------------------------------------------------------
    for x in range(1, len(list_profit_loss)):
        increase_decrease.append((int(list_profit_loss[x])) - (int(list_profit_loss[x-1])))

# # # #The average of the changes in "Profit/Losses" over the entire period
        average =  (sum(increase_decrease)/len(increase_decrease))
        
# # #The greatest increase in profits (date and amount) over the entire period
    
        greatest_increase = (max(increase_decrease))
        date_increase = str(list_months[increase_decrease.index(max(increase_decrease))+1])
        
# # # #The greatest decrease in losses (date and amount) over the entire period

        greatest_decrease = (min(increase_decrease))
        date_decrease = str(list_months[increase_decrease.index(min(increase_decrease))+1])
#print the analysis to the terminal and export a text file with the results.
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months:  {total_months}")
    print(f"Total: $ {column_sum}")
    print(f"Average Change: {str(average)}")
    print(f"Greatest Increase in Profits: {date_increase} ({(str(greatest_increase))})")
    print(f"Greatest Decrease in Profits: {date_decrease} ({(str(greatest_decrease))})")
    
# results_csv = zip(total_months, column_sum, average, greatest_increase, greatest_decrease)
# print(results_csv)
results = os.path.join("final_results.txt")
output= ("Financial Analysis" + "\n" + "-------------------------------" + "\n" +  ("Total: $" + column_sum) + "\n" + ("Average Change:" + (str(average))) + "\n" + ("Greatest Increase in Profits:" + date_increase + (str(greatest_increase))) + "\n" + ("Greatest Decrease in Profits:" + date_decrease + (str(greatest_decrease)))
with open(results, "w") as datafile:
    datafile.write(output)

# Error message
#   File "main.py", line 62
#     with open(results, "w") as datafile:
#        ^
# SyntaxError: invalid syntax