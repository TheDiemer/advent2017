#!/usr/bin/env python3
from sys import argv

try:
  b = int(argv[1])
except:
  print("NOPEEEE, {0} is not a number!".format(argv[1]))
  exit()
info = []
length = len(str(b))
for place1 in range(0,length):
  try:
    if (str(b)[place1] == str(b)[int(place1+(length/2))]):
      #"yes, because {0} is == to {1}".format(str(b)[list],str(b)[list+1])
      info.append(str(b)[place1])
    else:
      #"no, because {0} is != to {1}".format(str(b)[list],str(b)[list+1])
      pass
  except:
    if (str(b)[place1] == str(b)[int((place1+(length/2))-length)]):
      #"yes, because {0} is == to {1}".format(str(b)[list],str(b)[0])
      info.append(str(b)[place1])
    else:
      #"no, because {0} is != to {1}".format(str(b)[list],str(b)[0])
      pass
total = 0
for place2 in range(0,len(info)):
  total = total + int(info[place2])
print(total)
