badwords=['gandu','chutiya','idiot','bewkoof','madarchod','bahanchod','nonsense']
def Reporter(q):
  for i in badwords:
    if i in q:
      return 'Bad word Detected'
  return 88744