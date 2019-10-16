# supermath.py
'''This is a module designed either to fit in all the things that the regular Python math module 'missed', or simply
to make them easier to use.'''

# Author: Noah Broyles
# Email: noah@javamate.net
# Copyright: "None"


import math, getpass, os, fractions

pi = 3.1415926535897932384662643383279502884197
e  = 2.718281828459045235360287471352662497757

# Here is the validation class for True/False testing on things
class Validate:
    def isMac():
        """Unless some tricky person has a /System/Library/CoreServices/ folder on their PC with a Finder.app in it, this test will run correctly."""
        if os.path.exists('/System/Library/CoreServices/Finder.app'):
            return True
        else:
            return False

    def isPc():
        return not isMac()

    def hasLenOf(obj, length):
        """This is for validating the length of a thing.""" 
        if len(obj) == length:
            return True
        else:
            return False


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

def isRealNumber(number):
    if math.isnan(number) == False:
        return True
    else:
        return False

def squareRoot(number):
    return math.sqrt(number)

def exp(num, pow):
    return num**pow

# This is a beautiful quadratic equation solver! I used it for math. It worky!
def quadratic(a, b, c):
    try:
        x = (-b + math.sqrt(exp(b, 2) - (4*a*c))) / (2 * a)
        y = (-b - math.sqrt(exp(b, 2) - (4 * a * c))) / (2 * a)
        return x, y
    except ValueError:
        return 'Square root of negative number error! Don\'t ever do that again!'
    except ZeroDivisionError:
        return 'Divide by zero error! Don\'t ever do that again!'

# Returns the volume of a sphere based on the radius
def volSphere(r):
    global pi
    return (4/3 * (pi * r**3))

# Permutation notation
def permNote(n, r):
    return (math.factorial(n) / math.factorial((n - r)))

# Returns a division quotient with a remainder
def divideRemain(dividend, divisor):
    remainder = dividend % divisor
    if remainder == 0:
        return (dividend / divisor)
    else:
        ans = str(dividend / divisor)
        main = (ans.split('.'))[0]
        return int(main), remainder

# Trig functions in DEGREES like all the truly scientific minds prefer
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def csc(x):
    return (1 / sin(x))

def sec(x):
    return ((1 / cos(x)))

def cot(x):
    return (1 / tan(x))


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
                    return "y = " + str(fractions.Fraction(1/(4*p))) + "(" + "x - " + str(h) + ")^2 + " + str(k)
                elif h < 0:
                    return "y = " + str(fractions.Fraction(1/(4*p))) + "(" + "x + " + str(-h) + ")^2 + " + str(k)
                elif h == 0:
                    return "y = " + str(fractions.Fraction(1/(4*p))) + "x^2 + " + str(k)
            elif k < 0:
                if h > 0:
                    return "y = " + str(fractions.Fraction(1/(4*p))) + "(" + "x - " + str(h) + ")^2 - " + str(-k)
                elif h < 0:
                    return "y = " + str(fractions.Fraction(1/(4*p))) + "(" + "x + " + str(-h) + ")^2 - " + str(k)
                elif h == 0:
                    return "y = " + str(fractions.Fraction(1/(4*p))) + "x^2 - " + str(k)
        else:
            return "y = " + str(fractions.Fraction(1/(4*p))) + "x^2"
    except ZeroDivisionError:
        return "Those are not valid data points"
        

def areaOfPolygonInCircle(sides, radius):
    angle = (360 / sides) / 2
    x = radius * (sin(angle))
    A = radius * (cos(angle))
    area = ((x * A) / 2) * (sides * 2)
    return area

# This method solves algebraic equations using Cramer's rule of matrixes with a prolem looking like this:
def cramersRule(q, w, e,
               r, t, y):
    try:
        divisor = (q * t) - (r * w)
        x = ((e * t) - (y * w)) / divisor
        y = ((q * y) - (r * e)) / divisor
        return x, y
    except ZeroDivisionError:
        return "This problem has no solution."
# Cramer's rule is just so hot! I sure wish I had been taught about it a long while ago!


# This method gives the statistics on a list of numbers. I am quite proud of it!
def stats(list):
    # Get vars
    length = len(list)
    list = sorted(list) 
    # print(list)

    # Get mean
    mean = average(list)

    # Get median
    if length == 1:
        median = list[0]
    elif length == 2:
        median = mean
    else:
        if (length % 2) != 0:
            in1 = math.floor(length / 2)
            median = (list[in1])
        else:
            in1 = int(length / 2) - 1
            in2 = int(length / 2)
            median = (list[in1] + list[in2]) / 2

    # Get range
    r = list[-1] - list[0] # Whew! That was pretty easy!

    # Get modes / mode
    if not (length <= 1):
        modes = []
        copy = list.copy()
        try:
            for index in range(len(copy)):
                if copy[index - 1] == copy[index]:
                    modes.append(copy[index])
                    copy.pop(index - 1)
        except:
            pass
        mode = str(modes).strip('[]')
        if len(modes) == 0:
            mode = 'none'
    else: 
        mode = 'none'

    # Get standard deviation
    new = []
    for number in list:
        newNum = (number - mean) ** 2
        new.append(newNum)
    standard = math.sqrt(average(new))

    # Get variance
    variance = exp(standard, 2)

    # Return all the values
    return "mean = " + str(mean) + ", median = " + str(median) + ", range = " + str(r) + ", mode = " + str(mode) + ", standard deviation = " + str(standard) + ", variance = " + str(variance)
