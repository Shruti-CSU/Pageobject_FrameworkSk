from Oops import Test4, Test3, Test5


class childc(Test4):
    c1 = 155

    def __init__(self):
        Test4.__init__(self, 10, 20, 30)    #this is constuctore from parent class

    def m1(self):
        print("Method 1 from child class")

    def getdata(self):
        return self.c1 + self.var4 + self.sum04() #this will sum c1 from child class and var4 from paernt calss Test4


objc1 = childc()
print(objc1.getdata())
print(objc1.m1())

