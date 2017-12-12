#!/usr/bin/env python3
from sys import argv
import re

try:
  path = argv[1]
except:
  print("Please provide the full path to a file whereyou have put the spreadsheet you need to get the checksum of!")
  exit()

try:
  spreadsheet = open(path, "r")
except:
  print("This needs to be a valid path to the spreadsheet you want the checksum of, and {0} is NOT a valid spreadsheet path!".format(path))
  exit()

spreadLength = len(spreadsheet.readlines())
spreadsheet = open(path,"r")
individualLineNums = []
differenceNums = []
for full in range(0,spreadLength):
  line = spreadsheet.readline()
  for num in range(0,len(re.split(r'\t+', line))):
    try:
      individualLineNums.append(int(re.split(r'\t+', line)[num]))
    except:
      individualLineNums.append(int(re.split("\n",re.split(r'\t+', line)[num])))
  differenceNums.append(max(individualLineNums)-min(individualLineNums))
  individualLineNums = []
total = 0
for check in range(0,len(differenceNums)):
  total = total +differenceNums[check]

print("Your checksum is: {0}".format(total))
