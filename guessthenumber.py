import random

attempts_list = []

def show_score():
    if len(attempts_list) != 0:
        print("The current high score is {} attempts".format(min(attempts_list)))
    else:
        print("There is currently no high score, it's yours for the taking!")

def start_game():
    random_number = int(random.randint(1, 10))
    print("Hey There! Welcome to the game of guesses!")
    player_name = input("Enter your name: ")
    wanna_play = input("Hi {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))

    if wanna_play.lower() == "yes":
        show_score()
        attempts = 0

        while True:
            try:
                guess = input("Pick a number between 1 and 10: ")
                if int(guess) < 1 or int(guess) > 10:
                    raise ValueError("Please guess a number within the given range")
                
                attempts += 1
                guess = int(guess)

                if guess == random_number:
                    print("Congrats! You guessed it right!")
                    print("It took you {} attempts.".format(attempts))
                    attempts_list.append(attempts)
                    play_again = input("Would you like to play again? (Enter Yes/No) ")
                    if play_again.lower() == "no":
                        print("That's cool, have a nice day!")
                        break
                    else:
                        attempts = 0
                        random_number = int(random.randint(1, 10))
                        show_score()
                elif guess < random_number:
                    print("It's lower")
                elif guess > random_number:
                    print("It's higher")

            except ValueError as err:
                print("Oh no! That is not a valid value. Try again...")
                print("({})".format(err))
    else:
        print("That's cool, have a nice day!")

if __name__ == '__main__':
    start_game()
