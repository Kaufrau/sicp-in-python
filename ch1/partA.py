# Exercise 1.6
def abs(x):
    if x < 0:
        return -x
    else:
        return x


def average(x, y):
    return (x + y) / 2


def square(x):
    return x * x


def improve(guess, x):
    return average(guess, x / guess)


def good_enough(previous_guess, guess):
    return abs((guess - previous_guess) / guess) < 0.00000000001


def sqrt_iter(guess, x):
    if good_enough(guess, improve(guess, x)):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)


def sqrt(x):
    return sqrt_iter(1.0, x)


print(sqrt(4))
print(sqrt(123456789012345))
print(sqrt(0.00000000123456))


# Exercise 1.8
def cube(x):
    return x * x * x


def abs(x):
    if x < 0:
        return -x
    else:
        return x


def good_enough(previous_guess, guess):
    return abs(guess - previous_guess) < 0.00000000001


def cube_root_iter(guess, x):
    if good_enough(improve(guess, x), guess):
        return guess
    else:
        return cube_root_iter(improve(guess, x), x)


def improve(guess, x):
    return (x / (guess * guess) + 2 * guess) / 3


def cube_root(x):
    return cube_root_iter(1.0, x)


print(cube(cube_root(12345)))


def average(x, y):
    return (x + y) / 2


def square(x):
    return x * x


def sqrt(x):
    def good_enough(guess, x):
        return abs(square(guess) - x) < 0.001

    def improve(guess, x):
        return average(guess, x / guess)

    def sqrt_iter(guess, x):
        if good_enough(guess, x):
            return guess
        else:
            return sqrt_iter(improve(guess, x), x)

    sqrt_iter(1.0, x)


def sqrt_lexical_scoping(x):
    def good_enough(guess):
        return square(guess) - x < 0.001

    def improve(guess):
        return average(guess, x / guess)

    def sqrt_iter(guess):
        if good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))

    sqrt_iter(1.0)


# Linear recursive version (calls build up on the call stack)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial(n):
    fact_iter(1, 1, n)


def fact_iter(product, counter, max_count):
    if counter > max_count:
        return product
    else:
        return fact_iter(counter * product, counter + 1, max_count)


def factorial(n):
    def iter(product, counter):
        if counter > n:
            return product
        else:
            return iter(counter * product, counter + 1)

    return iter(1, 1)


print(factorial(6))


# Exercise 1.9
def inc(x):
    return x + 1


def dec(x):
    return x - 1


def plus(a, b):
    if a == 0:
        return b
    else:
        return inc(dec(a) + b)


def plus(a, b):
    if a == 0:
        return b
    else:
        return dec(a) + inc(b)


print(plus(4, 5))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))


def fib(n):
    def fib_iter(a, b, count):
        if count == 0:
            b
        else:
            fib_iter((a + b), a, count - 1)

    fib_iter(1, 0, n)


def count_change(amount):
    def cc(amount, kinds_of_coins):
        if amount == 0:
            return 1
        elif (amount < 0) or (kinds_of_coins == 0):
            return 0
        else:
            return cc(amount, kinds_of_coins - 1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)

    def first_denomination(kinds_of_coins):
        if kinds_of_coins == 1:
            return 1
        elif kinds_of_coins == 2:
            return 5
        elif kinds_of_coins == 3:
            return 10
        elif kinds_of_coins == 4:
            return 25
        elif kinds_of_coins == 5:
            return 50

    return cc(amount, 5)


assert count_change(100) == 292


# Exercise 1.11
def f(n):
    if n < 3:
        return n
    else:
        return f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)


def f_iter(n):
    if n < 3:
        return n
    a, b, c = 0, 1, 2  # f(0), f(1), f(2)
    for i in range(3, n + 1):
        next_f = c + 2 * b + 3 * a
        a, b, c = b, c, next_f
    return c


for i in range(10):
    assert f(i) == f_iter(i)


# Exercise 1.12.
def pascal(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return pascal(row - 1, col - 1) + pascal(row - 1, col)


def display_pascal_row(n, col=0):
    if col > n:
        print()  # newline at the end of row
        return
    print(pascal(n, col), end=" ")
    display_pascal_row(n, col + 1)


def display_pascal(n, row=0):
    if row > n:
        return
    display_pascal_row(row)
    display_pascal(n, row + 1)


display_pascal(10)
