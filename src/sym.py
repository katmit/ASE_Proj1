import math
class sym:
    n =0
    has = []
    most =0
    mode =None
    def __init__(self,n,has,most,mode):
        self.n =n
        self.has = has
        self.most =most
        self.mode = mode

    def add(self,x):
        if(x!= "?"):
            self.n = self.n +1
            self.has[x] = 1 + self.has[x]
            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x
    
    def mid(self,x):
        return self.mode
        
    def div(self, x ,fun ,e):
        e =0
        for i in self.has:
            e = e + fun(i/self.n)
        return e

    def fun(p):
        return p*math.log(p,2)






