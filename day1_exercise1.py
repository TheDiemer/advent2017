#!/usr/bin/env python3
from sys import argv

try:
  b = int(argv[1])
except:
  print("NOPEEEE, {0} is not a number!".format(argv[1]))
  exit()
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
