#==================Count Frequency of each digits=============================
def digit_frequency(n: int) -> dict[int, int]:
    freq = {}
    for digit in str(n):
        freq[int(digit)] = freq.get(int(digit), 0) + 1
    return freq


#===================COUNT WORDS IN sTRINGS======================
def count_words(s: str) -> int:
    return len(s.split())


#=====================OPTIMIZE PRIME CHECK====================
import math

def is_prime_optimized(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


#============================CHECK PANGRAM================
import string

def is_pangram(s: str) -> bool:
    return set(string.ascii_lowercase).issubset(set(s.lower()))

#===================SECOND LARGEST IN LIST=================
def second_largest(lst: list[int]) -> int:
    unique = list(set(lst))
    unique.sort(reverse=True)
    return unique[1] if len(unique) >= 2 else None

#=======================REVERSE A NUMBER======================
def reverse_number(n: int) -> int:
    return int(str(n)[::-1])

#=========================COUNT CHARECTER TYPES======================
def count_chars(s: str) -> dict[str, int]:
    result = {"upper": 0, "lower": 0, "digit": 0, "special": 0}
    for ch in s:
        if ch.isupper():
            result["upper"] += 1
        elif ch.islower():
            result["lower"] += 1
        elif ch.isdigit():
            result["digit"] += 1
        else:
            result["special"] += 1
    return result

#============================FIND FACTORS=========================
def find_factors(n: int) -> list[int]:
    return [i for i in range(1, n + 1) if n % i == 0]

#=======================SUM OF DIGITS===================
def sum_of_digits(n: int) -> int:
    return sum(int(d) for d in str(n))

#======================POWER WITHOUT **===========================
def power(base: int, exponent: int) -> int:
    result = 1
    for _ in range(exponent):
        result *= base
    return result


#| Function                                                    | Output                                               |
#| ----------------------------------------------------------- | ---------------------------------------------------- |
digit_frequency(112233)     #                                  | `{1: 2, 2: 2, 3: 2}`                                 |
count_words("I love Python programming")      #                | `4`                                                  |
is_prime_optimized(29)                        #                     `True`                                               |
is_pangram("The quick brown fox jumps over the lazy dog") #    | `True`                                               |
second_largest([10, 20, 40, 30])                        #        | `30`                                                 |
reverse_number(1234)                                    #  | `4321`                                               |
count_chars("Python@123")                               #  | `{'upper': 1, 'lower': 5, 'digit': 3, 'special': 1}` |
find_factors(12)                                        # | `[1, 2, 3, 4, 6, 12]`                                |
sum_of_digits(123)                                      # | `6`                                                  |
power(2, 3)                                     #               | `8`                                                  |
