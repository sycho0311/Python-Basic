import socket
from threading import Thread

HOST = 'localhost'
PORT = 9009

def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            pass

def runChat():
    data_transferred = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True
        t.start()

        while True:
            msg = input()
            message = msg.split()

            if message[0] == '/quit':
                sock.send(msg.encode())
                break

            elif message[0] == '/file':
                filename = message[1]
                print(filename)

                sock.send(msg.encode())

                print('파일[%s] 전송 시작...' % filename)

                with open(filename, 'rb') as f:
                    try:
                        data = f.read(1024)  # 파일을 1024바이트 읽음
                        while data:  # 파일이 빈 문자열일때까지 반복
                            data_transferred += sock.send(data)
                            data = f.read(1024)
                    except Exception as e:
                        print(e)

                print('파일[%s] 전송종료. 전송량 [%d]' % (filename, data_transferred))

                break

            else:
                print(msg)
                sock.send(msg.encode())

runChat()