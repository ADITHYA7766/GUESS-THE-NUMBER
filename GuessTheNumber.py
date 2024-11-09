import random
Generated_code = random.randrange(1,1000)

for chance in range(1,15):
    GIVEN_NUMBER = int(input("Guess a number between 1 and 1000:- "))


    if GIVEN_NUMBER == Generated_code:
        print("you won it in", chance)
        break
    elif GIVEN_NUMBER > Generated_code:
        print("your number is higher, you still have",15 - int(chance))
    else:
        print("your number is lower ,you still have",15- int(chance))

if chance < 15:
    print("You guessed the ans in ", chance,"the secret number is ",Generated_code)

if chance >15:
    print("you fucking piece of shit the the secret number is",Generated_code)