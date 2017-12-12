#!/usr/bin/env python3
from sys import argv
import re

def start(arg):
  try:
    path = arg
  except:
    print("Please provide the full path to a file whereyou have put the spreadsheet you need to get the checksum of!")
    exit()
  
  main(path)

def main(path):  

  try:
    spreadsheet = open(path, "r")
  except:
    print("This needs to be a valid path to the spreadsheet you want the checksum of, and {0} is NOT a valid spreadsheet path!".format(path))
    exit()
  
  spreadLength = len(spreadsheet.readlines())
  spreadsheet = open(path,"r")
  individualLineNums = []
  sortedNums = []
  dividedDiff = []
  for full in range(0,spreadLength):
    line = spreadsheet.readline()
    for num in range(0,len(re.split(r'\t+', line))):
      try:
        individualLineNums.append(int(re.split(r'\t+', line)[num]))
      except:
        individualLineNums.append(int(re.split("\n",re.split(r'\t+', line)[num])))
    sortedNums = sorted(individualLineNums, reverse=True)
    for c in range(0,len(sortedNums)):
      for d in range(1,len(sortedNums)):
        if c == d:
          pass
        else:
          if evenDivide(sortedNums[c],sortedNums[d]) == True:
            dividedDiff.append(sortedNums[c]/sortedNums[d])
          else:
            pass
    sortedNums = []
    individualLineNums = []
  total = 0
  for check in range(0,len(dividedDiff)):
    total = total + dividedDiff[check]
  
  print("Your evenly divided checksum is: {0}".format(total))


def evenDivide(num1, num2):
  if (num1 % num2) > 0:
    return False
  else: 
    return True


start(argv[1])
