#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 11:14:19 2025

@author: nicholasbyrne
"""

def bgrnd(Opt1,Opt2):
    # if background has skill prof, print
    # three options, proficiency plus any any option
    
    if Opt1 == "Any" and Opt2 == "Any":
        print("Select at least one Proficiency before searching.")
    else:
        no_choice = {
            "Acolyte": ["Insight", "Religion"],
            "Anthropologist": ["Insight", "Religion"],
            "Archaeologist": ["History", "Survival"],
            "Athlete": ["Acrobatics", "Athletics"],
            "Charlatan": ["Deception", "Sleight of Hand"],
            "City Watch": ["Athletics", "Insight"],
            "Clan Crafter": ["History", "Insight"],
            "Courtier": ["Insight", "Persuasion"],
            "Criminal": ["Deception", "Stealth"],
            "Entertainer": ["Acrobatics", "Performance"],
            "Faceless": ["Deception", "Intimidation"],
            "Far Traveler": ["Insight", "Perception"],
            "Feylost": ["Deception", "Survival"],
            "Fisher": ["History", "Survival"],
            "Folk Hero": ["Animal Handling", "Survival"],
            "Giant Foundling": ["Intimidation", "Survival"],
            "Gladiator": ["Acrobatics", "Performance"],
            "Guild Artisan": ["Insight", "Persuasion"],
            "Guild Merchant": ["Insight", "Persuasion"],
            "Haunted One": ["Arcana", "Investigation", "Religion", "Survival"],
            "Hermit": ["Medicine", "Religion"],
            "House Agent": ["Investigation", "Persuasion"],
            "Investigator (SCAG)": ["Insight", "Investigation", "Perception"],
            "Investigator (VRGR)": ["Insight", "Investigation", "Perception"],
            "Knight": ["History", "Persuasion"],
            "Marine": ["Athletics", "Survival"],
            "Mercenary Veteran": ["Athletics", "Persuasion"],
            "Noble": ["History", "Persuasion"],
            "Outlander": ["Athletics", "Survival"],
            "Pirate": ["Athletics", "Perception"],
            "Rewarded": ["Insight", "Persuasion"],
            "Ruined": ["Stealth", "Survival"],
            "Rune Carver": ["History", "Perception"],
            "Sage": ["Arcana", "History"],
            "Sailor": ["Athletics", "Perception"],
            "Shipwright": ["History", "Perception"],
            "Smuggler": ["Athletics", "Deception"],
            "Soldier": ["Athletics", "Intimidation"],
            "Spy": ["Deception", "Stealth"],
            "Urchin": ["Sleight of Hand", "Stealth"],
            "Uthgardt Tribe Member": ["Athletics", "Survival"],
            "Waterdhavian Noble": ["History", "Persuasion"],
            "Witchlight Hand": ["Performance", "Sleight of Hand"],
            "Urban Bounty Hunter": ["Deception", "Insight", "Persuasion", "Stealth"],
            }
    
        choose_1 = {
            "Cloistered Scholar": ["History", ["Arcana","Nature","Religion"]],
            "Inheritor": ["Survival", ["Arcana","History","Religion"]],
            "Knight of the Order": ["Persuasion", ["Arcana", "History", "Nature","Religion"]],
            }
    
        Valid_list = []
        for x in no_choice:
            if Opt1 == "Any" or Opt1 in no_choice[x]:
                if Opt2 == "Any" or Opt2 in no_choice[x]:
                    Valid_list.append(x)
    
        for x in choose_1:
        
            skills = choose_1[x] #set skills as list (value of each key)
            fixed = skills[0] # fixed is the first element
            choice = skills[1] # choice is list of choices (second element)
        
        
            if Opt1 == "Any" or Opt1 == fixed:
                if Opt2 == "Any" or Opt2 in choice:
                    Valid_list.append(x)
                
            elif Opt1 == "Any" or Opt1 in choice:
                if Opt2 == "Any" or Opt2 == fixed:
                    Valid_list.append(x)  
            
        if len(Valid_list) == 0:
            final_message = "No Valid Backgrounds"
        else:
            final_message = ""
            for r in Valid_list:
                final_message += f"{r}\n"
            
        return final_message

def present_BACK(Opt1,Opt2):
    if Opt1 == "Any":
        header = f"Backgrounds that give {Opt2} proficiency:\n"
    elif Opt2 == "Any":
        header = f"Backgrounds that give {Opt1} proficiency:\n"
    else:
        header = f"Backgrounds that give {Opt1} and {Opt2} proficiencies:\n"
    
    results = bgrnd(Opt1,Opt2)
    output = f"{header}\n{results}"
    return output
    
    
       
def tester():
    
    print(present_BACK("History","Any"))
    print(present_BACK("Athletics","Sleight of Hand"))

if __name__ == '__main__':
    tester()

        