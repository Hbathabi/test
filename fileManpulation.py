import json
import os.path
fileName = 'dataBase.json'

def openFile (fileName) :
    if not os.path.isfile(fileName):
        f = open(fileName, "w")      
        f.write('{\"data\":[]}')
        f.close()
    file= json.loads(open(fileName).read())
    return file

def saveFile (fileName , file) :
    newFile = open(fileName , 'w')
    json.dump(file,newFile)
    newFile.close()

# file = openFile(fileName)
# file["data"].append('hello')
# saveFile (fileName , file)