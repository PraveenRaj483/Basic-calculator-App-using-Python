import math
class c1:
    def add(self,a,b):
        return a+b
class c2:
    def sub(self,a,b):
        return a-b
class c3:
    def mul(self,a,b):
        return a*b
class c4:
    def div(self,a,b):
        return a/b
class c5:
    def log(self,a,b):
        return  math.log(a,b)
class c6:
    def cos(self,a):
        return  math.cos(a)
    
class calculation(c1,c2,c3,c4,c5,c6):
    def square(self,a,b):
        return a**b
    def min(self, h):
        return h*60
    def hour(self,m):
        return m/60
    def usd(self,r):
        return r/72.60
    def euro(self,e):
        return e/85.85 


CALCI=calculation()
value=print('''     +\n     -\n     /\n     *\n     **\n     log\n     cos\n     $\n     euro\n     min\n     hour\n''')
A=input("TYPE ANY SYMBOL:")
B=A.lower()
try:
    if (B=='+'):
        print(CALCI.add(int(input("ENTER VALUE:")),int(input("ENTER VALUE:"))))
    if (B=='-'):
        print(CALCI.sub(int(input("ENTER VALUE:")),int(input("ENTER VALUE:"))))
    if (B=='*'):
        print(CALCI.mul(int(input("ENTER VALUE:")),int(input("ENTER VALUE:"))))
    if (B=='/'):
        print(CALCI.div(int(input("ENTER VALUE:")),int(input("ENTER VALUE:"))))
    if (B=='**'):
        print(CALCI.square(int(input("ENTER VALUE:")),int(input("ENTER VALUE:"))))
    if (B=='log'):
        print(CALCI.log(int(input("ENTER VALUE:")),int(input("ENTER VALUE:"))))
    if (B=='cos'):
        print(CALCI.cos(int(input("ENTER VALUE:"))))
    if (B=='min'):
        print(CALCI.min(int(input("ENTER HOUR VALUE:"))))
    if (B=='hour'):
        print(CALCI.hour(int(input("ENTER MINUATE VALUE:"))))
    if (B=='$'):
        print(CALCI.usd(int(input("ENTER RUPEES VALUE:"))))
    if (B=='euro'):
        print(CALCI.euro(int(input("ENTER RUPEES VALUE:"))))
except Exception :
    print("PLEASE ENTER NUMBERS ONLY")





    
