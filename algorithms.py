

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

    print(max(rock))
