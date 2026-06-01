secret_number = 13
guess = 0
attempts = 0

while guess != secret_number and attempts < 3:


    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess  > secret_number:
        print("Too high! Try again.")

    elif guess < secret_number:
        print("Too low! Try agan")

    else:
        print("Congratulations! You guessed the number!")
        break

if guess != secret_number:
    print("Game Over! You have used all 3 attempts. ")

    play_again = input("do you want to play again? (yes/no:) ").lower()
    
print("Thanks for playing Mind Teaser!")
    
