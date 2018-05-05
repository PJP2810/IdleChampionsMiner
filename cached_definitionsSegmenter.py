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
hero_defines = [x for x in data['hero_defines']]

with open('hero_defines.json', 'w') as outfile:
    json.dump(hero_defines, outfile, indent=True,sort_keys=True)

upgrade_defines = [x for x in data['upgrade_defines']]

with open('upgrade_defines.json', 'w') as outfile:
    json.dump(upgrade_defines, outfile, indent=True,sort_keys=True)
