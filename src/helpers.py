

from ast import literal_eval
from main import random_instance
import re, math

# ----------------------------------------------- STRINGS -----------------------------------------------

def fmt(sControl: str, *args): #control string (format string)
    for string in args:
        print(string.format(sControl))

def o(t: object):
    #todo(ksm)
    return ""

def oo(t: object):
    print(o(t))
    return t

def coerce(s: str):
    type = literal_eval(s)
    return type


# ----------------------------------------------- NUMERICS -----------------------------------------------

def rand(lo , hi):
    return random_instance.randrange(lo, hi)

def rint(lo, hi):
    return math.floor(0.5 + rand(lo,hi))

def rnd(n, nPlaces = 3):
    mult = math.pow(10, nPlaces)
    return math.floor(n*mult + 0.5) / mult

# ----------------------------------------------- LISTS -----------------------------------------------

# do we even need this stuff?