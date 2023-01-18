import math
class Sym:

    def __init__(self):
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, x: chr):

        self.n = self.n + 1
        if x in self.has:
            self.has[x] = self.has[x] + 1
        else:
            self.has[x] = 1
        
        if self.has[x] > self.most:
            self.most = self.has[x]
            self.mode = x
    
    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for i in self.has:
            p = self.has[i] / self.n
            e = e + (p * math.log(p, 2))
        return -e



