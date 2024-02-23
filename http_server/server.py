from socket import *
from threading import Thread
IP=gethostbyname(gethostname())
PORT=2344
s=socket(AF_INET,SOCK_STREAM)
s.bind((IP,PORT))
s.listen(3)
header="HTTP/1.1 200 OK\nConnection: Keep-Alive;\nContent-Type: text/html;\nContent-Length:"
print('Server Listening...')
d=b''
def file(q='./public/index.html'):
  f=open(q,'r')
  x=f.read()
  d=(header+str(len(x))+";\n\n").encode('utf-8')
  f.close()
  x=x.encode('utf-8')
  return x
def handle(client,addr):
  while True:
    req=client.recv(2048)
    print(req.decode())
    client.send(d)
    client.send(file())
    print(file().decode())
   
while True:
  data,addr=s.accept()
  t1=Thread(target=handle,args=(data,addr))
  t1.start()
