import ast
import sys
from Responser import bestMatch
dataset=[]
filename='db.json'
def defaultwrite(file):
    f=open(file,'w')
    f.write('[]')
    f.close()
    return '[]'
def readDb(filename):
  try:
    f=open(filename,'r')
    data=f.read()
    f.close()
    if not data:
      data=defaultwrite(filename)
    data=ast.literal_eval(data)
    return data
  except:
    print('DBS File is missing...',e)
if not dataset:
  dataset=readDb('db.json')
  
def put(question,answer,insert_mode=False):
  f=open(filename,'r')
  x=f.read();
  f.close()
  if not x:
    x=defaultwrite(filename)
  
  data=ast.literal_eval(x)
  f=open(filename,'w')
  bst=bestMatch(question)
  if bst[1]>=80:
    conf=''
    if not  insert_mode:
      conf=input('Found a Similar Sentense Do you Want to merge ?: ')
    if conf.upper()=='Y' or insert_mode:
      data[bst[0]]['res'].append(answer)
      f.write(str(data))
      f.close()
    else:
      data.append({'query':question,'res':[answer]})
      f.write(str(data))
      f.close()
  else:
    data.append({'query':question,'res':[answer]})
    f.write(str(data))
    f.close()
    
def copy(file):
  f=open(file,'r')
  x=f.read()
  f.close()
  f=open(file+'.back','w')
  f.write(x)
  f.close()
def input_mode():
  try:
    while True:
      x=input('Enter Your Question: ')
      if x=='quit':
        break
      else:
        ans=input('Enter Your Answer: ')
        put(x,ans)
  except Exception as e:
    print('Training Error...\n',e)
def init():
  argument=sys.argv
  if len(argument)>=3:
    if argument[1].upper()=='-F':
      f=open(argument[2],'r')
      data=f.read().split(',')
      copy(filename)
      for i in range(0,len(data),2):
        put(data[i],data[i+1],True)
      print('Data Insertion Sucess')
  else:
    input_mode()
init()