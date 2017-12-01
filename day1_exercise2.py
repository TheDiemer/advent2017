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
      #yes, because the number we are currently looking at is == to that current number + the length of the list divided by 2
      info.append(str(b)[place1])
    else:
      #no, because the number we are currently looking at is != to that current number + the length of the list divided by 2
      pass
  except:
    if (str(b)[place1] == str(b)[int((place1+(length/2))-length)]):
      #yes, because the number we are currently looking at is == to (that current number + the length of the list divided by 2) - the full length of the list
      info.append(str(b)[place1])
    else:
      #"no, because the number we are currently looking at is != to (that current number + the length of the list divided by 2) - the full length of the list
      pass
total = 0
for place2 in range(0,len(info)):
  total = total + int(info[place2])
print("\nYour answer is: {0}".format(total))
