import random

no=random.randint(0,20)
chances=5
used=0

print("Number guessing game :-")

while chances>0:
    used+=1
    i=int(input("Guess a number between 0-20: "))

    if i==no:       
        print("You won the game in ",str(used)," chances !")
        break
    elif i<no:
        print("Sorry, guessed number is lessar than winning number.")
    elif i>no:
        print("Sorry, guessed number is greater that winning number.")
    
    chances-=1

if chances==0:
    print()
    print()
    print("You lose !")
    print("The number was, ",no)