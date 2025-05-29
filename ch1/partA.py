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
