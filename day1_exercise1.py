b =
info = []
for list in range(0,len(str(b))):
  try:
    if (str(b)[list] == str(b)[list+1]):
      #"yes, because {0} is == to {1}".format(str(b)[list],str(b)[list+1])
      info.append(str(b)[list])
    else:
      #"no, because {0} is != to {1}".format(str(b)[list],str(b)[list+1])
      pass
  except:
    if (str(b)[list] == str(b)[0]):
      #"yes, because {0} is == to {1}".format(str(b)[list],str(b)[0])
      info.append(str(b)[list])
    else:
      #"no, because {0} is != to {1}".format(str(b)[list],str(b)[0])
      pass

total = 0
for place in range(0,len(info)):
  total = total + int(info[place])

print(total)
