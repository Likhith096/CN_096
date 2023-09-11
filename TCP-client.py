from socket import *
serverName='127.0.0.1'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input("\nEnter file name: ") # file name into sentence 

clientSocket.send(sentence.encode()) #Encode it and send
filecontents=clientSocket.recv(1024).decode() #Recieve by decoing as fileConents b
print('\nFrom Server:\n')
print(filecontents)
clientSocket.close()























