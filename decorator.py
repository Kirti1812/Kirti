def plus_one(n):
    def add_one(n):
        return n+1

    result= add_one(n)
    return result*10
print(plus_one(5))

#OOPs-----

class Program:
    def show(self, ):
        print("Hello")
    def display(self, ):
        print("Kirti")
K= Program()
K.show()
K.display()


#Inheritence----


class A:
    def info(self):
        print("Multiple Inheritance")
A1=A()
class B():
    def infoB(self):
        print("Derived Class")
B1=B()
A1.info()
B1.infoB()
class C(A, B):
    def infoC(self):
        print("Inheritance")
C1=C()
C1.info()
C1.infoB()
C1.infoC()


class E:
    def info(self):
        print("Single Inheritance")
E1=E()
class D(E):
    def infoD(self):
        print("Derived Class")
D1=D()
D1.infoD()
E1.info()
D1.info()


