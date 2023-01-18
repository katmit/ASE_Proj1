
class Num:

    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0

        self.lo = float('inf')
        self.hi = float('-inf')


    def add(self, value: float):
        self.n = self.n + 1
        d = value - self.mu
        self.mu = self.mu + (d / self.n)
        self.m2 = self.m2 + (d * (value - self.mu))
        self.lo = min(value, self.lo)
        self.hi = max(value, self.hi)

    def mid(self):
        return self.mu

    def div(self): #return standard deviation using Welford's algorithm http://t.ly/nn_W
        if((self.m2 < 0) or (self.n < 2)):
            return 0
        return pow((self.m2 / (self.n - 1)), 0.5)

