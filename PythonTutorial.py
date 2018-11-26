# character type
"""
word = 'Python'
print(word[0])
word[42] -> index out of range
"""

# Number
# Operator
# +, -, *, **, %, //
'''
print(10 + 10)
print(10 - 10)
print(10 * 10)
print(10 ** 3)
print(10 % 3)
print(10 // 4)
'''

# Lists
"""
squares = [1, 4, 9, 16, 25]
print(squares)

# Append Lists
squares = squares + [36, 49, 64, 81, 100]
print(squares)

cubes = [1, 8, 27, 64, 125]
cubes.append(216)
print(cubes)
"""

# index (x, y]
"""
cubes = [1, 8, 27, 64, 125]
print(cubes[0:3])

letters = ['a', 'b', 'c', 'd', 'e']
print(letters[1:3])

letters[1:3] = ['B', 'C']
print(letters[1:3])
"""

# Print & String
'''
number1 = 10
number2 = "three"
number3 = "%d - 7 = %s" % (number1, number2)
print(number3)

print("Python", "PyCharm")
i = 256 * 256
print('The value of i is', i)
'''

# matrix
"""
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0][1])
"""

# while
"""
a1, a2 = 0, 1
while a1 < 100:
    print(a1, end=', ')
    a1, a2 = a2, a1 + a2
"""

# if
"""
x = int(input("Please enter an integer : "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')
"""

'''
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0: 
        result += n
print(result)
'''

# for
"""
words = ['cat', 'widow', 'defenestrate']
for w in words:
    print(w, len(w))
    
for i in range(1, 10):
    print(i, end=' ')
    
animals = ['cat', 'dog', 'cow']
print(animals[:])
"""

"""
for w in words[:]:
    if len(w) > 6:
        # word insert into index [x] // insert(x, word)
        words.insert(0, w)

print(words)
"""

# range
# range(stop) -> range object
# range(start, stop[, step]) -> range object
"""
for i in range(5):
    print(i)

range(0, 10, 3)
"""

"""
arr = ['mary', 'had', 'a', 'little', 'lamb']
## size of arr : len(arr)
for i in range(len(arr)):
    print(i, arr[i])
"""

'''
# n of range : 2 ~ 9
# x of range : 2 ~ n
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
'''

# Function
'''
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += result + i
    elif choice == "mul":
        result = 0
        for i in args:
            result = result * i
    return result

print(sum_mul('sum', 1,2,3,4,5,6))
'''

# Key - Value Parameter
'''
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1,2,3, name='foo', age=3)

# args = tuple, kwargs = dictionary
'''

# File I/O
'''
f = open('C:/Users/USER/Desktop/Python-Basic/write.txt', 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

'''
f = open('C:/Users/USER/Desktop/Python-Basic/write.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)

f.close()
'''

'''
with open('C:/Users/USER/Desktop/Python-Basic/write.txt', 'a') as f:
    for i in range(11, 21):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
'''

'''
s = '/file KorEng.json'

sentence = s.split()

print(sentence[0])

for i in sentence:
    print(i)
'''

'''
s = 'eng kor good job very good'
msg = s.split()

s = ''

for i in msg[2:len(msg)]:
    if i == msg[len(msg)-1]:
        s += i

    else:
        s += i + ' '
'''
