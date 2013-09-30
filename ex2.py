import math

a = float(raw_input("a:"))
b = float(raw_input("b:"))
c = float(raw_input("c:"))

first_solution = ((-1) * (b) + math.sqrt((b)**2 - 4 * (a) * (c)))/(2 * (a))

second_solution = ((-1) * (b) - math.sqrt((b)**2 - 4 * (a) * (c)))/(2 * (a))

print "x =",first_solution,"\n  ",second_solution