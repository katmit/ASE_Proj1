import re,math

class main:

    # Numerics 
    Seed = 937162211
    rand =0
    rint =0
    rnd =0

    def rand(lo , hi):
        lo = lo or 0
        hi = hi or 1
        Seed = (16807 * Seed ) % 2147483647

    def rint(lo, hi):
        return math.floor(0.5 + rand(lo,hi))

    def rnd(n, nPlaces):
        mult = math.pow(10, nplaces or 3)
        return math.floor(n*mult + 0.5)/mult


    # Lists


    # Strings

    # Main