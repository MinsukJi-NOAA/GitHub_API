#!/usr/bin/env python3
import sys
import json

def func1():
  #data1 = json.load(sys.stdin)['workflow_runs']
  #print("inside function 1")
  #print(data[0]['id'])
  print('skip')

def func2():
  #data2 = json.load(sys.stdin)['workflow_runs']
  #print("inside function 2")
  print(data[1]['id'])


data = json.load(sys.stdin)['workflow_runs']

if sys.argv[1] == '1':
  #print("Calling function 1")
  func1()
elif sys.argv[1] == '2':
  #print("Calling function 2")
  func2()
else:
  print("Wrong argument")
