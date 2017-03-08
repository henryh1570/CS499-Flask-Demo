
# Append a string to newline of file
def fileAppend(fileName, str) :
    target = open(fileName, 'a')
    target.write('\n' + str)
    target.close()
    return

# Restore the file to this default
def fileReset(fileName) :
    target = open(fileName, 'w')
    target.write('10,0,1,18:8\n10,0,2,9:7\n10,1,1,13:5\n5,0,1,15:6\n5,1,5,16:9\n5,1,6,18:9')
    target.close()
    return

# Read and print all lines from file
def fileRead(fileName) :
    with open(fileName) as fp:
        for line in fp:
            print line.strip('\n')
    return

# Extract lines into array
def fileToArr(fileName) :
    arr = []
    with open(fileName) as fp:
        for line in fp:
            arr.append(line.strip('\n'))
    return arr

# Clear all data from a file
def fileClear(fileName) :
    target = open(fileName, 'w')
    target.write('')
    return

# Turn String arr to 2D int array inputs
def dataToInputArr(fileArr):
    arr = []
    for line in fileArr:
        value_arr = []
        target = str(line).split(':')[0]
        values = target.split(',')

        for element in values:
            value_arr.append(int(element))
        arr.append(value_arr)
    return arr

# Turn String arr to 2D int array outputs
def dataToOutputArr(fileArr):
    arr = []
    for line in fileArr:
        target = str(line).split(':')[1]
        arr.append(int(target))
    return arr