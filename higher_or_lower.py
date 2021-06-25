import random

def user_number():
    number = input('Guess a number 0-10\n')
    return int(number)
    
def rand_number():
    number = random.randrange(0,11)
    return number
    
def compare_number():
    rand = rand_number()
    guess = False
    while guess == False:
        user = user_number()
        if user > rand:
            print('that was too high')
            
        elif user < rand:
            print('that was too low')
            
        elif user == rand:
            print('that was spot on')
            break
        else:
            print('error')

compare_number()