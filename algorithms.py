import re

def multiples():
    count = 0
    for number in range(0, 1000):
        if number % 3 == 0:
            count += number
        elif number % 5 == 0:
            count += number


def fibonacci():
    def recur_fibo(n):
        if n <= 1:
            return n
        else:
            return recur_fibo(n-1) + recur_fibo(n-2)
    for i in range(70):
        print(recur_fibo(i))


def prime_factor():
    n = 600851475143
    for j in range(100000):
        if j != 0:
            if n % j == 0:
                n = n / j
                print(j)


def palindrome():
    rock = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            n = i * j
            begin = str(n)
            reversed_begin = begin[::-1]
            if begin == reversed_begin:
                rock.append(n)


def getCount(inputStr):
    num_vowels = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for char in inputStr:
        for vowel in vowels:
            if char == vowel:
                num_vowels += 1

    return num_vowels

def cockroach_speed(s):
    n = 27.7778
    return int(s * n)

def reverse_seq(n):
    res = []
    for i in range(1, n + 1):
        res.append(i)

    return res[::-1]

# or

def reverse_seq(n):
    return list(range(n, 0, -1))

def square_sum(numbers):
    return sum([n ** 2 for n in numbers])


def get_real_floor(n):
    if n >= 15:
        return n - 2
    elif n <= 0:
        return n
    elif n <= 15:
        return n - 1

def is_vowel(s):
    if len(s) > 1:
        return False
    elif len(re.findall(r'[aeiAEI]', s)):
        return True
    elif len(s) == 0: return False


