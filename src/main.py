
import sys
import random

import tests

# set to their default values
random_instance = random.Random()
seed = 937162211 
dump = False


def run_tests():
    print("Executing tests...\n")
    
    passCount = 0
    failCount = 0
    test_suite = [tests.test_num_generation_rand, tests.test_syms, tests.test_nums]

    for test in test_suite:
        if(test()):
            passCount = passCount + 1
        else:
            failCount = failCount + 1
    
    print("Passing: " + str(passCount) + "\nFailing: " + str(failCount))



def find_arg_value(args: list(str), optionA: str, optionB: str) -> str:
    index = args.index(optionA) if optionA in args else args.index(optionB)
    if (index + 1) < len(args):
        return args[index + 1]
    return None

help_string = """script.py : an example script with help text and a test suite.\n
based on the original script (script.lua) by Tim Menzies <timm@ieee.org>\n
\n
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
]]"""

if __name__ == "__main__":
    args = sys.argv

    if '-h' in args or '--help' in args:
        print(help_string)

    if '-d' in args or '--dump' in args:
        dump_value = find_arg_value(args, 'd', '--dump')
        if dump_value is not None:
            dump_value_lower = dump_value.lower()
            dump = True if dump_value_lower.contains('true') else False

    if '-s' in args or '--seed' in args:
        seed_value = find_arg_value(args, '-s', '--seed')
        if seed_value is not None:
            try:
                seed = int(seed_value)
            except ValueError:
                print("Seed value must be an integer!")
        else:
            print("USAGE: Provide an integer value following an -s or --seed argument to set the seed value.\n Example: (-s 3030, --seed 3030)")
    
    # NOTE: the seed will be set in main, the rest of the application need not set it
    random_instance.seed(seed)    
    if '-g' in args or '--go' in args:
        run_tests()