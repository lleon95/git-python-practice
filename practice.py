#!/usr/bin/env python

def fx(x):
    '''
    Initial function f(x)
    '''
    return x

# Main execution line
xval = [x * 0.1 for x in list(range(-50,51,1))]
yval = fx(xval)

