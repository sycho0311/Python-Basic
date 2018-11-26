import socketserver
import threading
import pymysql
import codecs
import json

# to Use SocketServer
# to Use Client syncronize
# to Connect MariaDB

HOST = ''
PORT = 9009
# create a thread to User's synchronize
lock = threading.Lock()

# Class : for user management and sending and receiving messages.
class UserManager(socketserver.BaseRequestHandler):

    JsonFile = 0

    def __init__(self):
        # User Info Dictionary {User ID:(socket, address), }
        self.users = {}

    # Add User ID to self.users
    def addUser(self, username, conn, addr):

        if username in self.users:  # Already used ID
            conn.send('Already a registered ID.\n'.encode())
            return None

        # new user ID
        # Lock to prevent thread synchronization
        lock.acquire()
        self.users[username] = (conn, addr)
        # Unlock after update
        lock.release()

        '''    
        self.sendMessageToAll('[%s]님이 입장했습니다.' % username)
        print('+++ 대화 참여자 수 [%d]' % len(self.users))
        '''

        return username

    # Delete user ID
    def removeUser(self, username):
        if username not in self.users:
            return

        lock.acquire()
        del self.users[username]
        lock.release()

        '''
        self.sendMessageToAll('[%s]님이 퇴장했습니다.' % username)
        print('--- 대화 참여자 수 [%d]' % len(self.users))
        '''

    # Parts to process receive message
    def messageHandler(self, username, msg):

        message = msg.split()

        # form of sentence : .json
        if message[0] == '/file':
            self.JsonFile += 1
            # print(message)
            return
            # print(msg)

        # form of sentence : query
        elif message[0] == '/query':
            language = message[1]
            target = message[2]
            sentence = ''

            for i in message[3:len(message)]:
                if i == msg[len(msg) - 1]:
                    sentence += i

                else:
                    sentence += i + ' '

            conn = pymysql.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')

            try:
                with conn.cursor() as curs:
                    sql = "select " + target + " from translation where " + language + " = %s"
                    # print(sql)
                    curs.execute(sql, sentence)
                    rs = curs.fetchone()
                    # print(rs)

                    if rs == None:
                        data = sentence + "is No translation data."

                    else:
                        data = sentence + "= " + rs[0]
                # print(data)


            finally:
                conn.close()

            self.sendMessage(username, data)

            return

        # Disconnect client if incoming message is 'quit'
        elif message[0] == '/quit':
            self.removeUser(username)
            return -1

        else:
            if self.JsonFile == 1:
                print(msg)

                with open('make.json', 'w', encoding="utf-8") as make_file:
                    json.dump(msg, make_file, ensure_ascii=False, indent="\t")

                self.JsonFile -= 1
            else:
                # print(msg)
                msg = 'Please proceed according to the usage.'
                self.sendMessage(username, msg)

        # self.sendMessageToAll('[%s] %s' % (username, msg))

    '''
    # Broad Cast
    def sendMessageToAll(self, msg):
        
        for conn, addr in self.users.values():
            conn.send(msg.encode())
    
    '''

    # Reply to the person who sent the message
    def sendMessage(self, username, msg):
        user = self.users.get(username)
        conn = user[0]

        # print(msg)

        conn.send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()
    ''' 
    def fileTransport(self, msg):
        # 수신 메세지가 '/file'이면 클라이언트로부터 .json or .txt 파일을 수신

        message = msg.split()
        data_transferred = 0
        filename = message[1]  # 파일이름 이진 바이트 스트림 데이터를 일반 문자열로 변환
        print(filename)

        # data = self.request.recv(1024)

        with open(filename, 'wb') as f:
            try:
                while True:
                    data = self.request.recv(1024)

                    if not data:
                        break

                    f.write(data)
                    data_transferred += len(data)
            except Exception as e:
                print(e)

        return
    '''

    def handle(self):
        # Client address output when client connects
        print('IP Address : [%s] Connection' % self.client_address[0])

        try:
            # Register Client
            username = self.registerUsername()
            # receive message from Client
            # message Buffer Size = 1024
            usage = '* Usage *\n' + '1. File Transport : /file filename\n'\
                    + '2. Query : /query Language_to_Translate Target_Language sentence\n'\
                    + '3. Quit : /quit\n'

            while True:
                # message = msg.decode()
                # message = message.split()

                # if message[0] == '/file':
                    # print(message)
                    # self.fileTransport(msg.decode())

                # print(msg.decode())

                # Send Usage
                self.request.send(usage.encode())
                msg = self.request.recv(1024)

                if self.userman.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break

        except Exception as e:
            print(e)

        print('IP Address : [%s] Connection termination' % self.client_address[0])
        self.userman.removeUser(username)

    # To register a connected client
    def registerUsername(self):
        while True:
            self.request.send('Input ID : '.encode())
            # 받아온 ID 처리
            username = self.request.recv(1024)
            username = username.decode().strip()

            if self.userman.addUser(username, self.request, self.client_address):
                return username

class SocketServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def runServer():
    print('Socket Server On')

    try:
        server = SocketServer((HOST, PORT), MyTcpHandler)
        # Ready to accept requests from clients
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server Off')
        server.shutdown()
        server.server_close()

# Run Server
runServer()

