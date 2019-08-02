import random;

random_number = random.randrange(1,6)
guess = input("Guess a number between 1 and 6: ")
while guess != random_number:
    if guess > random_number:
        print("too big, try again")
        guess = input("Guess a number between 1 and 6: ")
    if guess < random_number:
        print("too small, try again")
        guess = input("Guess a number between 1 and 6: ")
    else:
        print("well done")
        break
