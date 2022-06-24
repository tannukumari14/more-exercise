from random import randint
def win():
    print("you win")
def lose():
    print("you lose")
while True:
    choice=input("what do you pick(rock,paper,scissors)")
    choice.strip()
    random_move=randint(0,2)
    moves=["rock","paper","scissors"]
    computer=moves[random_move]
    if choice==computer:
        print("draw")
    elif  choice== 'rock' and computer== 'scissors':
        win()
    elif  choice== 'paper' and computer== 'scissors':
        lose()
    elif  choice== 'scissors' and computer == 'paper':
        win()
    elif choice== 'scissors' and computer == 'rock':
        lose()
    elif choice== 'paper' and computer == 'rock':
        win()
    elif choice ==  computer:
        lose()
    again=input("do you want to play again?(y or n)").strip()
    if "again"=="n" and "again"=="y":
        break