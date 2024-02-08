number = 10
max = 7  
current_guess = 0  

print("Enter 'q' to quit ")
print("I'm thinking of a number...")

while current_guess < max:
    guess = input("What number am I thinking of?")
    
    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input")
        continue
    
    guess = int(guess)
    current_guess += 1
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("That's too low.")
    else:
        print("That's too high.")

if current_guess >= max:
    print("You've ran out of guesses! The number was" ,{number})

