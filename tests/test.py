#test suite!

import random
import math

from src.main import seed, dump
from src.num import Num
from src.sym import Sym

def round(n, nPlaces = 3):
    mult = math.pow(10, nPlaces)
    return math.floor(n*mult + 0.5) / mult

def show_settings_test():
    #todo, i'm not sure how to do this
    pass

# "generate, reset, regenerate same"
def test_num_generation_rand() -> bool:
    num1 = Num()
    num2 = Num()

    temp_random = random.Random()
    temp_random.seed(seed)

    for i in range(1000):
        val = temp_random.randrange(0, 2)
        num1.add(val)

    temp_random.seed(seed) #reset the random

    for i in range(1000):
        val = temp_random.randrange(0, 2)
        num2.add(val)

    m1 = round(num1.mid(), 10)
    m2 = round(num2.mid(), 10)

    return (m1 == m2) and round(m1, 1) == 0.5


def test_syms():
    sym = Sym()
    values = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    for value in values:
        sym.add(value)

    return ('a' == sym.mid()) and (1.379 == round(sym.div()))

def test_nums():
    num = Num()
    values = [1, 1, 1, 1, 2, 2, 3]
    for value in values:
        num.add(value)
    
    return ((11/ 7) == num.mid()) and (0.787 == round(num.div()))