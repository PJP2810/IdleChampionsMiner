'''
Created on 5 May 2018

@author: PJP2810
'''

# Function definitions
def writeSegmentsJSON(data, segment):
    
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

def parseUpgrades():

    parsedUpgrades = []
    
    fullUpgrades = readJSON("upgrade_defines", "cached_definitions")
    
    effectDict = {"hero_dps_multiplier_mult" : "Self Damage Boost",
                  "global_dps_multiplier_mult" : "All Damage Boost",
                  "buff_ultimate" : "Ultimate Boost",
                  "buff_upgrade" : "Ability Upgrade",
                  "buff_upgrades" : "Ability Upgrade",
                  "effect_def" : "Ability Unlock",
                  "health_add" : "Health Boost",
                  "gold_multiplier_mult" : "Gold Find Boost",
                  "add_attack_targets" : "Increase Number of Enemies Targeted",
                  "set_ultimate_attack" : "Ultimate Unlock",
                  "owner_killing_blow_gold_bonus" : "Gold Boost on Kill",
                  "add_attack_nearby_targets" : "Grants Secondary Attack to Nearby Target",
                  "reduce_attack_cooldown" : "Lowers Attack Timer",
                  "attacks_ricochet" : "Grants Ricochet to Attack",
                  "add_damage_over_time" : "Grants Damage Over Time to Attack",
                  "buff_crit_chance" : "Increases Critical Strike Chance",
                  "attack_crit_chance" : "Grants Critical Strike Chance to Attacks",
                  "increase_aoe_radius" : "Increases Area of Effect Radius",
                  "increase_stun_time" : "Increases Stun Time",
                  "increase_monster_attack_priority" : "Grants Enemy Taunt",
                  "damage_reduction" : "Grants Damage Reduction",
                  "return_damage_when_hit" : "Grants Thorns"}
    
    # Loop through fullUpgrades
    for x in fullUpgrades:
        
        # Store {effect, hero_id, id, required_level, required_upgrade_id} to variables
        upgradeEffect = x['effect']
        upgradeRequiredID = x['required_upgrade_id']
        upgradeHero = x['hero_id']
        
        # Split Effect into Type and Value
        tempList = upgradeEffect.split(",")
        
        upgradeEffectName = tempList[0]
        upgradeEffectValue = tempList[1]
        if len(tempList) == 3:
            upgradeBuffedID = tempList[2]
        else:
            upgradeBuffedID = ""
        
        # Use Specialisation name instead of Ability Name when Specialisation Name is present
        if 'specialization_name' in x:
            upgradeName = x['specialization_name']
            upgradeEffectName = "Specialisation Choice"
        else:
            upgradeName = x['name']
        
        # Replace Hero ID with Hero Name using Dictionary of Hero ID:Names
        
        
        # Replace Required Spec ID with Spec Name using Disctionary of Spec ID:Names | 0 = ""
        
        
        # Replace Effect with Human Friendly names
        upgradeEffectName = effectDict.get(upgradeEffectName, upgradeEffectName)
        
        parsedUpgrades.append({ "Hero" : upgradeHero, "Level" : x['required_level'],
                               "Name" : upgradeName,
                               "Effect" : upgradeEffectName,
                               "Value": upgradeEffectValue,
                               "Buffed Ability" : upgradeBuffedID,
                               "Upgrade ID" : x['id'],
                               "Required Spec" : upgradeRequiredID})
        
    # Output parsed Upgrades to CSV
    pd.DataFrame(parsedUpgrades).to_csv('ParsedUpgrades.csv', index=False, columns=["Hero",
                                                                                    "Level",
                                                                                    "Name",
                                                                                    "Effect",
                                                                                    "Value",
                                                                                    "Buffed Ability",
                                                                                    "Upgrade ID",
                                                                                    "Required Spec"])
    
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
    writeSegmentsJSON(fullData, x)


parseUpgrades()








