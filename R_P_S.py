import random

def compchoice():
    choices=["rock","paper","scissors"]
    return random.choice(choices) 


def user_choice():
    user=input("Enter rock,paper,scissors (or 'q' to quit ):" ).lower()
    while user not in ["rock","paper","scissors",'q']:
        user=input("Invalid choice.Enter rock,paper,scissors:")
        return user

    
def winner(user,compchoice):
    if(user==compchoice):
        return "it's a tie!!"
    elif (user == "rock" and compchoice =="scissors") or \
        (user == "paper" and compchoice =="rock") or \
            (user == "scissors" and compchoice == "paper" ):
                return "YOU WIN!!!"
            
    else:
        return "YOU LOSE :("


def game():
    while True:
        userch = user_choice()
        if userch == 'q':
            break
        compch = compchoice()
        print(f"\nYOU CHOSE{userch},computer choice{compch}")
        result = winner(userch,compch)
        print(result)

        
game()
         