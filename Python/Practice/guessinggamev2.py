def game():
    while True:
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
                break
            elif guessnum > rannum:
                print("THE GUESS IS TOO HIGH")
            else:
                print("THE GUESS IS TOO LOW")

        if chance == 0:
            print(f"GAME OVER! The correct number was {rannum}")

        again = input("DO YOU WANNA TRY AGAIN (Y/N): ")
        if again.upper() != "Y":
            print("THANKS FOR PLAYING GUESSING THE NUMBER, BYE")
            border()
            break
