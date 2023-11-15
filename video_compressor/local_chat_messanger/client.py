import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/Users/seiyanamioka/python_practice/video_compressor/local_chat_messanger/socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = input('Type anything\n')
    sock.sendall(bytes(message, 'utf-8'))

    sock.settimeout(2)

    try:
        while True:
            data = str(sock.recv(32))

            if data:
                print('Server response: ' + data)
            else:
                break

    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()

