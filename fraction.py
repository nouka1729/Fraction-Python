class frac:
    bunsi=0
    bunbo=1
    def __init__(self,Bunsi,Bunbo=1):
        self.bunsi=Bunsi
        self.bunbo=Bunbo
    
    def to_string(self):
        return f"{self.bunsi}/{self.bunbo}"
    def __str__(self):
        return self.to_string()
    def to_double(self):
        return self.bunsi/self.bunbo
    def floor(self):
        return self.bunsi//self.bunbo
    def ceil(self):
        return (self.bunsi+self.bunbo-1)//self.bunbo
    def gcd(self,a,b):
        while b:a,b=b,a%b
        return a
    def reduct(self):
        if self.bunbo<0:
            self.bunbo=-self.bunbo;self.bunsi=-self.bunsi
        g=self.gcd(self.bunsi,self.bunbo)
        self.bunsi//=g
        self.bunbo//=g
    def __iadd__(self,other):
        if type(other)==int:
            self.bunsi+=self.bunbo*other
            self.reduct()
            return self
        elif type(other)==frac:
            self.bunsi=self.bunsi*other.bunbo+self.bunbo*other.bunsi
            self.bunbo=self.bunbo*other.bunbo
            self.reduct()
            return self
        else:raise TypeError()
    def __isub__(self,other):
        if type(other)==int:
            self.bunsi+=self.bunbo*other
            self.reduct()
            return self
        elif type(other)==frac:
            self.bunsi=self.bunsi*other.bunbo-self.bunbo*other.bunsi
            self.bunbo=self.bunbo*other.bunbo
            self.reduct()
            return self
        else:raise TypeError()
    def __imul__(self,other):
        if type(other)==int:
            self.bunsi*=other
            self.reduct()
            return self
        elif type(other)==frac:
            self.bunsi=self.bunsi*other.bunsi
            self.bunbo=self.bunbo*other.bunbo
            self.reduct()
            return self
        else:raise TypeError()
    def __itruediv__(self,other):
        if type(other)==int:
            self.bunbo*=other
            self.reduct()
            return self
        elif type(other)==frac:
            self.bunsi=self.bunsi*other.bunbo
            self.bunbo=self.bunbo*other.bunsi
            self.reduct()
            return self
        else:raise TypeError()
    def __add__(self,other):
        self+=other;return self
    def __sub__(self,other):
        self-=other;return self
    def __mul__(self,other):
        self*=other;return self
    def __truediv__(self,other):
        self/=other;return self
    
    def __lt__(self,other):
        if type(other)==int:return self.bunsi<other*self.bunbo
        elif type(other)==frac:return self.bunsi*other.bunbo<self.bunbo*other.bunsi
        raise TypeError()
    def __le__(self,other):
        if type(other)==int:return self.bunsi<=other*self.bunbo
        elif type(other)==frac:return self.bunsi*other.bunbo<=self.bunbo*other.bunsi
        raise TypeError()
    def __gt__(self,other):
        if type(other)==int:return self.bunsi>other*self.bunbo
        elif type(other)==frac:return self.bunsi*other.bunbo>self.bunbo*other.bunsi
        raise TypeError()
    def __ge__(self,other):
        if type(other)==int:return self.bunsi>=other*self.bunbo
        elif type(other)==frac:return self.bunsi*other.bunbo>=self.bunbo*other.bunsi
        raise TypeError()
    def __eq__(self,other):
        if type(other)==int:return self.bunsi==other*self.bunbo
        elif type(other)==frac:return self.bunsi*other.bunbo==self.bunbo*other.bunsi
        raise TypeError()
    def __ne__(self,other):
        if type(other)==int:return self.bunsi!=other*self.bunbo
        elif type(other)==frac:return self.bunsi*other.bunbo!=self.bunbo*other.bunsi
        raise TypeError()
    

n=int(input())
d=[]
for i in range(n):
    a,b=map(int,input().split())
    d.append((frac(-a,a+b),i+1))
d.sort()
print(" ".join([str(i[1])for i in d]))
