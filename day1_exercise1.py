#!/usr/bin/env python3
from sys import argv

try:
  b = int(argv[1])
except:
  print("NOPEEEE, {0} is not a number!".format(argv[1]))
  exit()
info = []
for place1 in range(0,len(str(b))):
  try:
    if (str(b)[place1] == str(b)[place1+1]):
      #yes, because the number we are currently looking at is == to that current number + one
      info.append(str(b)[place1])
    else:
      #no, because the number we are currently looking at is != to that current number + one
      pass
  except:
    if (str(b)[place1] == str(b)[0]):
      #yes, because the number we are currently looking at is == to the first digit of the number
      info.append(str(b)[place1])
    else:
      #no, because the number we are currently looking at is != to the first digit of the number
      pass
total = 0
for place2 in range(0,len(info)):
  total = total + int(info[place2])
print(total)
