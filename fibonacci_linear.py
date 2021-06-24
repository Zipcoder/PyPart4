def fibonacci(n):
    fib_array = [0,1]
    #print(fib_array)
    fib_answer = 0
    #print(fib_answer)
    fib_index_1 = fib_array[0]
    fib_index_2 = fib_array[1]
    #print(fib_index_1)
    #print(fib_index_2)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return print('error')
    else:
        #loop
        for n in range(n-1):
            #print('in loop')
            fib_answer = fib_index_1 + fib_index_2
            fib_array[0] = fib_index_2
            fib_array[1] = fib_answer

            fib_index_1 = fib_array[0]
            fib_index_2 = fib_array[1]

            
            #print(fib_index_1)
            #print(fib_index_2)
            #print(fib_answer)
            #print(fib_array)
            
        return fib_answer



