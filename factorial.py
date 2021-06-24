def factorial(x):
    if x >= 0:
        answer = 1
        for x in range (1,x+1):
            answer = answer * x
            print(answer)
    else:
        return print('error')
    return answer

print(factorial(-3))