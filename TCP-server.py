from socket import *
serverName="127.0.0.1"
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
while 1:
    print("The serve is ready to receive")
    connectionSocket,addr = serverSocket.accept()   # accept from client
    sentence=connectionSocket.recv(1024).decode()   # decode

    file=open(sentence,"r") # file -> opened the filename given in sentence
    l=file.read(1024) # l -> content of file

    connectionSocket.send(l.encode())
    print('\nSent contents of '+sentence)
    file.close()
    connectionSocket.close()