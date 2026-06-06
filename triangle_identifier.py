"""An equilateral triangle has all three sides the same length.
 
An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
 
A scalene triangle has all sides of different lengths.
"""
def valid_triangle(sides):
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b
def equilateral(sides):
    if not valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b and b == c
def isosceles(sides):
    if not valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b or b == c or c == a
def scalene(sides):
    if not valid_triangle(sides):
        return False
    a, b, c = sides
    return a != b and b != c and c != a
