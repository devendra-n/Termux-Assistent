import requests
import wikipedia
from deep_translator import GoogleTranslator
import instaloader
from datetime import datetime
import os
import sys
import time
import subprocess
dk=datetime.now()
tm=dk.strftime('%I:%M %p')
#os.system('screenfetch')
query=subprocess.getoutput(['termux-speech-to-text'])
print('You said: ',query)
try:
  if query=='':
    subprocess.call(['termux-tts-speak',' सर, मैं आपके बोलने की प्रतीक्षा कर रहा हूं'])
  elif 'made' in query:
    subprocess.call(['termux-tts-speak',' सर मुझे देवेंद्र जी ने बनाया है|और , अभी भी वे मुझे डेवलप कर रहे है'])
  elif 'where am I' in query:
     subprocess.call(['termux-tts-speak',' O k sir,let me check'])
     bh='https://api.ipify.org/'
     op=requests.get(bh).text
     print(op)
  elif 'Instagram' in query:
     subprocess.call(['termux-tts-speak',' o k sir let me check']);
     os.system('termux-open https://instagram.com/devendra2073');
     time.sleep(5);
     subprocess.call(['termux-tts-speak',' क्या आप प्रोफाइल पिक्चर को डाउनलोड करना चाहते है'])
     condition=subprocess.getoutput('termux-speech-to-text');
     if 'yes' in condition:
         print('You said: ',condition)
         md=instaloader.Instaloader()
         md.download_profile('devendra2073',profile_pic_only=True)
         subprocess.call(['termux-tts-speak',' प्रोफाईल पिक्चर को मैने फाइल में सेव कर दिया है, सर अब मैं अगले टास्क के लिए रेडी हूं']);
     else:
      subprocess.call(['termux-tts-speak',' o k sir'])
      print('You said: ',condition)
  elif 'Facebook' in query:
    os.system('termux-open https://m.facebook.com/');
    time.sleep(7);
  elif 'how are you' in query:
    subprocess.call(['termux-tts-speak',' सर , आपकी खिदमत में हाज़िर'])
  elif 'time' in query:
    subprocess.call(['termux-tts-speak',tm])
  elif 'your name' in query or 'who are you' in query:
    subprocess.call(['termux-tts-speak',' सर मेरा नाम भार्गव है,और मैं आपका वाइस असिस्टेंट हूं'])
  elif 'temperature' in query:
    search='temperature in Lucknow'
    url="https://api.openweathermap.org/data/2.5/weather?q=Lucknow&appid=2338b0edd1fa04a3b81f650b4d56e114"
    r=requests.get(url);
    t=(r).json();
    fin=(t['main']['temp'])-273.15;
    fine=format(fin,'.2f');
    dl=str(fine)
    al='सर वर्तमान तापमान  '+dl+' अंश सेल्सियस है'
    subprocess.call(['termux-tts-speak',al]);
  elif 'exit' in query or 'bye' in query:
    subprocess.call(['termux-tts-speak',' Good bye sir,take care']);
    sys.exit();
  elif 'YouTube' in query:
    subprocess.call(['termux-tts-speak',' o k ,sir'])
    os.system('termux-open https://m.youtube.com')
  elif 'battery' in query:
    subprocess.call(['termux-tts-speak',' o k sir,wait,Getting deta from system'])
    os.system('termux-battery-status')
  elif 'WhatsApp' in query:
    subprocess.call(['termux-tts-speak',' o k sir'])
    os.system('termux-open https://chat.WhatsApp.com')
  elif 'age' in query:
    subprocess.call(['termux-tts-speak',' o k sir'])
    os.system('python age.py')
    sys.exit()  
  elif 'clear' in query:
    os.system('clear');
  elif 'blog' in query:
    os.system('termux-open https://dktechpoint.blogspot.com/');
  elif 'who am I' in query or 'mera naam' in query:
    subprocess.call(['termux-tts-speak',' सर जहां तक मैं जानता हूं ,आपका नाम मिस्टर देवेंद्र है']);
  elif 'ok' in query  or 'hey' in query or 'hello' in query:
    subprocess.call(['termux-tts-speak','  हैलो सर, मैं आपकी किस प्रकार सहायता कर सकता हूं'])  
  else:
    wiki=query.replace("wikipedia","");
    result=wikipedia.summary(wiki, sentences=2);
    translated = GoogleTranslator(source='auto', target='hi').translate(result);
    subprocess.call(['termux-tts-speak',' विकिपीडिया के अनुसार',translated]);
  os.system('python main.py');
except Exception as e:
  print(e);
  print('User has closed program or Somthing went wrong');
  print('Now you can run   dk');
