#test suite!

import random
import helpers

from main import seed, dump
from num import Num
from sym import Sym

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

    m1 = helpers.rnd(num1.mid(), 10)
    m2 = helpers.rnd(num2.mid(), 10)

    return (m1 == m2) and helpers.rnd(m1, 1) == 0.5


def test_syms():
    sym = Sym()
    values = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    for value in values:
        sym.add(value)

    return ('a' == sym.mid()) and (1.379 == helpers.rnd(sym.div()))

def test_nums():
    num = Num()
    values = [1, 1, 1, 1, 2, 2, 3]
    for value in values:
        num.add(value)
    
    return ((11/ 7) == num.mid()) and (0.787 == helpers.rnd(num.div()))