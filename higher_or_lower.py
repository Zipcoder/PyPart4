from random import randrange

def user_value():
    value = input('Please enter a number between 0 and 10\n')
    return value

def randomValue():
    return randrange(1, 10)

def isEqual():

    a = randomValue() #random generated number
    b = int(user_value())    #user guess3

    print("Random # generated: " + str(a))
    print("you guessed: " + str(b))

    while a != b:
        if a > b:
            print('You guessed too low')
            b = int(user_value())
        elif a < b:
            print('You guessed too high!')
            b = int(user_value())
        
    else:
        print('You guessed right!') 

isEqual()