'''
Created on 4 May 2018

@author: PJP2810
'''
# Imports
import os, datetime, json, csv

# Move to workingDirectory
os.chdir("workingDir")

now = datetime.datetime.now()
data = {}
hero_defines = []


# Read JSON file
with open('cached_definitions.json') as json_file:  
    data = json.load(json_file)

# Separate JSON segments
hero_defines = [x for x in data['hero_defines']]
with open('hero_defines.json', 'w') as outfile:
    json.dump(hero_defines, outfile, indent=True,sort_keys=True)

# Parse segment


# Format parsed segment


# Output formatted segment (as CSV?)
with open("champData.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random\nFinal random text")
