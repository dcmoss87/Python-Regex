import re
import glob
from pathlib import Path
import pyinputplus as pyin

def allCaps(myStr, fileName):
    wordsAllCaps = re.compile(r'\b[A-Z]+\b')
    searchObj1 = wordsAllCaps.findall(myStr)
    print(f'\n{fileName}: ' + ', '.join(searchObj1))

def twelveChars(myStr, fileName):
    numChars = re.compile(r'\w{12,}')
    searchObj2 = numChars.findall(myStr)
    print(f'\n{fileName}: ' + ', '.join(searchObj2))

def stemForg(myStr, fileName):
    forgWord = re.compile(r'[f|F]org\w+')
    searchObj3 = forgWord.findall(myStr)
    print(f'\n{fileName}: ' + ', '.join(searchObj3))

def contVine(myStr, fileName):
    vineWord = re.compile(r'[v|V]ine\w*')
    searchObj4 = vineWord.findall(myStr)
    print(f'\n{fileName}: ' + ', '.join(searchObj4))

if __name__ == "__main__":
    choice = 0

    #p = Path.home()/'bible' Use this if file is stored in the user subdirectory. ex. C:\Users\User_Name\bible
    p = Path.cwd()/'bible' #Otherwise use this if the file is located in the current working directory.
    pathList = []
  
    for fileName in p.glob('*.txt'):
        pathList.append(fileName)
    
    while choice != 5:
        print('1. Display All Caps Words\n2. Display Words That Have at Least 12 Characters\n3. Display Words that Start with F/forg\n4. Display Words that Start with V/vine\n5. Exit')
        choice = pyin.inputInt("Enter a Choice: ", max = 5)
        
        if choice == 1:
            for fileName in pathList:
                myFile = open(fileName)
                readFile = myFile.read()
                allCaps(readFile, fileName.name)
            myFile.close()
    
        if choice == 2:
            for fileName in pathList:
                myFile = open(fileName)
                readFile = myFile.read()
                twelveChars(readFile, fileName.name)
            myFile.close()
        
        if choice == 3:
            for fileName in pathList:
                myFile = open(fileName)
                readFile = myFile.read()
                stemForg(readFile, fileName.name)
            myFile.close()
        
        if choice == 4:
            for fileName in pathList:
                myFile = open(fileName)
                readFile = myFile.read()
                contVine(readFile, fileName.name)
            myFile.close() 
        
    if choice == 5:
        print('Goodbye!')
        exit()