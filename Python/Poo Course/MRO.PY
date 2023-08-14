#el MRO es el el orden en el que las funciones son priorizidas en el ambito de ejecucion
class A:
    def hablar(self):
        print("hi, I'm A")

class B(A):
    def hablar(self):
        print("Hi, I'm B ")
        
class C(A):
        pass
        
class D(B,C):
        pass
        
d = D()        

d.hablar()   



