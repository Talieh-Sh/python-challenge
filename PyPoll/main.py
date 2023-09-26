#PyPoll
#Importing Modules
import os
import csv

#CSV path to get csv
pypoll_csv=os.path.join("Resources","election_data.csv")

     
#open and read the csv
with open (pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader) #Skipp the header

    #Initial variables
    total_votes=0
    candidate_name_list=[]
    candidate_vote_list=[]

    #Iterate over each row in csv
    for row in csv_reader:
        if row[0] != "":
            total_votes += 1
            candidate_name = row[2]
            #Check if the candidate name is in candidate_name_list
            if candidate_name not in candidate_name_list:
                candidate_name_list.append(candidate_name) #Add candidate name to the list 
                candidate_vote_list.append(1)#Initialize their vote count to 1
            #If the candidate is already in list increment the vote of that candidate
            else : candidate_vote_list[candidate_name_list.index(candidate_name)] += 1 

    #Printing the results
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
   
    
    for i in range(len(candidate_name_list)):
        candidate_vote_percentage=(candidate_vote_list[i]/total_votes)*100
        print(f"{candidate_name_list[i]}: {candidate_vote_percentage:0.3f}% ({candidate_vote_list[i]})")

    print("-------------------------")
    max_vote=max(candidate_vote_list)
    winner=candidate_name_list[candidate_vote_list.index(max_vote)]
    print(f"Winner: {winner}")
    print("-------------------------")

#Define the output path
output_file=os.path.join("analysis","pypol_results.txt")
#Save the results to a text file in the analysis folder

with open(output_file,"w") as output:
    output.write("Election Results\n")
    output.write("-------------------------\n")
    for i in range(len(candidate_name_list)):
        candidate_vote_percentage=(candidate_vote_list[i]/total_votes)*100
        output.write(f"{candidate_name_list[i]}: {candidate_vote_percentage:0.3f}% ({candidate_vote_list[i]})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write("-------------------------\n")
# Print a message indicating that the results have been saved
print("Results have been saved to " + output_file)  




