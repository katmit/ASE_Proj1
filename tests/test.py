#test suite!

import random
import math
import os
import sys
import traceback

sys.path.append(os.path.abspath('../'))
from src.script import get_seed, should_dump, get_crashing_behavior_message
from src.num import Num
from src.sym import Sym

def round(n, nPlaces = 3):
    mult = math.pow(10, nPlaces)
    return math.floor(n*mult + 0.5) / mult

def test_show_dump():
    test_exception = Exception("This is a test exception")
    try:
        raise test_exception
    except Exception as e:
        expected_output = str(test_exception)
        output = get_crashing_behavior_message(test_exception)

        if should_dump():
            return len(output) > len(expected_output) and expected_output in output
        else:
            return expected_output == output


# "generate, reset, regenerate same"
def test_num_generation_rand() -> bool:
    num1 = Num()
    num2 = Num()

    temp_random = random.Random()
    temp_random.seed(get_seed())

    for i in range(1000):
        val = temp_random.randrange(0, 2)
        num1.add(val)

    temp_random.seed(get_seed()) #reset the random

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