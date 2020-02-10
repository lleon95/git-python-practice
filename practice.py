#!/usr/bin/env python
import sys
import math
import matplotlib.pyplot as plt

def fx(x):
    '''
    Initial function f(x)
    '''
    return x

# Function 2
def fx2_p(x):
    '''
    Polynomial function: f(x) = x**2
    '''
    return [ xi**2 for xi in x ]

# Function 3
def fx3_p(x):
    '''
    Polynomial function: f(x) = x**3
    '''
    return [ xi**3 for xi in x ]

def fx2_t(x):
    '''
    Trigonometric function f(x) = sin(x)
    '''
    return [ math.sin(xi) for xi in x ]

def fx3_t(x):
    '''
    Trigonometric function f(x) = cos(x)
    '''
    return [ math.cos(xi) for xi in x ]

def fx4_t(x):
    '''
    Trigonometric function f(x) = tan(x)
    '''
    return [ math.tan(xi) for xi in x ]

# Main execution line
xval = [x * 0.1 for x in list(range(-30,31,1))]

# Set default function
function_collection = [fx, fx2_p, fx3_p, fx2_t, fx3_t, fx4_t]
function_number = 1

if len(sys.argv) > 1:
    function_choose = int(sys.argv[1])
    if function_choose > 0 and function_choose <= len(function_collection):
        function_number = function_choose
    else:
        print("Resolving as function 1...")
else:
    print("Usage: " + sys.argv[0] + " <function number>")
    print("Where function numbers are: ")
    print("\t - 1. f(x) = x")
    print("\t - 2. f(x) = x^2")
    print("\t - 3. f(x) = x^3")
    print("\t - 4. f(x) = sin(x)")
    print("\t - 5. f(x) = cos(x)")
    print("\t - 6. f(x) = tan(x)")
    print("Non-valid function numbers fallback to function 1")
    exit()
    
yval = function_collection[function_number - 1](xval)

# Plot
plt.plot(xval, yval)
plt.title("Plotting function " + str(function_number))
plt.xlabel("Values for x")
plt.ylabel("Values for f(x)")
plt.show()
