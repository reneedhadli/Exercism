"""Calculate the number of grains of wheat on a chessboard.
 
A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.
 
This code calculates:
 
the number of grains on a given square
the total number of grains on the chessboard
"""
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)
def total():
    result = 0
    for loop in range(1, 65):
        result = result + square(loop)
    return result
