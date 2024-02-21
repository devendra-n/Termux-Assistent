import subprocess as sb
import Responser
try:
  #query=sb.getoutput('termux-speech-to-text')
  query=input('Query: ')
  print(Responser.bestMatch(query))
except:
  print('Error')