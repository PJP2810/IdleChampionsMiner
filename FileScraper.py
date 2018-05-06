'''
Created on 5 May 2018

@author: PJP2810
'''

# Function definitions
def writeSegments(data, segment):
    
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
                json.dump(segData, outfile, indent=True, sort_keys=True)
    except:
        print("---Exception--- " + json.dumps(segment) +"\n")
    
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

def sortUpgrades(fullUpgrades):

    # Loop through fullUpgrades
    for x in fullUpgrades:
        
        # Store {effect, hero_id, id, required_level, required_upgrade_id} to variables
        upgradeID = x['id']
        upgradeEffect = x['effect']
        upgradeHeroID = x['hero_id']
        upgradeRequiredID = x['required_upgrade_id']
        upgradeLevel = x['required_level']
        upgradeType = x['upgrade_type']
        
        
        # Save variables to dict based on hero_id
        #tempDict = []
        #tempDict.append({upgradeID, upgradeLevel, upgradeRequiredID, upgradeEffect, upgradeType})
        
        #print("\n\n" + str(tempDict))        
        
        
        #print("Hero: " + str(upgradeHeroID))
        
        
    #print("\n\n" + str(fullUpgrades))        
        
        # Add dictName to list
        
        
        # clear duplicates from list
        
        
        # iterate through list of names
        
            # output name dict to file 
        
    return



'''
main_
'''

import os
import json
import pandas as pd

os.chdir("workingDir")

fullData = readJSON("cached_definitions")

segNames = listSegments(fullData)

for x in segNames:
    writeSegments(fullData, x)
    
# Parse segment.json, write to file in usable format

upgrades = readJSON("upgrade_defines", "cached_definitions")

#print(json.dumps(upgrades, sort_keys=True, indent = True))
#print(len(upgrades))

#print(upgrades[0]['hero_id'])

#sortUpgrades(upgrades)

pd.DataFrame(upgrades).to_csv('out.csv', index=False)








