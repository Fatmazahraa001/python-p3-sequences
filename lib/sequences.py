#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length <= 0:
        print([])
        return
    
    fibonacci = [0, 1]
    
    while len(fibonacci) < length:
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)
    
    print(fibonacci[:length])