'''
Created on 11 May 2018

@author: PJP2810
'''

import os
import json
import pandas as pd
import re


def readCDJSON(): # Read the cached_definitions.json file
    
    with open('cached_definitions.json') as json_file:  
        data = json.load(json_file)
    
    writeRawCSVs(data)
    
    return data


def writeRawCSVs(data):
    
    os.chdir("Output - Raw")
    
    # Output useful raw parts of the json to CSVs
    pd.DataFrame(data['ability_defines']).to_csv("Ability.csv", index=False)
    pd.DataFrame(data['achievement_defines']).to_csv("Achievements.csv", index=False)
    pd.DataFrame(data['attack_defines']).to_csv("Attacks.csv", index=False)
#    pd.DataFrame(data['background_defines']).to_csv("Backgrounds.csv", index=False)
    pd.DataFrame(data['buff_defines']).to_csv("Buffs.csv", index=False)
    pd.DataFrame(data['chest_type_defines']).to_csv("Chests.csv", index=False)
    pd.DataFrame(data['effect_defines']).to_csv("Effects.csv", index=False)
    pd.DataFrame(data['effect_key_defines']).to_csv("Effect Keys.csv", index=False)
    pd.DataFrame(data['familiar_defines']).to_csv("Familiars.csv", index=False)
    pd.DataFrame(data['graphic_defines']).to_csv("Graphics.csv", index=False)
    pd.DataFrame(data['hero_defines']).to_csv("Heroes.csv", index=False)
    pd.DataFrame(data['loot_defines']).to_csv("Loot.csv", index=False)
#    pd.DataFrame(data['monster_defines']).to_csv("Monsters.csv", index=False)
    pd.DataFrame(data['news_defines']).to_csv("News.csv", index=False)
    pd.DataFrame(data['premium_item_defines']).to_csv("Premium Items.csv", index=False)
    pd.DataFrame(data['sound_defines']).to_csv("Sounds.csv", index=False)
    pd.DataFrame(data['text_defines']).to_csv("Texts.csv", index=False)
    pd.DataFrame(data['tutorial_state_defines']).to_csv("Tutorial.csv", index=False)
    pd.DataFrame(data['upgrade_defines']).to_csv("Upgrades.csv", index=False)
    
    os.chdir("..")
    
    return


def parseAchievementDefinitions(achievements):
    
    os.chdir("Output - Parsed")
    
    # Parse Achievements
    effectDict = {"global_dps_multiplier_mult" : "All Champion Damage Boost",
                  "gold_multiplier_mult" : "Gold Find Boost"}
    
    for x in achievements:
        
        # Rename Keys in Dict
        x['Name'] = x.pop('name')
        x['Graphic ID'] = x.pop('graphic_id')
        x['Description'] = x.pop('description')
        x['Effect'] = x.pop('effect')
        x['Category'] = x.pop('properties')
        
        # Very UGLY attempt to clean up the Dict within the properties Values
        x['Category'] = str(x['Category']).replace("category':", "")
        x['Category'] = str(x['Category']).replace("category':", "")
        x['Category'] = str(x['Category']).replace("'", "")
        x['Category'] = str(x['Category']).replace('"', "")
        x['Category'] = str(x['Category']).replace("{ ", "")
        x['Category'] = str(x['Category']).replace("{", "")
        x['Category'] = str(x['Category']).replace("}", "")
        x['Category'] = str(x['Category']).replace("[]", "Other")
        x['Category'] = str(x['Category']).replace("hidden: 1", "Hidden")
        x['Category'] = re.sub(r"for_event:.*, ", "", str(x['Category']))
        x['Category'] = re.sub(r", for_event:.*", "", str(x['Category']))
                
        # Combine requirement and description for Human-readable description/requirement
        amount = re.sub(r'.*>=', r'' ,x['requirements']) # RegEx to filter requirement down to just the value
        x['Description'] = x['Description'].replace('$(amount)', amount, 1) # Replace '$(amount)' with the requirement value
        
        # Split Effect into Type and Value
        tempList = x['Effect'].split(",")
        # Set Effect name based on Dict of effects : Human-readable names
        x['Effect'] = effectDict.get(tempList[0], tempList[0])
        # Set Effect Value
        try:
            x['Effect Value (%)'] = tempList[1]
        except:
            x['Effect Value (%)'] = ""
        
        # Remove unwanted Keys from Dict
        del x['requirements']
        del x['id']
        
    # Output parsed Achievements to CSV
    pd.DataFrame(achievements).to_csv("Achievements.csv", index=False, columns=['Name', 'Description', 'Effect', 'Effect Value (%)', 'Category', 'Graphic ID'])
    
    os.chdir("..")
    
    return achievements


def parseLootDefinitions(loot):
    
    os.chdir("Output - Parsed")
    
    # Parse Loot
    effectDict = {"hero_dps_multiplier_mult" : "Self Damage Boost",
                  "global_dps_multiplier_mult" : "All Champion Damage Boost",
                  "buff_ultimate" : "Ultimate Boost",
                  "buff_upgrade" : "Ability Upgrade",
                  "buff_upgrades" : "Ability Upgrade",
                  "health_add" : "Health Boost",
                  "buff_crit_chance" : "Increases Critical Strike Chance",
                  "reduce_ultimate_cooldown" : "Reduces Ultimate Cooldown",
                  "health_mult" : "Increases Health",
                  "buff_nrakk_ultimate" : "Buffs Nrakk's Ultimate Effect",
                  "hero_dps_multiplier_if_attack" : "Increases Damage During Ultimate",
                  "buff_attack_damage" : "Increases Specific Specialisation"}
    
    for x in loot:
        
        # Rename Keys in Dict
        x['Name'] = x.pop('name')
        x['Graphic ID'] = x.pop('graphic_id')
        x['Item Description'] = x.pop('description')
        effect = x['effects']
        x['Effect'] = effect[0].get('effect_string', "TEST")
        x['Effect Description'] = effect[0].get('description', "")
        x['Hero'] = x.pop('hero_id')
        x['Rarity'] = x.pop('rarity')
        x['Slot'] = x.pop('slot_id')
        
        x['Effect Value (%)'] = "ThisShouldntBeVisible"
        
        print(x['Effect'], x['Effect Description'])
        
        # Split Effect into Type and Value
        tempList = x['Effect'].split(",")
        # Set Effect name based on Dict of effects : Human-readable names
        x['Effect'] = effectDict.get(tempList[0], tempList[0])
        # Set Effect Value
        try:
            x['Effect Value (%)'] = tempList[1]
        except:
            x['Effect Value (%)'] = ""
        
        # Remove unwanted Keys from Dict
        del x['id']
        del x['effects']
        
    # Output parsed Achievements to CSV
    pd.DataFrame(loot).to_csv("Gear.csv", index=False, columns=['Hero', 'Name', 'Effect', 'Effect Value (%)', 'Effect Description', 'Slot', 'Rarity', 'Item Description', 'Graphic ID'])
    
    os.chdir("..")
    return loot

'''
main_
    Everything past this point is completely unoptimised and purely in place for testing of functions whilst they continue to be built
    Also plenty of what is before this point is probably unoptimised, but is planned to be improved
'''


os.chdir("workingDir")

data = readCDJSON()

parseAchievementDefinitions(data['achievement_defines'])
parseLootDefinitions(data['loot_defines'])











