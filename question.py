def first(q):
  if 'do you'.upper() in q.upper():
    x=q.upper().replace('do you'.upper(),"")
    return [1,x]
  elif 'who is'.upper() in q.upper():
    x=q.upper().replace('who is'.upper(),"")
    return [2,x]
  elif 'are you'.upper() in q.upper():
    x=q.upper().replace('are you'.upper(),"")
    return [3,x]
  elif 'what is'.upper() in q.upper():
    x=q.upper().replace('what is'.upper(),"")
    return [4,x]
  elif 'how to'.upper() in q.upper():
    x=q.upper().replace('how to'.upper(),"")
  else:
    return [0,'Command Error']
