from socket import *
import subprocess
from threading import Thread
ip=gethostbyname(gethostname())
port=1233
s=socket(AF_INET,SOCK_STREAM)
s.bind((ip,port))
s.listen(1)
def handle(client,addr):
  client.send(b'Remote Connected...\r\n$ ')
  pwd=''
  cmd=''
  def back(path):
    actpath=''
    path=path.split('/')
    for i in range(len(path)-2):
      actpath+=path[i]+'/'
    print(actpath)
    return actpath
  while True:
    x=client.recv(2048).decode('utf-8')
    if 'cd' in x:
      if '..' in x:
        try:
          if pwd.split('/')[1]=='':
            pwd+=str(x.split(' ')[1]+'/')
          else:
            pwd=back(pwd)
        except:
          pwd+=str(x.split(' ')[1]+'/')
      else:
        pwd+=str(x.split(' ')[1]+'/')
      pwd=pwd.replace('\n','')
      client.send((pwd+' $ ').encode())
      continue
    if pwd=='':
      cmd=x
    else:
      cmd='cd '+pwd+' && '+x
    d=subprocess.getoutput(cmd)
    error0='/data/data/com.termux/files/usr/bin/sh: 1:'
    error1=': not found'
    if error0 in d and error1 in d:
      d=d.replace(error0,'').replace(error1,'')
      d=d+' command not Found'
    client.send((d+'\n'+pwd+' $ ').encode())
while True:
  client,addr=s.accept()
  handle(client,addr)
  