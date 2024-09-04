#!/usr/bin/env python3

#"def print_fibonacci(length):
   # '''Prints the first 'length' numbers in the Fibonacci sequence.'''
   # if length == 0:
      #  print('[]')
       # return
    #fib_sequence = [0, 1]
    #while len(fib_sequence) < length:
        #fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fibonacci = [0, 1]
    
    while len(fibonacci) < length:
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)
    
    print(fibonacci[:length])