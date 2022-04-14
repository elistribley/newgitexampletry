import random
import time
print("Hi! this is a guessing game. I am going to pick a number between 1 and 50")
time.sleep(4)
print("Please guess a number: ")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,50)

guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
     guess = int(input("Wrong. You need to guess higher! What is your guess?: "))
    else:
     guess = int(input("Wrong. You need to guess lower! What is your guess?: "))

print(f"Congrats! the right answer was {correct_number} and you guessed {guess_count} times")