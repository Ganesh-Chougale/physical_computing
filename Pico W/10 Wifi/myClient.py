import socket as localSocket

serverIpAddress = '10.161.66.250' # found in first program terminal
serverListenerPort = 2222
serverConfig = (serverIpAddress, serverListenerPort)

bufferSize = 1024

UDPclient = localSocket.socket(localSocket.AF_INET, localSocket.SOCK_DGRAM)

while True:
    userInput = input('What is your color?: ')
    cmdEncoded = userInput.encode('utf-8')
    UDPclient.sendto(cmdEncoded, serverConfig)