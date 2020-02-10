#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt

def fx(x):
    '''
    Initial function f(x)
    '''
    return x

# Main execution line
xval = [x * 0.1 for x in list(range(-50,51,1))]

# Set default function
function_collection = [fx]
function_number = 1

if len(sys.argv) > 1:
    function_choose = int(sys.argv[1])
    if function_choose > 0 and function_choose <= len(function_collection):
        function_number = function_choose
    
yval = function_collection[function_number - 1](xval)

# Plot
plt.plot(xval, yval)
plt.title("Plotting function " + str(function_number))
plt.xlabel("Values for x")
plt.ylabel("Values for f(x)")
plt.show()
