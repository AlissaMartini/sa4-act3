number = 10
print("Enter 'q' to quit")
print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? ")

    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input")
        continue
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("That's too low.")
    else:
        print("That's too high")