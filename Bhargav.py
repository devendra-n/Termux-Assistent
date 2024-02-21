import os
import sys
import time
import subprocess
import requests
from datetime import datetime
t=datetime.now()
h=datetime.now().hour
tm=t.strftime('%I:%M %p')
os.system('clear')
os.system('figlet -f banner BHARGAV')
os.system('echo "                          AI system"')
os.system('echo "                                     -Made by Devendra"')
os.system('mpv bhargav.mp3')
time.sleep(3)
os.system('clear')
os.system('figlet -f banner DEVENDRA')
time.sleep(1)

if h<11:
  subprocess.call(['termux-tts-speak','Good morning sir,,  I am bhargav  your virtual assistent'])
  subprocess.call(['termux-tts-speak',tm])
elif h>11 and h<16:
  subprocess.call(['termux-tts-speak','Good ofternoon sir  I am bhargav  your virtual assistent'])
  subprocess.call(['termux-tts-speak',tm])
elif h>16 and h<21:
  subprocess.call(['termux-tts-speak','Good evenig sir , I am bhargav  your virtual assistent'])
  subprocess.call(['termux-tts-speak',tm])
else:
  subprocess.call(['termux-tts-speak','Hello sir,  I am bhargav  your virtual assistent']) 
  subprocess.call(['termux-tts-speak',tm])
os.system('python main.py')  
