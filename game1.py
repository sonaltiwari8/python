import random
#till choice of the user != exit , till user choice == play again 
round = 0 
score = 0
user_choice= "p"
while user_choice == "p":
    round += 1  
    number = random.randint(0 , 20)
   
    chances_left = 10


    while chances_left >0:
        number_user = int(input("enter any number between 0 to 20   :"))
        if number_user >20 or number_user<0:
            print("you cant enter number greater than 20 or less than 1")
        elif number == number_user:
            print("you won ")
            if chances_left > 6:
                score +=10 
            elif chances_left >2:
                score+= 5
            break
        elif number_user > number:
            print("entered number is greater than the actual number")
        elif number_user < number:
            print("entered number is less than the actual number")
                
        chances_left -=1
        print(f"chances left = {chances_left}")
    if chances_left ==0 :
        score-=5
    user_choice= input("enter your choice : p to play again or e to exit  :")
print(f"game is over:   round : {round} and score : {score} " )    

# score(comp and user) , round 10, winner as per score ,

import random

round = 0
score = 0
chances_left = 10





while chances_left > 0:
    computer_choice= random.choice(["stone", "paper", "scissor"])
    print(computer_choice)
    user_choice = input("enter your choice to play \n1.stone \n2. paper \n3. scissors and \n4.e to exit the game \n5.p to play again    :")
    winner = None
    if user_choice == computer_choice:
        print("there is a tie ")
    elif user_choice == "stone":
        if computer_choice == "paper":
            winner = "computer"   
        else :
            winner = "user"
    elif user_choice == "paper":
        if computer_choice == "stone":
            winner = "user"            
        else:
            winner = "computer"      
    elif user_choice == "scissor":
        if computer_choice == "paper":
            winner = "user"
        else:
            winner = "computer"
             
    if user_choice == "e":
        print(f"game is over :chances left - {chances_left} your score is {score}")
        break
    # if user_choice == "p":
    # round+= 1
    chances_left -= 1


import random

score_user = 0
score_computer = 0
chances_left = 3

print("enter your choice to play \n1.stone \n2. paper \n3. scissors and \n4.e to exit the game \n5.p to play again    :")
while chances_left > 0:
    computer_choice= random.choice(["stone", "paper", "scissor"])
    user_choice = input("enter your choice :")
    winner = None
    if user_choice == computer_choice:
        print("there is a tie ")
    elif user_choice == "stone":
        winner = "computer" if computer_choice == "paper" else "user"  #ternary operator
    elif user_choice == "paper":
        winner = "user"if computer_choice == "stone" else "computer"         
    elif user_choice == "scissor":
       winner= "user" if computer_choice == "paper" else "computer"    
    # if user_choice == "p":
    # round+= 1
    chances_left -= 1
    if winner == "user":
        score_user +=1
    if winner == "computer":
       score_computer += 1 
    print(f"winner is  : {winner} 😊😊 user score is {score_user} and computer score is {score_computer}" )

if score_user > score_computer:
    print("user wins the game")
elif score_user < score_computer: 
    print("computer wins ")
else: 
    print("there is a tie")
   
    
    
    

          



