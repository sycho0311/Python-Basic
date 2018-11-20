import json
import codecs

'''
class Json:
    def func1(self, **kwargs):
        self.str = kwargs

    def func2(self, kwargs):
        self.str = kwargs

json1 = Json()

json1.func1(name='임꺽정', age=20)
print(json1.str)

j1 = {"name":"홍길동", "age":30}
json1.func2(j1)
print(json1.str)

print(json.dumps(json1.str, indent=2))
'''

# Json Function
# loads() read String, load() read File

with codecs.open('C:/Users/USER/Desktop/PythonSeminar/myinfo.json', 'r', 'utf-8') as f:
    data = json.load(f)

print(type(data))
print(data)

'''
json은 URL요청시 입출력 데이터로 많이 활용된다.

import json
import urllib.request

url = "http://ip.jsontest.com"  # URL

d = {'name': '홍길동', 'birth': '0525', 'age': 30}
params = json.dumps(d).encode("utf-8")  # encode: 문자열을 바이트로 변환
req = urllib.request.Request(url, data=params,
                             headers={'content-type': 'application/json'})
response = urllib.request.urlopen(req)
print(response.read().decode('utf8'))  # decode: 바이트를 문자열로 변환

위 예제는 http://ip.jsontest.com 이라는 URL에 json요청을 보내고 그 응답으로 json을 리턴받아 출력하는 예제이다.
아마도 위 예제를 수행하면 호출한 PC의 IP 주소가 출력될 것이다.
(참고. http://ip.jsontest.com 은 호출한 클라이언트의 아이피를 출력해 주는 테스트 서비스이다.)

urllib.request.Request 사용시 json문자열이 아닌 json 바이트 배열로 주고 받아야 한다는 점에 유의하자.

'''