class ImaginaryNumber:
    
    def __init__(self, re = 0, im = 0):
        self.re = re
        self.im = im

    def __add__(self, other):
        return self.re + other.re, self.im + other.im
    
    def __sub__(self, other):
        return  self.re - other.re, self.im - other.im
    
    def __mul__(self, other):
        return  self.re + other.re - self.im * other.im, self.re * other.im + self.im * other.re
    
    def __truediv__(self, other):
        n1 = (self.re * other.re + self.im * other.im)/(other.re**2 + other.im**2)
        n2 = (self.im * other.re - self.re * other.im)/(other.re**2 + other.im**2)
        return n1, n2
    
    def module(self):
        return (self.re**2 + self.im**2)**1/2

    def __str__(self):
        return(str(self.re) + ', ' + str(self.im)) 


