# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 22:49:48 2025

@author: admin
"""

import cmath  # Import cmath to handle complex numbers

def quadratic_equ(a, b, c):
    if a == 0:
        return f"Invalid input: {a} cannot be zero in a quadratic equation."

    d = (b ** 2) - (4 * a * c)  # Compute discriminant
    
    if d > 0:
        # Two distinct real roots
        root1 = (-b + d ** 0.5) / (2 * a)
        root2 = (-b - d ** 0.5) / (2 * a)
        return f"The Roots For {a}, {b}, {c} are:\nRoot 1: {root1}\nRoot 2: {root2}"
    
    elif d == 0:
        # One real root (double root)
        root = -b / (2 * a)
        return f"The Roots For {a}, {b}, {c} are:\nDouble Root: {root}"
    
    else:
        # Complex roots (when d < 0)
        root1 = (-b + cmath.sqrt(d)) / (2 * a)
        root2 = (-b - cmath.sqrt(d)) / (2 * a)
        return f"The Roots For {a}, {b}, {c} are:\nRoot 1: {root1}\nRoot 2: {root2}"

# Take user input
a = float(input("Enter the coefficient of x² (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

# Print the result
print(quadratic_equ(a, b, c))
