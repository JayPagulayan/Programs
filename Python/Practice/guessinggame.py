import random

def randomnumber(lowbound, upbound):
    return random.randint(lowbound, upbound)

def border():
    print("=" * 15 + " GUESS THE NUMBER " + "=" * 15)


border()
print("WELCOME TO OUR NUMBER GUESSING GAME.")
print("YOU ONLY HAVE 7 CHANCES, SO DON'T WASTE THEM\n")

def tryagain():
    again=input("DO YOU WANNA TRY AGAIN (Y/N) :")
    if again.upper() == "N":
        print("THANKS FOR PLAYING GUESSING THE NUMBER, BYE")
        border()
    elif again.upper() == "Y":
        game()

def game():
    border()

    upbound = int(input("ENTER UPPER BOUND: "))
    lowbound = int(input("ENTER LOWER BOUND: "))

    rannum = randomnumber(lowbound, upbound)

    chance = 7
    gstrike = 0

    while chance > 0:
        print(f"REMAINING CHANCE: {chance}")
        guessnum = int(input("ENTER YOUR GUESS: "))
        gstrike += 1
        chance -= 1

        if guessnum == rannum:
            print(f"CORRECT! You guessed the number {guessnum}")
            print(f"You guessed it in {gstrike} tries\n")
            tryagain()
        elif gstrike == 7 and guessnum != rannum:
            print(f"GAME OVER! The correct number was {rannum}")
            tryagain()
        elif rannum < guessnum:
            print("THE GUESS IS TO HIGH")
        elif rannum > guessnum:
            print("THE GUESS IS TO LOW")
game()

