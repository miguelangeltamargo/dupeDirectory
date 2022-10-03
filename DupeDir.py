import os
from pathlib import Path
from natsort import natsorted
from tkinter import filedialog as fd
import getpass


user = getpass.getuser()
#dirA = '/Users/miguel/Desktop/Test Code/dupe/tryA'
print('Open the directory to be duped:')
#dirA = fd.askdirectory(initialdir='C:/Users/%s' % user)
dirA = input("Drag and Drop:(JK paste it)\n")
dirA = Path(dirA)
print(dirA)
#dirB = '/Users/miguel/Desktop/Test Code/dupe/tryB'
print('Open the directory to be changed:')
#dirB = fd.askdirectory(initialdir='C:/Users/%s' % user)
dirB = input("Drag and Drop:(JK paste it)\n")
dirB = Path(dirB)
print(dirB)

def getFile(dirA, dirB):
    
    #declaring list for dirA & dirB and appending all filepaths to list, excluding dotfiles
    fileA = [] #holds each folder path in dirA 
    for n in os.listdir(dirA):
        if not n.startswith('.'):
            newDirA = dirA / n
            fileA.append(newDirA)

    fileB = [] #holds each folder path in dirB
    for n in os.listdir(dirB):
        if not n.startswith('.'):
            newDirB = dirB / n
            fileB.append(newDirB)
            
    #naturally sorting  lists(not sure if needed but keep)
    fileA = natsorted(fileA)
    fileB = natsorted(fileB)
    
    #loop to create a list of each directory to hold directory file names and 
    dirAFiles = [] #holds each file names in the dir
    for file in fileA: #creates a list of each file name
        #fiName = Path(file)
        for each in file.iterdir():
            dirAFiles.append(str(each.name)) #adds filename to list and splits into format
            
    #appends the files of each dir to a list
    dirBFiles = [] #holds each file names in the dir
    for dir in fileB:
        for nextdir in dir.iterdir():
            dirBFiles.append(nextdir.name)
    
    j=0
    x=0
    while x<len(dirAFiles):
        aSplit = dirAFiles[x].split('. ')
        if aSplit[1] != dirBFiles[j]:
#           print('\tFail-Comparing: '+aSplit[1]+' & '+dirBFiles[j])
            j+=1
        else:
            print('\tPass-Comparing '+aSplit[1]+' & '+dirBFiles[j])
            os.chdir(fileB[0])
            newName = '. '.join(aSplit)
            os.rename(str(dirBFiles[j]), newName)
            j=0
            x+=1
            
                
        
getFile(dirA, dirB)
