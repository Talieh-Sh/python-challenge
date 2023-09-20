#PyPoll
import os
import csv
pypoll_csv=os.path.join("Resources","election_data.csv")

     
#open and read the csv
with open (pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    total_votes=0
    candidate_name_list=[]
    candidate_vote_list=[]

    for row in csv_reader:
        if row[0] != "":
            total_votes += 1
            candidate_name = row[2]
            if candidate_name not in candidate_name_list:
                candidate_name_list.append(candidate_name)
                candidate_vote_list.append(1)

            else : candidate_vote_list[candidate_name_list.index(candidate_name)] += 1


    print("Total Votes: " + str(total_votes))
    print("candidate_name_list= " + ",".join(candidate_name_list))
    
    for i in range(len(candidate_name_list)):
        candidate_vote_percentage=(candidate_vote_list[i]/total_votes)*100
        print(f"{candidate_name_list[i]}: {candidate_vote_list[i]} votes ({candidate_vote_percentage:0.2f}%)")

    
    max_vote=max(candidate_vote_list)
    winner=candidate_name_list[candidate_vote_list.index(max_vote)]
    print(f"Winner: {winner}")

