#!/usr/bin/env python
import sys

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
    function_choose = sys.argv[1]
    if function_choose > 0 and function_choose <= len(function_collection):
        function_number = int(sys.argv[1])
    
yval = function_collection[function_number - 1](xval)
