
#print("CTI-110")
#print("P4HW1 - Score list")
#print("Christina Gay")
#print("04/06/2023")
#print()



scores_list = []


total_scores = int(input("How many scores you want to enter? "))
print()


num_score = 0


while True:
    
    while num_score < total_scores:
        scores = float(input('Enter score #{}: '.format(num_score+1)))
        
        
        while True:
            if scores < 0 or scores > 100:
                print()
                print("INVALID Score entered!!!!\nScore should be between 0 and 100")
                scores = float(input('Enter score #{} again: '.format(num_score+1)))
            
                
            else:
                scores_list.append(scores) 
                break
        num_score+=1
        
    
    if num_score == total_scores:
        break
    
min_score = min(scores_list)

scores_list.remove(min(scores_list))

average = sum(scores_list) / len(scores_list)


if average > 90 and average <= 100:
    grade='A'
else:
    if average > 80 and average <= 90:
        grade='B'
    else:
        if average > 70 and average <= 80:
            grade='C'
        else:
            if average > 60 and average <= 80:
                grade='D'
            else:
                if average > 50 and average <= 60:
                    grade='B'
                else:
                        grade='F'

print()
print()

print("------------Results-----------------")
print("Lowest Score  :",min_score)
print("Modified List :",scores_list)
print("Scores Average:",average)
print("Grade         :",grade)
print("--------------------------------------")
