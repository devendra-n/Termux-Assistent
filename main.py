import subprocess as sb
import Responser
import random as rd
hot_words=['bye','exit','quit','break','goodbye']
def reply(query):
  res=Responser.bestMatch(query)
  fk=res[2][rd.randint(0,len(res[2])-1)]
  if res[1]<=20:
    return ("Sorry Sir , I am Currently Unable to Understand.",0)
  elif 20<res[1]<50:
    return ("I am res[2][rd.randint(0,len(res[2]))]not sure About My Answer But here is the answer "+fk,2)
  elif 50<=res[1]<80:
    return ('According to me '+fk,3)
  else:
    return (fk,4)
try:
  run=True
  while run:
    #query=sb.getoutput('termux-speech-to-text')
    query=input('Query: ')
    rep=reply(query)
    if rep[1]==0:
      for i in hot_words:
        if i in query:
          run=False
    else:
      print('Response:',rep[0])
    
except Exception as e:
  print('Error')