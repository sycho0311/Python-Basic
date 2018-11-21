'''
try:
    f = open('foo.txt', 'r')
# Exception
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()
'''

'''
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")
except IndexError:
    print("IndexError")
'''

'''
try:
    f = open("None.txt", 'r')
except FileNotFoundError:
    pass
'''

# Intentional Error
# Must Implement
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

