
class Test:
    varA = 150

    def fun(self):
        print("This is method under class")


object01 = Test()
object01.fun()
print(object01.varA)


print("******practice class 2********")

class Test2:
    Varb = "This is string"

    def fun01(self):
        print("Anything from method")

object02 = Test2()
object02.fun01()
print(object02.Varb)


print("********call with consructor*********")


class Test3:
    var3 = "This is class variable"

    def __init__(self):
        print("This is automatic init method, will call first automatically")

    def method3(self):
        print("This is method 01")

object03 = Test3()
object03.method3()
print(object03.var3)


print("******sum method with multiple objects")

class Test4:
    var4 = 105

    def __init__(self, x, y, z): #these are instance variable and value can be changes as per mentioned in objects
        self.fistno = x
        self.secondno = y
        self.thirdno = z
        print("This will run first as a defualt method")

    def fun04(self):
        print("This is the first method")

    def sum04(self):
        return self.fistno + self.secondno + self.thirdno + self.var4


object04 = Test4(10, 5, 20)
object04.fun04()
print(object04.sum04())

object041 = Test4(18, 15, 5) #objects can be multiple based on different values
object041.fun04()
print(object041.sum04())


print("*****Parent Clas 5*********")

class Test5:
    T5 = 50

    def __init__(self, a, b):
        self.A = a
        self.B = b

    def c5(self):
        return self.T5 + self.A + self.B

Obj5 = Test5(5, 5)
print(Obj5.c5())