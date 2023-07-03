import random

answer = input("Would you like to play this number guessing game? (enter yes or no) ")

if answer.lower() == "yes":
    print('Lets begin! ')
else:
    quit()

max_num = input('What would you like the highest number to be? ')

if max_num.isdigit():
    max_num = int(max_num)
    if max_num <= 0:
        print('Please enter a number larger than 0')
        quit()
else:
    print('Please enter a number next time')
    quit()



random_number = random.randint(0, max_num)
guesses_made = 0


while True:
    guesses_made +=1
    guess = input('Guess the number  ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please enter a number next time')
        continue

    if guess == random_number:
        print('You got it correct! ')
        break
    elif guess > random_number:
        print('Hint: try guessing lower ')
    else:
        print('Hint: try guessing abit higher ')

print('You got it in ',guesses_made, ('guesses'))

