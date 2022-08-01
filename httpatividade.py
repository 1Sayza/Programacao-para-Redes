"""
    python3 httpatividade.py <HOST> <PORT> <RESOURCE> -o <OUTPUT_FILE> [-p <DATA> | -f <FILE>]
               0               1      2        3      4    5            6    7   |  6     7
"""

import socket, time
import sys
import ssl 

posicao = sys.argv 

print(sys.argv)

SERVER_NAME = (posicao[1])  #httbin.org
PORT = int(posicao[2]) #80
CMD = posicao[3] # metodo GET ou POST
arqsaida = posicao[5]
dados = posicao[7]


def createSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_NAME, PORT))
    return sock
 
def createSocketSSL():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_NAME, PORT))
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    return context.wrap_socket(sock, server_hostname=SERVER_NAME)


def sendHTTPCommand(cmd, sock):
    HTTP_CMD = ("GET "+cmd+" HTTP/1.1\r\n"+
                "Host: "+SERVER_NAME +"\r\n" +
                "\r\n")
    sock.sendall(HTTP_CMD.encode())

def getBodyContentLen(body, lenBody, sock):
    while len(body) < lenBody:
        body += sock.recv(4096)
    return body

def getBodyChunked(response, sock):
    posNL = response.find(b"\r\n")
    lenChunk = int (response[:posNL], 16)
    response = response[posNL+2:]

    while len(response) < lenChunk:
        response += sock.recv(4096)
    body = response[:lenChunk]

    return body

def getResponse(sock):
    buffer = sock.recv(4096)
    pos2NL = buffer.find(b"\r\n\r\n")
    headers = buffer[:pos2NL]
    body = buffer[pos2NL+4:]

    print ("Headers:", headers.decode())

    for header in headers.split(b"\r\n"):
        if header.startswith(b"Content-Length:"):
            lenBody = int(header.split(b":")[1])
            body = getBodyContentLen(body, lenBody ,sock)
            break
        elif header.startswith(b"Transfer-Encoding:"):
            body = getBodyChunked(body)
            break
    return body

def saveBody(fileName, body):
    fd = open (fileName, "wb")
    fd.write(body)
    fd.close()

if len(posicao) != 6 or sys.argv[4] != "-o":
    print('python3 httatividade.py <host> <porta> -o <resource>')

else:
    if PORT == 80:
        sock = createSocket()
        sendHTTPCommand(CMD, sock)
        body = getResponse(sock)
        sock.close()
        saveBody(f"{arqsaida}", body)

    elif PORT == 443:
        sock = createSocketSSL()
        sendHTTPCommand(CMD, sock)
        body = getResponse(sock)
        sock.close()
        saveBody(f"{arqsaida}", body)

