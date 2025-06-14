# 1.==========Write a Python function using lambda to multiply two numbers.========
def use_lambda(*args:tuple)->int:
    a=1
    for i in args:
        c=lambda i:a*i  # c is the refrence of lambda function
        a=c(i) # lambda function call use c(i)
    print(a)

use_lambda(2,3,4)        

# 2.===========Use map() to get the square of each number from a list.========

# map() Python ka built-in function hai jo kisi function ko har element par apply karta hai ek iterable (jaise list, tuple, etc.) ke
# map(function, iterable)
# function: ek function jo har element par apply hoga.
# iterable: jaise list, tuple, string, etc.
def use_map(a:list)->list:
    n=map(lambda x:x**2,a) #
    print(list(n))

use_map([2,3,4,5])

# 3.Use filter() to find all numbers divisible by 3 from a list.

def use_filter(a:list)->list:
    n=filter(lambda x:x%3==0,a)
    print(list(n))

use_filter([3,6,5,7,9,8])    

#4. Use reduce() to multiply all elements in a list.
from functools import reduce
def use_reduce(n:list)->int:
    a=reduce(lambda x,y:x*y,n)
    print(a)
use_reduce([3,4,5,5])    

#5.  Check if a string is a pangram (contains all 26 letters)
# Aisa sentence jisme English alphabet ke saare 26 letters kam se kam ek baar ho
def is_pangram(s: str) -> bool:
    s = s.lower()
    letters = set()

    for char in s:
        if 'a' <= char <= 'z':
            letters.add(char)

    return len(letters) == 26

# Test
text = "The quick brown fox jumps over the lazy dog"
print(is_pangram(text))  # Output: True
