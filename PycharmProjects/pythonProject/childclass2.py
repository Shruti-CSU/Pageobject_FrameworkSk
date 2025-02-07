from Oops import Test5


class childcx(Test5):
    num5 = 100

    def __init__(self):
        Test5.__init__(self, 10, 20)

    def m2(self):
        return self.num5 + self.c5()


print("end")

obj = childcx()
print(obj.m2())
