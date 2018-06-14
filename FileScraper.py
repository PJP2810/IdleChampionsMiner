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

def parseHeroes(fullHeroes = None):
    
    parsedHeroes = []
    heroesDict = {}
    
    if fullHeroes is None:
        fullHeroes = readJSON("hero_defines", "cached_definitions")
    
    
    for x in fullHeroes:
        
        # Store {ability_scores {str, dex, con, int, wis, cha}, age, alignment, backstory, class, race, portrait_graphic_id, id, name, seat_id} to variables
        heroCharSheet = x['character_sheet_details']
        heroSTR = heroCharSheet['ability_scores']['str']
        heroDEX = heroCharSheet['ability_scores']['dex']
        heroCON = heroCharSheet['ability_scores']['con']
        heroINT = heroCharSheet['ability_scores']['int']
        heroWIS = heroCharSheet['ability_scores']['wis']
        heroCHA = heroCharSheet['ability_scores']['cha']
        
        if heroCharSheet['alignment'] == "Neutral": # Converting alignment of Neutral to True Neutral
            heroAlignment = "True Neutral"
        else:
            heroAlignment = heroCharSheet['alignment']
        
        parsedHeroes.append({"Name" : x['name'], "ID" : x['id'],
                             "Class" : heroCharSheet['class'], "Race" : heroCharSheet['race'],
                             "STR" : heroSTR, "DEX" : heroDEX, "CON" : heroCON,
                             "INT" : heroINT, "WIS" : heroWIS, "CHA" : heroCHA,
                             "Age" : heroCharSheet['age'], "Alignment" : heroAlignment,
                             "Seat" : x['seat_id'], "Backstory" : heroCharSheet['backstory']})
        
        heroesDict[x['id']] = {"Name" : x['name'], "Class" : heroCharSheet['class'], "Race" : heroCharSheet['race'],
                                   "STR" : heroSTR, "DEX" : heroDEX, "CON" : heroCON,
                                   "INT" : heroINT, "WIS" : heroWIS, "CHA" : heroCHA,
                                   "Age" : heroCharSheet['age'], "Alignment" : heroCharSheet['alignment'],
                                   "Seat" : x['seat_id'], "Backstory" : heroCharSheet['backstory']}
                
    # Output parsed Upgrades to CSV
    pd.DataFrame(parsedHeroes).to_csv('ParsedHeroes.csv', index=False, columns=["Name", "ID", "Class", "Race", 
                                                                                "STR", "DEX", "CON",
                                                                                "INT", "WIS", "CHA",
                                                                                "Age", "Alignment",
                                                                                "Seat", "Backstory"])
    
    return parsedHeroes, heroesDict

def parseUpgrades(heroesDict, fullUpgrades = None):

    parsedUpgrades = []
    upgradeNameDict = {0 : ""}
    
    if fullUpgrades is None:
        fullUpgrades = readJSON("upgrade_defines", "cached_definitions")
    
    effectDict = {"hero_dps_multiplier_mult" : "Self Damage Boost",
                  "global_dps_multiplier_mult" : "All Champion Damage Boost",
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
        
        # Split Effect into Type and Value
        tempList = x['effect'].split(",")
        
        upgradeEffectName = tempList[0]
        #print(tempList[1])
        
        upgradeEffectValue = tempList[1]
        
        if len(tempList) == 3:
            upgradeBuffedID = eval(tempList[2])
        else:
            upgradeBuffedID = ""
        
        # Use Specialisation name instead of Ability Name when Specialisation Name is present
        if 'specialization_name' in x:
            upgradeName = x['specialization_name']
            upgradeEffectName = "Specialisation Choice"
        else:
            upgradeName = x['name']
        
        # Replace Hero ID with Hero Name using Dictionary of Hero ID:Names
        upgradeHero = heroesDict.get(x['hero_id'])['Name']
        
        # Create dictionary of upgradeID:Name
        upgradeNameDict[x['id']]= upgradeName
        
        # Replace Effect with Human Friendly names
        upgradeEffectName = effectDict.get(upgradeEffectName, upgradeEffectName)
        
        parsedUpgrades.append({"Hero" : upgradeHero, "Level" : x['required_level'],
                               "Name" : upgradeName,
                               "Effect" : upgradeEffectName,
                               "Value": upgradeEffectValue,
                               "Buffed Ability" : upgradeNameDict.get(upgradeBuffedID, upgradeBuffedID), # Replace Buffed Ability ID with Ability Name using Dictionary of Ability ID:Names
                               "Required Spec" : upgradeNameDict.get(x['required_upgrade_id'], x['required_upgrade_id'])}) # Replace Required Spec ID with Spec Name using Dictionary of Ability ID:Names
        
    # Output parsed Upgrades to CSV
    pd.DataFrame(parsedUpgrades).to_csv('ParsedUpgrades.csv', index=False, columns=["Hero",
                                                                                    "Level",
                                                                                    "Name",
                                                                                    "Effect",
                                                                                    "Value",
                                                                                    "Buffed Ability",
                                                                                    "Required Spec"])
    
    return parsedUpgrades

'''
main_
    Everything past this point is completely unoptimised and purely in place for testing of functions whilst they continue to be built
    Also plenty of what is before this point is probably unoptimised, but is planned to be improved
'''

import os
import json
import pandas as pd

os.chdir("workingDir")

fullData = readJSON("cached_definitions")

segNames = listSegments(fullData)

for x in segNames:
    writeSegmentsJSON(fullData, x)

parsedHeroes, heroesDict = parseHeroes()

parseUpgrades(heroesDict, fullData['upgrade_defines'])




