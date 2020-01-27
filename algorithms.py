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


fibonacci()
