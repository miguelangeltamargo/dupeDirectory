import os
from natsort import natsorted


# dirA = input('Enter the directory you want duped:\n');
dirA = '/Users/miguel/Downloads/learn/Node:JS/Code With Mosh - The Complete Node.js Course'
# ext = input('Enter the extensions you want to check. (Press Enter to skip):\n')
# dirB = input("Enter the directory where you will dupelicate 'too':\n")
dirB = '/Users/miguel/Downloads/learn/Node:JS/Code With Mosh - Node.js The Complete Guide to Build RESTful APIs'
while True:
	c = input("Enter a choice:")
	if c == '1':
		print('DirA:')
		for f in sorted(os.listdir(dirA)):
			if not f.startswith('.'):
				print(f)
		print('DirB:')
		for f in sorted(os.listdir(dirB)):
			if not f.startswith('.'):
				print(f)
	
	elif c == '2':

		#for f in sorted(os.scandir(dirA), key=lambda e: e.name):
		for f in sorted((os.scandir(dirA))):
			print(f)


	elif c == 'q':
		exit()
