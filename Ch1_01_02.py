# Your task for "warm up" is: define a function that returns so called factorial.
# The recursion should terminate at factorial(0) = 1 so that we
# don't create an infinite loop.
def factorial(n): 
    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1)  # <-- replace this with the recursive call
        
print(factorial(6))              # this should print 720
