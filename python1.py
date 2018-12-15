#The OS module

import os

print(dir(os)) #Shows all module methods

print(os.getcwd()) #Print current working directory

os.chdir('/home/matt/Desktop')

print(os.getcwd()) #Change current working directory

os.chdir('/home/matt/Desktop/Python3')

print(os.getcwd())

print(os.listdir('/home/matt/Desktop')) #List directories in folder

os.mkdir('OS-Demo-2') #Make a directory
os.makedirs('OS-Demo-3/Sub-Dir-1') #Make multiple levels at once

os.rmdir('OS-Demo-2') 
os.removedirs('OS-Demo-3/Sub-Dir-1') 

os.rename('test.txt', 'demo.txt')
os.rename('demo.txt', 'test.txt')

print(os.stat('test.txt')) #Statistics about file test.txt

from datetime import datetime

mod_time = os.stat('test.txt').st_mtime

print(datetime.fromtimestamp(mod_time))


for dirpath, dirnames, filenames in os.walk('/home/matt/Desktop'):
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

print(file_path)

print(os.path.basename('/home/matt/test.txt'))
print(os.path.dirname('/home/matt/test.txt'))
print(os.path.split('/home/matt/test.txt'))
print(os.path.exists('/home/matt/test.txt'))

print(os.path.isdir('/home/matt'))
print(os.path.isfile('/home/matt'))

print(dir(os.path))









