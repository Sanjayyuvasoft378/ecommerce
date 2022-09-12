import socket
import sys
try:
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created successfully")
except Exception as e:
    print("error occured",e)
port = 80
try:
    ip = socket.gethostbyname('www.facebook.com')
except Exception as e:
    print("something goes wrong")
skt.connect((ip,port))
print("socket connected to the facebook")

