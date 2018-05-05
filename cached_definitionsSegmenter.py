'''
Created on 5 May 2018

@author: PJP2810
'''
import json
import os

# Move to workingDirectory
os.chdir("workingDir")

# Read JSON file
with open('cached_definitions.json') as json_file:  
    data = json.load(json_file)

# Separate JSON segments
def segJSON(fullData, segment):
    
    segData = [x for x in fullData[str(segment)]]
    
    with open(str(segment)+'.json', 'w') as outfile:
        json.dump(segData, outfile, indent=True,sort_keys=True)
    return



segment = 'loot_defines'

segJSON(data, segment)

'''
TODO:

- Create array of desired segments
    hero_defines
    upgrade_defines
    loot_defines
    effect_defines
    upgrade_defines
        etc
- Loop through segmentArray calling segJSON
'''