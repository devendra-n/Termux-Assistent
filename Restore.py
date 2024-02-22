try:
  f=open('db.json.back','r')
  x=f.read()
  f.close()
  f=open('db.json','w')
  f.write(x)
  f.close()
  print('Restore Succesfull')
except Exception as e:
  print('Unable to restore')
