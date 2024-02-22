import subprocess as sb
import Responser
from MathD import koro
from Badword_detector import Reporter
import random as rd
hot_words=['bye','exit','quit','break','goodbye']
def reply_(q):
  if Reporter(q)==88744:
    return reply(q)
  else:
    return [Reporter(q),2]
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
    
    mth=koro(query)
    if mth:
      sb.call(['termux-tts-speak',str(mth[0]+' is equal to '+str(mth[1]))])
      print('Answer:',mth[1])
    rep=reply_(query)
    if rep[1]==0:
      for i in hot_words:
        if i in query:
          run=False
          sb.call(['termux-tts-speak','Good Bye sir'])
          break
          
    else:
      print('Response:',rep[0])
      sb.call(['termux-tts-speak',rep[0]])
    
except Exception as e:
  print('Error',e)