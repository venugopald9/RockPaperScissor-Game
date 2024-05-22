import random

choice = 'y'

while choice == 'y':
    user = input("enter your choice in 'r' for rock, 'p' for paper, 's' for scissors \t".lower())
    comp = random.choice(['r','p','s'])    
    
    if user == comp:
        print(f"Your choose {user}, computer chose {comp},it\'s a tie")
    
    elif (user == 'r' and comp == 's') or (user == 's' and comp =='p') or (user == 'p' and comp == 'r'):
        print(f"Your choose {user}, computer chose {comp}, so You won the game")
    else:
        print(f"Your choose {user}, computer chose {comp},You lost the game")
    choice = input("Are you interested to pla again 'y' for yes 'n' for no \t")

        
    