class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def setData(self, first, second):
        self.first = first
        self.second = second

calc1 = Calculator()

print(calc1.add(3))
calc1.setData(10, 20)

print(calc1.first)

class MultiCalculator(Calculator):
    pass

calc2 = MultiCalculator()
print(calc2.add(20))
