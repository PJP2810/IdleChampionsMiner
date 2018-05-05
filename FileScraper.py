'''
Created on 5 May 2018

@author: PJP2810
'''
import os
import json



def writeSeg(data, segment):
    
    # Move to output directory
    os.chdir("cached_definitions")
    
    try:
        # Skip empty segments
        if data[segment] == []:
            os.chdir("..")  # Return to workingDirectory
            return
        elif isinstance(data[segment], int) or isinstance(data[segment], bool):   # Handle non-iterable int and bool segments
            with open(segment+".txt", "w") as outfile:
                outfile.write(segment + ":" + str(data[segment]))
        else:
            segData = [x for x in data[str(segment)]]
            with open(str(segment)+'.json', 'w') as outfile:
                json.dump(segData, outfile, indent=True,sort_keys=True)
    except:
        print("---Exception--- " + str(data[segment]) +"\n")
    
    # Return to workingDirectory
    os.chdir("..")
    return

def readJSON(fileName, dirName = None):
    if dirName is not None:
        os.chdir(dirName)
        
    with open(fileName + '.json') as json_file:  
        data = json.load(json_file)
        
    if dirName is not None:
        os.chdir("..")
    return data

def listSegments(data):
    
    segments = [x for x in data]    
    
    return segments


'''
main_
'''


os.chdir("workingDir")

file = "cached_definitions"

fullData = readJSON(file)

segNames = listSegments(fullData)

for x in segNames:
    writeSeg(fullData, x)



















