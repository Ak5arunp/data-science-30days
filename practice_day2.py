#======================== Print Prime Numbers from 1 to 100========================

# Output: 2, 3, 5, 7, ..., 97
import math

def prime_upto_100() -> list[int]:
    primes = []
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

#========================Count frequency of each element in a list=======================

def count_frequency(lst: list[int]) -> dict[int, int]:
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

#============================Sum of even numbers from 1 to N=============================

def sum_even_upto_n(n: int) -> int:
    return sum(i for i in range(2, n+1, 2))

#========================== Fibonacci series up to N terms==================================

def fibonacci_series(n: int) -> list[int]:
    if n == 0: return []
    if n == 1: return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


#============================Armstrong number check (3-digit only)================================

def is_armstrong(n: int) -> bool:
    if n < 100 or n > 999:
        return False
    total = sum(int(digit)**3 for digit in str(n))
    return total == n


#==================================Remove duplicates from a list============================

def remove_duplicates(lst: list[int]) -> list[int]:
    return list(set(lst))


#===================================Factorial using loop============================

def factorial_loop(n: int) -> int:
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


#===================================Reverse an integer (e.g. 123 → 321)==================
def reverse_integer(n: int) -> int:
    reversed_num = int(str(n)[::-1])
    return reversed_num

#==================================Check if number is perfect number========================
def is_perfect(n: int) -> bool:
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n

#===================================Count words and characters in a string===================
def count_words_and_chars(text: str) -> tuple[int, int]:
    words = text.strip().split()
    return len(words), len(text.replace(" ", ""))


print(count_frequency([1,2,2,3,3,3,4]))
print(prime_upto_100())
print(sum_even_upto_n(10))
print(fibonacci_series(7))
print(is_armstrong(153))
print(remove_duplicates([1,2,2,3,3]))
print(factorial_loop(5))
print(reverse_integer(12345))
print(is_perfect(28))
print(count_words_and_chars("Data science is power"))
