import math

#============SWAP TWO NUMBERS==================================================
def swap_numbers(a: int, b: int) -> tuple[int, int]:
    a, b = b, a
    return a, b


#================EVEN OR ODD===================================================
def is_even(num: int) -> bool:
    # num & 1 == 0 means even
    return num & 1 == 0


#================FACTORIAL OF A NUMBER=========================================
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)




#==================PRIME NUMBER CHECK==========================================
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


#==================REVERSE A STRING============================================
def reverse_string(s: str) -> str:
    return s[::-1]




#=================LARGEST OF THREE NUMBERS=====================================
def largest_of_three(a: int, b: int, c: int) -> int:
    return max(a, b, c)


#==================SUM OF A LIST===============================================
def sum_list(lst: list[int]) -> int:
    return sum(lst)


#===============COUNT VOWELS IN A STRING=======================================
def count_vowels(s: str) -> int:
    count = 0
    for char in s.lower():
        if char in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    return count




#==============MULTIPLICATION TABLE (1 to 10)===================================
def multiplication_table(n: int) -> None:
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")


#===============PALINDROME STRING CHECK========================================
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


print(swap_numbers(3, 5))
print(is_even(4))
print(factorial(5))
print(is_prime(17))
print(reverse_string("hello"))
print(largest_of_three(5, 10, 3))
print(sum_list([1, 2, 3]))
print(count_vowels("Education"))
multiplication_table(7)
print(is_palindrome("madam"))
