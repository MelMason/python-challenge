import os
import csv

budget_data = os.path.join("Resources/budget_data.csv")

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
        template="{:,.2f}"
        output_months=template.format(column_sum)
        output_inc = template.format(greatest_increase)
        output_dec = template.format(greatest_decrease)

    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months:  {total_months}")
    print("Total: $",output_months)
    print("Average Change:", (round(average, 2)))
    print(f"Greatest Increase in Profits:", (date_increase), "  $",(output_inc))
    print(f"Greatest Decrease in Profits:", (date_decrease), "  $",(output_dec))

results = os.path.join("final_results.txt")
output= ("Financial Analysis" + "\n" + "-------------------------------"+ "\n" + "Total Months: " + (str(total_months)) +"\n" +  "Total: $" + (str(output_months)) + "\n" +"Average Change: " + (str(round(average, 2))) + "\n"  +"Greatest Increase in Profits: "  +(str(date_increase)) + "  $" + (str(output_inc)) + "\n"  +"Greatest Decrease in Profits: " + (str(date_decrease)) +"  $" + (str(output_dec)))
with open(results, "w") as datafile:
    datafile.write(output)
