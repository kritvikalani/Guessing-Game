import random;

number = random.randint(1,9)
chance = 0

while chance < 5:
    guess = int(input("Guess the number- "))

    if (guess == number):
        print("Congratulations!")
        break;

    elif (guess < number):
        print("Guess a bigger number than ", guess)
        
    else :
        print("Guess a smalled number than ", guess)

    chance = chance + 1

if not chance < 5:
    print("You Lose! The number is ", number)