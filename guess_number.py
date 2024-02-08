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
        print("Invalid input. Please enter a number or 'q' to quit.")
        continue
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print("Sorry! That's incorrect. Try again.")
