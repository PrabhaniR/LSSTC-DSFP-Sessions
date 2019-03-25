
import math

def even(x):
    c = math.ceil(x)
    f = math.floor(x)
    if c%2 == 0:
        r = c
    else:
        r = f
    return r