import socketserver
import threading
import pymysql

HOST = ''
PORT = 9009
lock = threading.Lock()  # syncronized 동기화 진행하는 스레드 생성

class UserManager:  # 사용자 관리 및 메세지 송수신을 담당하는 클래스

    def __init__(self):
        self.users = {}  # 사용자의 등록 정보를 담을 사전 {사용자 이름:(소켓,주소),...}

    def addUser(self, username, conn, addr):  # 사용자 ID를 self.users에 추가하는 함수

        if username in self.users:  # 이미 등록된 사용자라면
            conn.send('이미 등록된 사용자입니다.\n'.encode())
            return None

        # 새로운 사용자를 등록함
        lock.acquire()  # 스레드 동기화를 막기위한 락
        self.users[username] = (conn, addr)
        lock.release()  # 업데이트 후 락 해제

        '''    
        self.sendMessageToAll('[%s]님이 입장했습니다.' % username)
        print('+++ 대화 참여자 수 [%d]' % len(self.users))
        '''

        return username

    def removeUser(self, username):  # 사용자를 제거하는 함수
        if username not in self.users:
            return

        lock.acquire()
        del self.users[username]
        lock.release()

        '''
        self.sendMessageToAll('[%s]님이 퇴장했습니다.' % username)
        print('--- 대화 참여자 수 [%d]' % len(self.users))
        '''

    def messageHandler(self, username, msg):  # 수신 Message 처리하는 부분
        if msg.strip == '/file': # 수신 메세지가 'file'이면 클라이언트로부터 .json 파일을 수신
            return

        elif msg.strip == '/query':  # 수신 메세지가 'query'이면 클라이언트에게 번역문 전송
            # self.sendMessageToAll('[%s] %s' % (username, msg))
            # self.sendMessage(username, msg)
            return

        elif msg.strip() == '/quit':  # 수신 메세지가 'quit'이면 클라이언트 접속 해제
            self.removeUser(username)
            return -1

        else:
            self.sendMessage(username)

    '''
    접속한 클라이언트 전체 메세지 송신
    def sendMessageToAll(self, msg):
        
        for conn, addr in self.users.values():
            conn.send(msg.encode())
    
    '''

    def sendMessage(self, username):  # 메세지를 보낸 해당 사용자에게 답변
        user = self.users.get(username)
        conn = user[0]
        msg = 'Please proceed according to the usage.'

        # TODO
        '''
            수신한 메세지를 통해
            1. 파일을 수신할 것인지
            2. Query를 진행할 것인지
            3. 종료
        '''
        # print(msg)

        conn.send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()

    def handle(self):  # 클라이언트가 접속시 클라이언트 주소 출력
        print('IP Address : [%s] Connected' % self.client_address[0])

        try:
            # 클라이언트 등록
            username = self.registerUsername()
            # 클라이언트로부터 message 수신
            # message 크기 최대 1024
            usage = '* Usage *\n' + '1. File Transport : /file filename\n' + '2. Query : /query Target_Language sentence\n' + '3. Quit : /quit\n'
            self.request.send(usage.encode())
            msg = self.request.recv(1024)

            while msg:
                # print(msg.decode())
                if self.userman.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                self.request.send(usage.encode())
                msg = self.request.recv(1024)

        except Exception as e:
            print(e)

        print('[%s] 접속종료' % self.client_address[0])
        self.userman.removeUser(username)

    # 접속한 클라이언트를 등록하기 위함
    def registerUsername(self):
        while True:
            self.request.send('Input ID : '.encode())
            # 받아온 ID 처리
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.userman.addUser(username, self.request, self.client_address):
                return username

class TestServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def runServer():
    print('Test Server On')

    try:
        server = TestServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server Off')
        server.shutdown()
        server.server_close()

runServer()

