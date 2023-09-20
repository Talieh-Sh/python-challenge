#PyBank 
# Importing Modules
import os
import csv

#Csv path to get csv
pybank_csv=os.path.join("Resources","budget_data.csv")

#Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    # Calculating the total number of months and Total included in the dataset
    #Initial variables
    Total_Months=0
    Total=0
    previous_amount=0
    greatest_increase_amount=0
    greatest_increase_month=[]
    greatest_decrease_amount=0
    greatest_decrease_month=[]
    
    #Iterate over each row in csv
    for row in csv_reader:
        if row[0]!="":
            #Calculating greatest inctease and decrease
            if int(row[1])-previous_amount>greatest_increase_amount:
                greatest_increase_amount=int(row[1])-previous_amount
                previous_amount=int(row[1])
                greatest_increase_month=str(row[0])
            if int(row[1])-previous_amount<greatest_decrease_amount:
                greatest_decrease_amount=int(row[1])-previous_amount
                previous_amount=int(row[1])
                greatest_decrease_month=str(row[0])
            previous_amount=int(row[1])
            Total_Months+=1
            Total+=int(row[1])

#Calculating Average Change 
with open(pybank_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    next(csv_reader)    
    #Converting the csv_reader to a list of lists to get access to the first and last row by indexing
    csv_list=list(csv_reader)
    last_month=len(csv_list)-1
    first_month_profit=int(csv_list[0][1])
    last_month_profit=int(csv_list[last_month][1])
    if Total_Months>0:
        average_change=round((last_month_profit-first_month_profit)/(Total_Months-1),2)

    else:
        average_change=0



    #Printing the results
    print("Financial Analysis")
    print("----------------------------")
    print("Total Month: "+ str(Total_Months))
    print("Total : $"+ str(Total))
    print("Average change: ",str(average_change))
    print("Greates increase in profit :"+str(greatest_increase_month)+"($"+str(greatest_increase_amount)+")")
    print("Greates increase in profit :"+str(greatest_decrease_month)+"($"+str(greatest_decrease_amount)+")")







