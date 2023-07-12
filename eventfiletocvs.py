import sys
fileLines = []
cmdArgs = sys.argv

def saveToFile(fileName):
    fileName += 'csv'
    try:
        theFile = open(fileName, "w")
    except Exception as e:
        print('An error occurred:', e)
        return
    print("save to file")
    #print(theFile)
    for line in fileLines:
        theFile.write("%s\n" % line)
    theFile.close()


# do the magic to the line
def proceedTheLine(aLine,aNumber):
    if (' - - - - - Timer_ConnectionIdle -' not in aLine
            and '- - - - - Timer_MinBytesPerSecond -' not in aLine):
       if (aNumber > 2):
           #if (len(aLine.split(' ')) > 3):
               fileLines.append(aLine.replace(' ', ';').strip())
       else:
           fileLines.append(aLine)

# open the file, handle exeptions, and read lines in the file
def openFile(fname):
    lineNumber = 0
    print("reading the file " + fname)
    try:
        theFile = open(fname)
    except Exception:
        print('File does not exist')
        return
    for line in theFile:
        if (lineNumber < 4):
            if ('#Fields:' in line):
                line = line.lstrip('#Fields:')
                line = line.lstrip(' ')
            if ('#' in line):
                line = line.lstrip('#')
                line = line.lstrip(' ')

        proceedTheLine(line,lineNumber)
        lineNumber += 1

    theFile.close()
    # use the same file name 
    csvFile = fname.rsplit(fname[-3:])[0]
    saveToFile(csvFile)



# open files from arguments
def proceedArguments(someArgs):
    i = 1
    if (len(someArgs) > 1):
        while (i < len(someArgs)) :
            openFile(someArgs[i])
            fileLines.clear()
            i +=1
    else:
        print("This script needs filenames as an arguments to proceed. Exiting... ")


proceedArguments(cmdArgs)
