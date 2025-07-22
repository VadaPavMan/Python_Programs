import random

number = random.randint(0, 100)
print("Guess The Random Number From 0 To 100.")
x = int(input("Enter Your Guessed Number: "))
tries = 1
while True:
    if(x < number-10):
        x = int(input("Guess A Greater Number: "))
    elif(x < number): 
        x = int(input("Almost Close, Guess A Greater Number: "))
    elif(x > number+10):
        x = int(input("Guess A Lesser Number: "))
    elif(x > number): 
        x = int(input("Almost Close, Guess A Lesser Number: "))
    else:
        print(f"You Guessed It Right. Number: {x} ,Tries: {tries}")
        break
    tries+=1