badwords=['gandu','chutiya','chutiye','idiot','bewkoof','madarchod','bahanchod','nonsense','bhosadi','bhosadike','bhosdike','bhosdi','bhosdiwale']
def Reporter(q):
  for i in badwords:
    if i.upper() in q.upper():
      return 'Bhosdike gandu machchhar ki jhaant chutiye gaali deta hai'
  return 88744