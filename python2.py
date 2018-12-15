#Reading and writing files

f = open('test.txt', 'r') #Open file for reading

print(f.name)
print(f.mode)

f.close() #Close file

with open('test.txt', 'r') as f: #Context manager, will auto-close file
	f_contents = f.read()
	print(f_contents)
	
	
print(f.closed) #File was closed automatically


with open('test.txt', 'r') as f: 
	print(f.readlines())
	
with open('test.txt', 'r') as f: 
	print(f.readline())

with open('test.txt', 'r') as f: 
	for line in f:
		print(line, end='')
	
with open('test.txt', 'r') as f:
	f_contents = f.read(100)
	print(f_contents, end='')
	

with open('test.txt', 'r') as f: #Print 10 chars at a time until EOF
	size_to_read = 10
	f_contents = f.read(size_to_read)
	
	while len(f_contents) > 0:
		print(f_contents, end='*')	
		f_contents = f.read(size_to_read)
	

	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end='')
	
	f.seek(0) #Go back to the beginning
	
	f_contents = f.read(size_to_read)
	print(f_contents)
	

# ~ with open('test2.txt', 'w') as f:
	# ~ f.write('Test')
	# ~ f.seek(0) #Go back to the beginning
	# ~ f.write('Test') #Overwrite the same thing
	
	
with open('test.txt', 'r') as rf: 	
	with open('test_copy.txt', 'w') as wf: 		
		for line in rf:
			wf.write(line)
		
		
with open('doggo.jpg', 'rb') as rf: 	
	with open('doggo_copy.jpg', 'wb') as wf: 		
		for line in rf:
			wf.write(line)		
		
with open('doggo.jpg', 'rb') as rf: 	
	with open('doggo_copy.jpg', 'wb') as wf: 		
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)	
		
		
		
		

