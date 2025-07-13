import random
#initialising score's as 0
user_score=0
computer_score=0
option=["rock","paper","scissor"]
print("=====Welcome to rock, paper, scissor game=====")
while True:
    user_choice=input("\n Please choose - rock,paper,scissor:").lower()
    if user_choice in option:
        computer_choice=random.choice(option)
        print("computer choose's:", computer_choice)
        if user_choice==computer_choice:
            print("Tie!!")
        elif(user_choice=="rock" and computer_choice=="scissor") or (user_choice=="scissor" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="rock"):
            print("You win!!")
            user_score+=1
        else:
            print("computer wins")
            computer_score+=1
            print("----------score----------")
        print("You -" , user_score ,"|" ,"computer score -", computer_score)
         
    key = input("\nDo you want to play again?--Say yes if you want or no if not.").lower()
    if key=="no":
        print("--------------------Game over--------------------")
        break
    elif key=="yes":
        continue
    else:
        print("Invalid choice.Please try again.")
            
            
        
        
    
