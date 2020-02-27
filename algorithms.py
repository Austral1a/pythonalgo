import re
import os
from math import *
import functools
from collections import defaultdict
from collections import Counter


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
            return recur_fibo(n - 1) + recur_fibo(n - 2)

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
    elif len(s) == 0:
        return False


def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


def number_of_occurrences(element, sample):
    res = []
    for x in sample:
        if x == element:
            res.append(x)
    return len(res)


def compareTriplets(a, b):
    aInt = 0
    bInt = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            aInt += 1
        elif a[i] < b[i]:
            bInt += 1
    res = [aInt, bInt]  # alice, bob
    return res


def aVeryBigSum(ar):
    return sum(ar)


def diagonalDifference(arr):
    r = len(arr) - 1
    d1, d2 = [], []
    for row in range(0, len(arr)):
        d1.append(arr[row][row])
        d2.append(arr[row][r])
        r -= 1
    return abs(sum(d1) - sum(d2))


def plusMinus(arr):
    plus, minus, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
        else:
            zero += 1

    pos = sum(map(lambda i: i > 0, arr)) * 1.0 / len(arr)
    neg = sum(map(lambda i: i < 0, arr)) * 1.0 / len(arr)
    zer = sum(map(lambda i: i == 0, arr)) * 1.0 / len(arr)
    print(pos, neg, zer)
    print("%f\n%f\n%f\n" % (plus / len(arr), minus / len(arr), zero / len(arr)))


def simpleArraySum(ar):
    return sum(ar)


def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + ('#' * i))


def miniMaxSum(arr):
    """
        SAS
    """
    min = sorted(arr)
    max = sorted(arr)[::-1]
    print(sum(min[:4]), sum(max[:4]))


def ASCII(str):
    codes = functools.reduce(lambda a, b: a + b, [ord(c) for c in str])
    return print(codes)


def birthdayCakeCandles(ar):
    heighest = sorted(ar)[::-1]
    return heighest.count(heighest[0])




def timeConversion(s):
    h = int(s[0:2])
    if s[-2:] == 'PM':
        if h != 12:
            h += 12
    else:
        if h == 12:
            h = 0
    return '%02d%s' % (h, s[2:-2])



def odd_one_out(s):
    arr = [c for c in s]
    coincidence = []
    for c in arr:
        if arr.count(c) > 1:
            coincidence.append(c)

    #[coincidence.remove(c) if coincidence.count(c) % 2 != 0 else None for c in coincidence]

    for c in coincidence:
        if coincidence.count(c) % 2 != 0:
            coincidence.remove(c)

    for c in coincidence:
        del arr[arr.index(c)]
       # arr.pop(arr.index(c))
    return arr



def count_inversions(array):
    sample = sorted(array)
    counter = 0
    def bubble_sort(arr):
        nonlocal counter
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    counter += 1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    bubble_sort(array)
    return counter


def countBits(n):
    res = []
    res = [True if b == '1' else None for b in bin(n)[2:]]
    return res.count(True)
    #return bin(n).count('1')


def grabscrab(word, possible_words):
    res = []
    for i in possible_words:
        print()
    for c in possible_words:
        my_re = r'[' + word + ']'
        res.append(re.findall(my_re, c))
    print(res)


def two_oldest_ages(ages):
    res = []
    for i in range(0, 2):
        res.append(max(ages))
        ages.remove(max(ages))
    return res[::-1]

def bouncingBall(h, bounce, window):
    mSeen = 0
    if h > 0 and 0 < bounce < 1 and window < h:
        hCopy = h
        while True:
            hCopy *= bounce
            mSeen += 2
            if hCopy <= window:
                break
        print(mSeen - 1)
        return mSeen - 1
    else:
        return -1
