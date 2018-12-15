#The OS module

import os

print(dir(os)) #Shows all module methods

print(os.getcwd()) #Print current working directory

os.chdir('/home/matt/Desktop')

print(os.getcwd()) #Change current working directory

os.chdir('/home/matt/Desktop/Python3')

print(os.getcwd())
