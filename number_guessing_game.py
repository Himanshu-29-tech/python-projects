#generate a random number
#loop
    #Ask the user to make a guess
    # if not a vakid nuber
    #print an error
    # if number < guess
    #print too low
    # if number > guess
    # print too high
    # Else
    # print well done


import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break   # stop the loop after correct guess

    except ValueError:
        print("Please enter a valid number.")





