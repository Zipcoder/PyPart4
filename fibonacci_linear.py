def fibonacci(n):
    x=0
    for i in range(2):
        n = n-1
        print(n)
        x = x+n
        print(x)
    #print(x)
    return x

fibonacci(4)