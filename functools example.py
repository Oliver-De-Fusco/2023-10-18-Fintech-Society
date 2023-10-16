from functools import cache
# Functools gives us decorators to use for functions
# Decorators wrap a target function inside of them to easily add extra functionallity
# In this case the functools cache method which stores our input and the respective output so it doesnt have to be calculated over and over
# This significantly speeds up programs and even makes some calculations possible


# @cache
def fibonacci(n):
    if n <= 1: # This is the base case, a recurisve function without a base case will continue forever
        return n 

    return fibonacci(n-1) + fibonacci(n-2) # fibonacci is defined as the previous two numbers added together


print(fibonacci(50))