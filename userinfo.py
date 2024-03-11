import ast
def write(key,value='Unknown'):
  profarma={}
  try:
    try:
       f=open('userinfo.txt','r')
       profarma=ast.literal_eval(f.read())
       f.close()
       profarma[key]=value
    except:
      profarma[key]=value
    x=open('userinfo.txt','w')
    x.write(str(profarma))
    x.close()
    return True
  except Exception as e:
    return e
def read(key):
  try:
    x=open('userinfo.txt','r')
    data= (True,ast.literal_eval(x.read())[key])
    x.close()
    return data
  except Exception as e:
    return e
def init():
  bio=[['Your Name','name'],['Date Of Birth','dob'],['Your Gender','gen']]
  for i in bio:   
    dt=write(i[1],input('Please Enter '+i[0]+': '))
init()