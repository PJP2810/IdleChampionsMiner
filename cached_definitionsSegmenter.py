'''
Created on 5 May 2018

@author: PJP2810
'''
import json
import os

# Move to workingDirectory
os.chdir("workingDir")

# Separate JSON segments
def writeSeg(fullData, segment):
    
    # Move to output directory
    os.chdir("cached_definitions")
    
    try:
        # Skip empty segments
        if data[segment] == []:
            os.chdir("..")  # Return to workingDirectory
            return
        elif isinstance(data[i], int) or isinstance(data[segment], bool):   # Handle non-iterable int and bool segments
            with open(segment+".txt", "w") as outfile:
                outfile.write(segment + ":" + str(data[segment]))
        else:
            segData = [x for x in fullData[str(segment)]]
            with open(str(segment)+'.json', 'w') as outfile:
                json.dump(segData, outfile, indent=True,sort_keys=True)
    except:
        print("---Exception--- " + str(data[segment]) +"\n")
    
    # Return to workingDirectory
    os.chdir("..")
    return

'''
main_
'''

# Read JSON file
with open('cached_definitions.json') as json_file:  
    data = json.load(json_file)

# Create list of desired segments
segments = ['hero_defines', 'upgrade_defines', 'loot_defines']

# Iterate through segments
for i in data:
    #print(i)
    writeSeg(data, i)

