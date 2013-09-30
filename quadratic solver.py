from sys import argv
import math


def quadratic(a, b, c):
    first_solution = ((-1) * (b) + math.sqrt((b)**2 - 4 * (a) * (c)))/(2 * (a))
    second_solution = ((-1) * (b) - math.sqrt((b)**2 - 4 * (a) * (c)))/(2 * (a))
    
    print "x =",first_solution,"\n  ",second_solution
    
    print "if following is '0.0' '0.0', solutions are correct."
    print (a * ((first_solution)**2)) + (b * first_solution) + c
    print (a * ((first_solution)**2)) + (b * first_solution) + c

while True:
    print "Please enter a, b, c:"
    a = float(raw_input())
    b = float(raw_input())
    c = float(raw_input())

    quadratic(a, b, c)