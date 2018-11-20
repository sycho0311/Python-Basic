'''
class Calculator:
    def __init__(self, result):
        self.result = result

    def add(self, num):
        self.result += num
        return self.result

    def setData(self, first, second):
        self.first = first
        self.second = second
        print(self.first, self.second)

calc1 = Calculator(0)

print(calc1.add(3))
calc1.setData(10, 20)
print(calc1.first)

# Inheritance
class MultiCalculator(Calculator):
    def pow(self, first, second):
        self.result += first * second
        return self.result

    # Method Overriding
    def add(self, num):
        self.result += num + num
        return self.result

calc2 = MultiCalculator(30)

print(calc2.add(20))
print(calc2.pow(3, 5))
calc2.setData(20, 10)
print(calc2.first)
'''

class Num():
    num = 10
    def getterNum(self):
        return self.num

    def setterNum(self, num):
        self.num = num

num1 = Num()
print(num1.num)
print(num1.getterNum())
num1.setterNum(20)
print(num1.getterNum())
