import json
import codecs
import urllib.request

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