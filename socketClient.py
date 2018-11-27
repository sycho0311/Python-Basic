# import threading
# from threading import Thread
# import codecs
# import json
import socket

class FileManager:  # ##싱글턴을 쓴다면? 아니면 다른 방법?
    @staticmethod
    def get_path(filename, ext):
        path = './{ext}/{filename}.{ext}'.format(ext=ext, filename=str(filename))
        return path

class Client:
    HOST = '172.30.4.176'
    PORT = 9009
    BUF_SIZE = 1024
    TAG_SYSTEM = '<system>'
    EXT_JSON = 'json'
    JsonFile = 0

    # 생성자 : 소켓 생성-연결-테스트메시지 송수신-Loop 시작
    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            self.sock.connect((Client.HOST, Client.PORT))
            """
            t = Thread(target=self.recv_msg, args=())
            t.daemon = True
            t.start()
            """
            # ID --- (for test)############
            # Input ID string
            ## self.recv_msg()
            ## id_str = str(input())
            # Send ID string
            ##self.sock.send(id_str.encode())
            ##############################
            self.main_loop()

    # 서버로부터 메시지 수신 후, 콘솔에 출력
    def recv_msg(self):
        try:
            data = self.sock.recv(Client.BUF_SIZE)

            if data:
                if self.JsonFile == 1:
                    self.JsonFile = 0
                    return
                print(Client.TAG_SYSTEM, data.decode())
        except:
            pass

    # Main Loop
    def main_loop(self):  # ##좋지 않은 코드가 아닌가...
        while True:
            # Get Usage
            self.recv_msg()

            # Input Command str
            input_str = str(input())
            self.sock.send(input_str.encode())

            # Split Command str into list
            input_list = input_str.split(' ')
            cmd_data = input_list[0]

            if len(input_list) > 1:
                # COMMAND############################
                # JSON transfer
                if cmd_data == '/file':
                    path = FileManager.get_path(input_list[1], Client.EXT_JSON)
                    self.send_file(path)
                    self.JsonFile += 1
                    self.recv_msg()
                # query
                elif cmd_data == '/query':
                    #Get result of query
                    self.recv_msg()
            # quit
            elif cmd_data == '/quit':
                break
            # wrong command
            else:
                # Get wrong command msg
                self.recv_msg()
                continue
            #####################################

    # 서버에 rb 모드로 파일 전송 (BUF_SIZE 단위)
    def send_file(self, path):
        try:
            with open(path, 'rb') as f:
                data = f.read(Client.BUF_SIZE)
                while data:
                    self.sock.send(data)
                    data = f.read(Client.BUF_SIZE)
        except FileNotFoundError:
            print('File Not Found')


# START
client = Client()



"""
#2. open json
def OpenJSON(filename):
    path = './json/' + str(filename) + '.json'

    try:
        with codecs.open(path, 'r', 'utf-8') as f:
            data = json.load(f)
            print(type(data), data)
            return data

    except FileNotFoundError:
        print('File Not Found')
"""

