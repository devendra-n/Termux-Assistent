import ast
dataset=[]
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

def Tokenizer(sentense):
  return sentense.split(' ')

def matcher(query,db):
  wt=0
  query=Tokenizer(query)
  db=Tokenizer(db)
  if(len(query)>len(db)):
    w=len(query)-len(db)
    wt=int(w*100/len(query))
  elif len(query)==len(db):
    wt=100
  else:
    w=len(db)-len(query)
    wt=int(w*100/len(db))
  i=0
  count=0
  for word in query:
    if (len(db)<i+1):
      break
    if word.upper()==db[i].upper():
      count+=1
    else:
      pass
    i+=1
  return({'level':int(count*100/len(query)),'weight':100-wt})

def bestMatch(que):
  level=0
  index=-1
  resp=[]
  for i in dataset:
    mtch=matcher(i['query'],que)
    index+=1
    if mtch['level']>=level:
        level=mtch['level']
        resp=i['res']
    else:
      pass
  return [index,level,resp]