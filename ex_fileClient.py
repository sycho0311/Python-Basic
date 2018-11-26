import socket

HOST = 'localhost'
PORT = 9009

def getFileFromServer(filename):
    data_transferred = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))

        sock.sendall(filename.encode())
        message = filename.split()

        '''
        data = sock.recv(1024)
        if not data:
            print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생' % filename)
            return

        with open('C:/Users/USER/Desktop/Python-Basic/' + filename, 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)
        '''

        print('파일[%s] 전송 시작...' % message[1])
        with open(message[1], 'rb') as f:
            try:
                data = f.read(1024)  # 파일을 1024바이트 읽음
                while data:  # 파일이 빈 문자열일때까지 반복
                    data_transferred += sock.send(data)
                    data = f.read(1024)
            except Exception as e:
                print(e)

    print('파일[%s] 전송종료. 전송량 [%d]' % (filename, data_transferred))
    return

while True:
    filename = input('Input FileName to Transport:')

    getFileFromServer(filename)

    if filename == 'quit':
        break