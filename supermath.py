# supermath.py
'''This is a module designed either to fit in all the things that the regular Python math module 'missed', or simply
to make them easier to use.'''

# Authors: Noah Broyles and ankith26
# Copyright: "None"


import math
import random
import fractions

pi = 3.1415926535897932384662643383279502884197
realpi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989
e = 2.718281828459045235360287471352662497757


# Here are the regular functions of math
def average(listOfNums):
    total = math.fsum(listOfNums)
    av = (total / len(listOfNums))
    return av


# The mean is sorta the same as the average
def mean(listOfNums):
    return average(listOfNums)


# I did not write this one
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# we know lcm * gcd of two numbers is equal to their product
def lcm(a, b):
    return (a * b) / gcd(a, b)


def isRealNumber(number):
    if not math.isnan(number):
        return True
    else:
        return False


def squareRoot(number):
    return math.sqrt(number)


def fastExp(num, power):
    # Thanks to anteprandium @ https://gist.github.com/anteprandium/3c5d855f96e3d39fe604 for the algorithm for super fast exponentiation in python!
    def bits_of(m):
        n = int(m)
        while n:
            yield n & 1
            n >>= 1

    result = 1
    partial = num

    for bit in bits_of(power):
        if bit:
            result *= partial
        partial **= 2

    return result


# This is a beautiful quadratic equation solver! I used it for math. It worketh!
def quadratic(a, b, c):
    try:
        x = (-b + math.sqrt(fastExp(b, 2) - (4 * a * c))) / (2 * a)
        y = (-b - math.sqrt(fastExp(b, 2) - (4 * a * c))) / (2 * a)
        return x, y
    except ValueError:
        return 'The equation has no real roots!'
    except ZeroDivisionError:
        return 'The equation entered is not a quadratic (how could you enter a = 0)!!'


# Returns the volume of a sphere based on the radius
def volSphere(r):
    global pi
    return 4 / 3 * (pi * r ** 3)


# Permutation notation
def permNote(n, r):
    return math.factorial(n) / math.factorial((n - r))


# Combination notation
def combNote(n, r):
    return permNote(n, r) / math.factorial(r)


# Returns a division quotient with a remainder
def divideRemain(dividend, divisor):
    remainder = dividend % divisor
    if remainder == 0:
        return int(dividend / divisor), 0
    else:
        ans = str(dividend / divisor)
        main = (ans.split('.'))[0]
        return int(main), remainder


# Trig functions in DEGREES like all the truly scientific minds prefer

# small modification by ankith26,
# you can specify in the trigonometric function
# wether you want degree or radian with the degree being the default
# if you want radians, use
# sin(pi/2, False)

def sin(x, degree=True):
    if degree:
        x = math.radians(x)
    return math.sin(x)


def cos(x, degree=True):
    if degree:
        x = math.radians(x)
    return math.cos(x)


def tan(x, degree=True):
    if degree:
        x = math.radians(x)
    return math.tan(x)


def csc(x, degree=True):
    return 1 / sin(x, degree)


def sec(x, degree=True):
    return 1 / cos(x, degree)


def cot(x, degree=True):
    return 1 / tan(x, degree)


# Returns the equation of a parabola when given the coordinates of the vertex and focus. Vertex vars: (xv, yv) Focus vars: (xf, yf)
def parabolaEquation(xv, yv, xf, yf):
    # I am so proud of this function! I can't sing it's praise enough!
    try:
        h = xv
        k = yv
        p = -(k - yf)
        if yv != 0:
            if k > 0:
                if h > 0:
                    return "y = " + str(fractions.Fraction(1 / (4 * p))) + "(" + "x - " + str(h) + ")^2 + " + str(k)
                elif h < 0:
                    return "y = " + str(fractions.Fraction(1 / (4 * p))) + "(" + "x + " + str(-h) + ")^2 + " + str(k)
                elif h == 0:
                    return "y = " + str(fractions.Fraction(1 / (4 * p))) + "x^2 + " + str(k)
            elif k < 0:
                if h > 0:
                    return "y = " + str(fractions.Fraction(1 / (4 * p))) + "(" + "x - " + str(h) + ")^2 - " + str(-k)
                elif h < 0:
                    return "y = " + str(fractions.Fraction(1 / (4 * p))) + "(" + "x + " + str(-h) + ")^2 - " + str(k)
                elif h == 0:
                    return "y = " + str(fractions.Fraction(1 / (4 * p))) + "x^2 - " + str(k)
        else:
            return "y = " + str(fractions.Fraction(1 / (4 * p))) + "x^2"
    except ZeroDivisionError:
        return "Those are not valid data points"


def areaOfPolygonInCircle(sides, radius):
    angle = (360 / sides) / 2
    x = radius * (sin(angle))
    A = radius * (cos(angle))
    area = ((x * A) / 2) * (sides * 2)
    return area


# This method solves algebraic equations using Cramer's rule of matrices with a problem looking like this:
def cramersRule(q, w, e, r, t, y):
    divisor = (q * t) - (r * w)
    if divisor != 0:
        x = ((e * t) - (y * w)) / divisor
        y = ((q * y) - (r * e)) / divisor
        return x, y
    elif (q * y) == (r * e):
        return "This problem has infinite solutions (when equations are graphed, we get coincident lines)"
    else:
        return "This problem has no solution (when equations are graphed, they are parallel and do not intersect)"


# Cramer's rule is just so hot! I sure wish I had been taught about it a long while ago!


# This method gives the statistics on a list of numbers. I am quite proud of it!
def stats(lis):
    # Get vars
    length = len(lis)
    lis = sorted(lis)

    # Get mean
    mean = average(lis)

    # Get median
    if length == 1:
        median = lis[0]
    elif length == 2:
        median = mean
    else:
        if (length % 2) != 0:
            in1 = math.floor(length / 2)
            median = (lis[in1])
        else:
            in1 = int(length / 2) - 1
            in2 = int(length / 2)
            median = (lis[in1] + lis[in2]) / 2

    # Get range
    r = lis[-1] - lis[0]  # Whew! That was pretty easy!

    # Get modes / mode
    if not (length <= 1):
        modes = []
        copy = lis.copy()
        try:
            for index in range(len(copy)):
                if copy[index - 1] == copy[index]:
                    modes.append(copy[index])
                    copy.pop(index - 1)
        except IndexError:
            pass
        mode = list(set([number for number in modes]))
        if len(modes) == 0:
            mode = None
    else:
        mode = None

    # Get standard deviation
    new = []
    for number in lis:
        newNum = (number - mean) ** 2
        new.append(newNum)
    standard = math.sqrt(average(new))

    # Get variance
    variance = fastExp(standard, 2)

    # Return all the values
    return {"mean": mean, "median": median, "range": r, "mode": mode, "standardDeviation": standard, "variance": variance}


def isPrime(n):
    # Miller-Rabin primality test implemented in Python
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(40):  # 40 is a good amount of times to test for primality
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
