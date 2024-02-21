import ast
from Responser import bestMatch
dataset=[]
filename='db.json'
def readDb(filename):
  try:
    f=open(filename,'r')
    data=f.read()
    f.close()
    data=ast.literal_eval(data)
    return data
  except:
    print('DBS File is missing...')
if not dataset:
  dataset=readDb('db.json')

def put(question,answer):
  f=open(filename,'r')
  x=f.read();
  f.close()
  data=ast.literal_eval(x)
  f=open(filename,'w')
  bst=bestMatch(question)
  print(bst)
  if bst[1]>=70:
    conf=input('Found a Similar Sentense Do you Want to merge ?: ')
    if conf.upper()=='Y':
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
