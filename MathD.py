x=['add','+','sub','-','multiply','*','divide','/','addition','+','subtract','-','squire','sq','power','sq']
def mth(q):
  for i in range(10):
    if str(i) in q:
      print(i)
def ind(q):
  axl=[]
  lst=[]
  num=0
  for i in range(len(q)):
    if q[i]=='1':
      axl.append((1,i))
    elif q[i]=='2':
      axl.append((2,i))
    elif q[i]=='3':
      axl.append((3,i))
    elif q[i]=='4':
      axl.append((4,i))
    elif q[i]=='5':
      axl.append((5,i))  
    elif q[i]=='6':
      axl.append((6,i))  
    elif q[i]=='7':
      axl.append((7,i))  
    elif q[i]=='8':
      axl.append((8,i))  
    elif q[i]=='9':
      axl.append((9,i))  
    elif q[i]=='0':
      axl.append((0,i))
  lst=[]
  index=[]
  data=[]
  num=0
  Act=False
  for i in axl:
    lst.append(i[0])
    index.append(i[1])
  for i in range(len(lst)):
    if Act:
      if index[i-1]+1==index[i]:
        num=num*10+lst[i]
        if i==len(lst)-1:
          data.append(num)
      else:
        data.append(num)
        num=0
        num=num*10+lst[i]
    else:
      num=num*10+lst[i]
      Act=True
  return data
def init(q):
  for i in range(0,len(x),2):
    if x[i] in q:
      g=ind(q)
      return [g,x[i+1]]
  return False
def koro(q):
  x=init(q+' the1')
  if not x:
    return False
  xlt=0
  gd=1
  word=''
  if x[1]=='+':
    for i in x[0]:
      xlt=xlt+i
      word=word+str(i)+' plus '
  elif x[1]=='-':
    xlt=x[0][1]-x[0][0]
    word=str(x[0][1])+' minus '+str(x[0][0])
  elif x[1]=='*':
    for i in x[0]:
      gd=gd*i
      word=word+str(i)+' multiply '
  elif x[1]=='sq':
    word='Squire of '+str(x[0])
    gd=x[0][0]*x[0][0]
  else:
    word=word+str(x[0][1])+' divided  by '+str(x[0][0])
    gd=x[0][1]/x[0][0]
  if x[1]=='*' or x[1]=='/' or x[1]=='sq':
    return [word,gd]
  else:
    return [word,xlt]

