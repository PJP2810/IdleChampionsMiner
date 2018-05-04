'''
Created on 4 May 2018

@author: PJP2810
'''
# Imports
import os, datetime, json

# Move to workingDirectory
os.chdir("workingDir")

now = datetime.datetime.now()
data = {}  

# Read JSON file
with open('cached_definitions.json') as json_file:  
    data = json.load(json_file)

# Back-up JSON with date
with open('cached_definitions ['+now.strftime("%Y-%m-%dT%H.%M")+'].json', 'w') as outfile:  
    json.dump(data, outfile, indent=True,sort_keys=True)
    

# Separate JSON segments


# Parse segment


# Format parsed segment


# Output formatted segment
with open("champData.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random\nFinal random text")
