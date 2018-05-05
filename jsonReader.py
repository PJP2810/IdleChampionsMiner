'''
Created on 5 May 2018

@author: PJP2810
'''
import json
import os



# Load .json and .txt files from workingDir\cached_definitions\
def jsonRead(fileName, dirName):
    os.chdir(dirName)
    with open(fileName + '.json') as json_file:  
        data = json.load(json_file)
    os.chdir("..")
    return data

# Parse loaded .json file


'''
main_
'''

workingDirectory = "workingDir"
segmentDirectory = "workingDir\cached_definitions"

file = "cached_definitions"

test = jsonRead(file, workingDirectory)

os.chdir(segmentDirectory)
with open("test.json", "w") as outfile:
    json.dump(test, outfile, sort_keys=True)
os.chdir("..")









