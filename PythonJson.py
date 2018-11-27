import json
import ast
import codecs

import urllib.request
import csv

'''
class Json:
    def func1(self, **kwargs):
        self.str = kwargs

    def func2(self, kwargs):
        self.str = kwargs

json1 = Json()
# **kwargs key-value, dictionary
json1.func1(name='임꺽정', age=20)
print(json1.str)

j1 = {"name":"홍길동", "age":30}
json1.func2(j1)
print(json1.str)

# function json.dumps() dictionary to json string
print(json.dumps(json1.str, indent=2))
'''

# Json Function
# loads() read String, load() read File
'''
with codecs.open('C:/Users/USER/Desktop/Python-Basic/myinfo.json', 'r', 'utf-8') as f:
    data = json.load(f)

print(type(data))
print(data)

with open('C:/Users/USER/Desktop/Python-Basic/myinfo.txt', 'a') as f:
    d = json.dumps(data)
    f.write(d)
'''

'''    
print(data["name"])
print(data["age"])
'''

'''
with codecs.open('C:/Users/USER/Desktop/Python-Basic/member.json', 'r', 'utf-8') as f:
    data = json.load(f)

    for i in data:
        for info in data[i]:
            print(i, info)

with open('C:/Users/USER/Desktop/Python-Basic/member.txt', 'a') as f:
    for i in data:
        for info in data[i]:
            mem = "%s, %s\n" % (i, info)
            f.write(mem)
'''

'''
# test URL
url = "http://ip.jsontest.com"  

d = {'name': '홍길동', 'birth': '0525', 'age': 30}
# encode : string to bytes
params = json.dumps(d).encode("utf-8")
# url, data, header type
req = urllib.request.Request(url, data=params, headers={'content-type': 'application/json'})
response = urllib.request.urlopen(req)
# decode: bytes to string
print(response.read().decode('utf8')) 

# urllib.request.Request : when request & response not json string, json bytes
'''

'''
arr = []

with codecs.open('C:/Users/USER/Desktop/Python-Basic/name.json', 'r', 'utf-8') as f:
    data = json.load(f)

    print(len(data))

    for i in data:
        for info in data[i]:
            print(i, info)
'''
'''
dic = {}

msg = '{' + '\n\t' + '"kor": ["안녕", "안녕하세요", "잘가요", "잘했어", "한글과컴퓨터"],' + '\n\t' + '"eng": ["Hi", "Hello", "Good Bye", "Good Job", "Hancom"]' + '\n' + '}'

dic = ast.literal_eval(msg)

# dic = msg
print(dic)

with open('make.json', 'w', encoding="utf-8") as make_file:
    json.dump(dic, make_file, ensure_ascii=False, indent="\t")
'''

korean = list()
english = list()
language = {}

with codecs.open('make.json', 'r', 'utf-8') as f:
    data = json.load(f)

    for i in data:
        if i == 'kor':
            korean = data[i]
        elif i == 'eng':
            english = data[i]

for i in range(len(korean)):
    print(korean[i])
    print(english[i])

korean.insert(0, 'KOREAN')
english.insert(0, 'ENGLISH')

'''
with open('test_out.csv', 'a', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(korean)
    writer.writerow(english)
'''