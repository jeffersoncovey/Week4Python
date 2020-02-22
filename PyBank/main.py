#import dependencies
import os
import csv

budget_csv = os.path.join("budget_data.csv")

# Assign Variables
MonthsTotal = 0
PLTotal = 0
ProfitChange = []
AverageProfit = 0
GreatestProfit = 0
GreatestMonth = ""
WorstLoss = 0
WorstMonth = ""
LastMonth = 0


with open(budget_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    for row in csvreader:
        
        # Counts the number of rows 
        MonthsTotal += 1
        # Sums the Profit/Loss Total with each iteration.
        PLTotal = PLTotal + float(row[1])

        if MonthsTotal > 1:
            # Collects an array for each of the Profit/Loss Changes for each month.
            ProfitChange.append(float(row[1]) - LastMonth)
            
            # Identifies the Greatest Profit/Month
            if ProfitChange[MonthsTotal - 2] > GreatestProfit:
                GreatestProfit = ProfitChange[MonthsTotal - 2]
                GreatestMonth = row[0]

            # Identifies the Worst Profit/Month
            if ProfitChange[MonthsTotal - 2] < WorstLoss:
                WorstLoss= ProfitChange[MonthsTotal - 2]
                WorstMonth = row[0]
            exit

        LastMonth = float(row[1])

        
    

# Prints results to terminal
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {MonthsTotal}")
print(f"Total: {int(PLTotal)}")
print("Average  Change: $" + "{0:.2f}".format((sum(ProfitChange) / len(ProfitChange))))
print(f"Greatest Increase in Profits: {GreatestMonth} (${int(GreatestProfit)})")
print(f"Greatest Increase in Profits: {WorstMonth} (${int(WorstLoss)})")

# Prints results to text file
with open("MainOutput.txt", "w") as text_file:

    print(f"Financial Analysis", file=text_file)
    print(f"----------------------------", file=text_file)
    print(f"Total Months: {MonthsTotal}", file=text_file)
    print(f"Total: {int(PLTotal)}", file=text_file)
    print("Average  Change: $" + "{0:.2f}".format((sum(ProfitChange) / len(ProfitChange))), file=text_file)
    print(f"Greatest Increase in Profits: {GreatestMonth} (${int(GreatestProfit)})", file=text_file)
    print(f"Greatest Increase in Profits: {WorstMonth} (${int(WorstLoss)})", file=text_file)

            
        

