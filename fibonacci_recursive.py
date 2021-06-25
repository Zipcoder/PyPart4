def fibonacci(n):
    if n < 0 or n > 30:
        print("error")
    elif n == 0:
        return 0
    elif n == 1 :#or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        


    