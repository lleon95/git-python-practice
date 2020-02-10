#!/usr/bin/env python
import sys
import math
import matplotlib.pyplot as plt

def fx(x):
    '''
    Initial function f(x)
    '''
    return x

def fx2(x):
    '''
    Trigonometric function f(x) = sin(x)
    '''
    return [ math.sin(xi) for xi in x ]

def fx3(x):
    '''
    Trigonometric function f(x) = cos(x)
    '''
    return [ math.cos(xi) for xi in x ]

def fx4(x):
    '''
    Trigonometric function f(x) = tan(x)
    '''
    return [ math.tan(xi) for xi in x ]

# Main execution line
xval = [x * 0.1 for x in list(range(-30,31,1))]

# Set default function
function_collection = [fx, fx2, fx3, fx4]
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
    print("\t - 2. f(x) = sin(x)")
    print("\t - 3. f(x) = cos(x)")
    print("\t - 4. f(x) = tan(x)")
    print("Non-valid function numbers fallback to function 1")
    exit()
    
yval = function_collection[function_number - 1](xval)

# Plot
plt.plot(xval, yval)
plt.title("Plotting function " + str(function_number))
plt.xlabel("Values for x")
plt.ylabel("Values for f(x)")
plt.show()
