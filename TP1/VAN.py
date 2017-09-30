class van:

    def __init__(self, fcf, n, io):
        self.fcf = fcf
        self.n = n
        self.io = io

    def calculate(self, i):
        aux = 0
        for x in range(1, self.n):
            aux = aux + (self.fcf/pow(1+i, x))
        return self.io - aux