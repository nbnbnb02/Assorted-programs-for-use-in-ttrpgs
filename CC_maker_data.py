#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 00:18:56 2025

@author: nicholasbyrne
"""

subclass_dict = {
"-": [['-'],(1,1)],
"Artificer": [['-','Alchemist', 'Armourer', 'Artillerist', 'Battle Smith'],(8,5)], 
"Barbarian": [['-','Ancestral Guardian', 'Battlerager', 'Beast', 'Berserker', 'Giant', 'Storm Herald', 'Totem Warrior', 'Wild Magic', 'Zealot'],(12,7)],
"Bard": [['-','Creation', 'Eloquence', 'Glamour', 'Lore', 'Spirits', 'Swords', 'Valour', 'Whispers'], (8,5)], 
"Cleric": [['-','Arcana', 'Death', 'Forge', 'Grave', 'Knowledge', 'Life', 'Light', 'Nature', 'Order', 'Peace', 'Tempest', 'Trickery', 'Twilight', 'War'], (8,5)],
"Druid": [['-','Dreams', 'Land', 'Moon', 'Shepherd', 'Spores', 'Stars', 'Wildfire'], (8,5)], 
"Fighter": [['-','Arcane Archer', 'Bannerete', 'Battle Master', 'Cavalier', 'Champion', 'Echo Knight', 'Eldritch Knight', 'Psi Warrior', 'Rune Knight', 'Samurai'], (10,6)], 
"Monk": [['-','Mercy', 'Ascendant Dragon', 'Astral Self', 'Drunken Master', 'Four Elements', 'Kensei', 'Long Death', 'Open Hand', 'Shadow', 'Sun Soul'], (8,5)],
"Paladin": [['-','Ancients', 'Conquest', 'Crown', 'Devotion', 'Glory', 'Redemption', 'Vengeance', 'Watchers', 'Oathbreaker'], (10,6)], 
"Ranger": [['-','Beast Master', 'Drakewarden', 'Fey Wanderer', 'Gloom Stalker', 'Horizon Walker', 'Hunter', 'Monster Slayer', 'Swarmkeeper'], (10,6)], 
"Rogue": [['-','Arcane Trickster', 'Assassin', 'Inquisitive', 'Mastermind', 'Phantom', 'Scout', 'Soulknife', 'Swashbuckler', 'Thief'], (8,5)], 
"Sorcerer": [['-','Aberrant Mind', 'Clockwork Soul', 'Draconic Bloodline', 'Divine Soul', 'Lunar Sorcery', 'Shadow Magic', 'Storm Sorcery', 'Wild Magic'], (6,4)], 
"Warlock": [['-','Archfey', 'Celestial', 'Fathomless', 'Fiend', 'The Genie', 'Great Old One', 'Hexblade', 'Undead', 'Undying'], (8,5)], 
"Wizard": [['-','Abjuration', 'Bladesinging', 'Chronurgy', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Graviturgy', 'Illusion', 'Necromancy', 'Order of Scribes', 'Transmutation', 'War Magic'], (6,4)]
}

bgr_profs = {
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
            "Hermit": ["Medicine", "Religion"],
            "House Agent": ["Investigation", "Persuasion"],
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
            
            "Cloistered Scholar": ["History", ["Arcana","Nature","Religion"]],
            "Inheritor": ["Survival", ["Arcana","History","Religion"]],
            "Investigator (SCAG)": ["Insight", ["Athletics","Investigation"]],
            "Knight of the Order": ["Persuasion", ["Arcana", "History", "Nature","Religion"]],
            
            "Haunted One": [2, ["Arcana", "Investigation", "Religion", "Survival"]],
            "Investigator (VRGR)": [2, ["Insight", "Investigation", "Perception"]],
            "Urban Bounty Hunter": [2,["Deception", "Insight", "Persuasion", "Stealth"]],
            }



Lineages = {
         'Dragonborn':['Black', 'Blue', 'Green', 'Red', 'White','Amethyst', 'Crystal', 'Emerald', 'Saphire', 'Topaz','Brass', 'Bronze', 'Copper', 'Gold', 'Silver'],
         'Dwarf': ['Hill', 'Mountain'], 
         'Elf': ['Dark', 'High', 'Wood', 'Pallid'], 
         'Gnome': ['Forest', 'Rock'], 
         'Half-Elf': ["General","High","Wood","Dark","Aquatic"],
         'Half-Orc': "-", 
         'Halfling': ['Lightfoot', 'Stout', 'Ghostwise', 'Lotsuden'], 
         'Human': "-", 
         'Tiefling': ['Asmodeus', 'Baalzebul', 'Dispater', 'Fierna', 'Glasya', 'Levistus', 'Mammon', 'Mephistopheles', 'Zariel','Variant'],
         'Aarakocra': "-", 
         'Aasimar': ['Protector', 'Scourge', 'Fallen'], 
         'Changeling': "-", 
         'Deep Gnome': "-", 
         'Duergar': "-", 
         'Eladrin': "-", 
         'Fairy': "-", 
         'Firbolg': "-", 
         'Genasi': ['Air', 'Fire', 'Water', 'Earth'], 
         'Githyanki': "-", 
         'Githzerai': "-", 
         'Goliath': "-", 
         'Harengon': "-", 
         'Kenku': "-", 
         'Locathah': "-", 
         'Owlin': "-", 
         'Satyr': "-", 
         'Sea Elf': "-", 
         'Shadar-Kai': "-", 
         'Tabaxi': "-", 
         'Tortle': "-", 
         'Triton': "-", 
         'Verdan': "-", 
         'Warforged': "-",
         'Bugbear': "-", 
         'Centaur': "-", 
         'Goblin': "-", 
         'Grung': "-", 
         'Hobgoblin': "-", 
         'Kobold': "-", 
         'Lizardfolk': "-", 
         'Minotaur': "-", 
         'Orc': "-", 
         'Shifter': ['Werebear', 'Wererat', 'Weretiger', 'Werewolf (wolf)', 'Werewolf (dog)'], 
         'Yuan-Ti': "-"
         }

    





                       
ADV = ["Acid", "Bludgeoning", "Cold", "Fire", "Force", "Lightning", "Necrotic", "Piercing", "Poison", "Psychic", "Radiant", "Slashing", "Thunder", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma","Strength(S)", "Dexterity(S)", "Constitution(S)", "Intelligence(S)", "Wisdom(S)", "Charisma(S)", "Blinded", "Charmed", "Deafened", "Frightened", "Grappled", "Incapacitated", "Invisible", "Paralysed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious", "Exhausted"]

Immunities = ["Acid", "Bludgeoning", "Cold", "Fire", "Force", "Lightning", "Necrotic", "Piercing", "Poison", "Psychic", "Radiant", "Slashing", "Thunder", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma","Strength(S)", "Dexterity(S)", "Constitution(S)", "Intelligence(S)", "Wisdom(S)", "Charisma(S)", "Blinded", "Charmed", "Deafened", "Frightened", "Grappled", "Incapacitated", "Invisible", "Paralysed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious", "Exhausted","Sleep","Disease"]


Armour = ["Light","Medium","Heavy","Shield","Only Shield","All"]

Weapons = ["Simple","Martial","All","Club","Dagger","Greatclub","Handaxe","Javelin","Light Hammer","Mace","Quarterstaff","Sickle","Spear","Light Crossbow","Dart","Shortbow","Sling","Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War pick", "Warhammer", "Whip", "Blowgun", "Hand Crossbow","Heavy Crossbow", "Longbow", "Net"]

Resistances = ["Acid", "Bludgeoning", "Cold", "Fire", "Force", "Lightning", "Necrotic", "Piercing", "Poison", "Psychic", "Radiant", "Slashing", "Thunder"]

Languages = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon", "Aquan", "Auran", "Ignan", "Terran", "Aarakocra", "Druidic", "Gith", "Thieves' Cant"]




#   (walking,flying,swimming,climbing), (bright, dim, dark), armour, weapon, language,
Race_feats2 = {
        #     RACE                  SPEED         SIGHT         FEATURES                              PROFICIENCIES/RESISTANCE               ADV       ALT AC     
         'Dragonborn':         ([30,"-","-","-"],"Normal",["Breath Weapon"],["Draconic"],                                                      [], [],           []),
         'Black':              ([30,"-","-","-"],"Normal",["Acid","Line","Dex","Chromatic Warding"],            ["Acid"],                      [], [],           []),
         'Blue':               ([30,"-","-","-"],"Normal",["Lightning","Line","Dex","Chromatic Warding"],       ["Lightning"],                 [], [],           []),
         'Green':              ([30,"-","-","-"],"Normal",["Poison","Line","Dex","Chromatic Warding"],          ["Poison"],                    [], [],           []),
         'Red':                ([30,"-","-","-"],"Normal",["Fire","Line","Dex","Chromatic Warding"],            ["Fire"],                      [], [],           []),
         'White':              ([30,"-","-","-"],"Normal",["Cold","Line","Dex","Chromatic Warding"],            ["Cold"],                      [], [],           []),
         'Amethyst':           ([30,"W","-","-"],"Normal",["Force","Cone","Dex","Psionic Mind","Gem Flight"],   ["Force"],                     [], [],           []),
         'Crystal':            ([30,"W","-","-"],"Normal",["Radiant","Cone","Dex","Psionic Mind","Gem Flight"], ["Radiant"],                   [], [],           []),
         'Emerald':            ([30,"W","-","-"],"Normal",["Psychic","Cone","Dex","Psionic Mind","Gem Flight"], ["Psychic"],                   [], [],           []),
         'Saphire':            ([30,"W","-","-"],"Normal",["Thunder","Cone","Dex","Psionic Mind","Gem Flight"], ["Thunder"],                   [], [],           []),
         'Topaz':              ([30,"W","-","-"],"Normal",["Necrotic","Cone","Dex","Psionic Mind","Gem Flight"],["Necrotic"],                  [], [],           []),
         'Brass':              ([30,"-","-","-"],"Normal",["Fire","Cone","Dex","Metallic Breath Weapon"],       ["Fire"],                      [], [],           []),
         'Bronze':             ([30,"-","-","-"],"Normal",["Lightning","Cone","Dex","Metallic Breath Weapon"],  ["Lightning"],                 [], [],           []),
         'Copper':             ([30,"-","-","-"],"Normal",["Acid","Cone","Dex","Metallic Breath Weapon"],       ["Acid"],                      [], [],           []),
         'Gold':               ([30,"-","-","-"],"Normal",["Fire","Cone","Dex","Metallic Breath Weapon"],       ["Fire"],                      [], [],           []),
         'Silver':             ([30,"-","-","-"],"Normal",["Acid","Cone","Dex","Metallic Breath Weapon"],       ["Acid"],                      [], [],           []),

         'Dwarf':              ([25,"-","-","-"],"Darkvision",["Tool Proficiency","Stonecunning"], ["Handaxe","Light Hammer","Battleaxe","Poison","Dwarvish"],["Poisoned"],[],[]),
         'Hill':               ([25,"-","-","-"],"Darkvision",["Dwarven Toughness"],                           [],                             [],  [],                  []),
         'Mountain':           ([25,"-","-","-"],"Darkvision",[],                                    ["Light","Medium"],                 [],         [],          []),

         'Elf':                ([30,"-","-","-"],"Darkvision",["Trance"],                                    ["Perception","Elvish"],      ["Charmed"],["Sleep"], []),
         'Dark':               ([30,"-","-","-"],"Superior Darkvision",["Sunlight Sensitivity","Drow Magic"],  ["Rapier","Shortsword","Hand Crossbow"],  [],[],    []),
         'High':               ([30,"-","-","-"],"Darkvision",["Wizard Cantrip","Extra Language"],["Shortbow","Shortsword","Longsword","Longbow"],[], [],         []),
         'Wood':               ([35,"-","-","-"],"Darkvision",["Mask of the Wild"],["Shortbow","Shortsword","Longsword","Longbow"],            [], [],               []),
         'Pallid':             ([30,"-","-","-"],"Darkvision",["Blessing of the Moonweaver"],                  [],                          ["Investigation","Insight"],[], []),
         
         'Gnome':              ([25,"-","-","-"],"Darkvision",[],                 ["Gnomish"],              ["Intelligence(S)","Wisdom(S)","Charisma(S)"], [],        [] ),
         'Forest':             ([25,"-","-","-"],"Darkvision",["Natural Illusionist","Speak with Small Beasts"],       [],                    [], [],              []),
         'Rock':               ([25,"-","-","-"],"Darkvision",["Artificer's Lore","Tinker"],                       [],                        [],  [],              []),

         'Half-Elf':           ([30,"-","-","-"],"Darkvision",["Extra Language"],                                  ["Elvish"],        ["Charmed"],["Sleep"],         []),
         'Skill Versatility':  ([30,"-","-","-"],"Darkvision",["Skill Versatility"],                                 [],                        [], [],              []),
         'Elf WT (H or W)':    ([30,"-","-","-"],"Darkvision",[],                         ["Shortbow","Shortsword","Longsword","Longbow"],      [], [],              []),
         'Cantrip (H)':        ([30,"-","-","-"],"Darkvision",["Wizard Cantrip"],                                [],                            [], [],               []),
         'Fleet of Foot (W)':  ([35,"-","-","-"],"Darkvision",[],                                                [],                            [], [],              []),
         'Mask of Wild (W)':   ([30,"-","-","-"],"Darkvision",["Mask of the Wild"],                               [],                           [], [],              []),
         'Drow Magic (D)':     ([30,"-","-","-"],"Darkvision",["Drow Magic"],                                    [],                            [], [],              []),
         'Swim Speed (A)':     ([30,"-",30,"-"], "Darkvision",[],                                                 [],                           [], [],              []),

         'Half-Orc':           ([30,"-","-","-"],"Darkvision",["Relentless Endurance","Savage Attacks"],        ["Intimidation","Orc"],               [], [],              []),

         'Halfling':           ([25,"-","-","-"],"Normal",["Lucky","Nimble"],                                   ["Halfling"],                     ["Frightened"],[],[]),
         'Lightfoot':          ([25,"-","-","-"],"Normal",["Naturally Stealthy"],[],[],[],[]),
         'Stout':              ([25,"-","-","-"],"Normal",[],["Poison"],["Poisoned"],[],[]),
         'Ghostwise':          ([25,"-","-","-"],"Normal",["Silent Speech"],[],[],[],[]),
         'Lotsuden':           ([25,"-","-","-"],"Normal",["Children of the Woods","Timberwalk"],[],[],[],[]),

         'Human':              ([30,"-","-","-"],"Normal",["Skills","Feat","Extra Language"],[],[],[],[]),

         'Tiefling':           ([30,"-","-","-"],"Darkvision",[],["Fire","Infernal"],[],[],[]),
         'Asmodeus':           ([30,"-","-","-"],"Darkvision",["Infernal Legacy"],[],[],[],[]),
         'Baalzebul':          ([30,"-","-","-"],"Darkvision",["Legacy of Maladomini"],[],[],[],[]),
         'Dispater':           ([30,"-","-","-"],"Darkvision",["Legacy of Dis"],[],[],[],[]),
         'Fierna':             ([30,"-","-","-"],"Darkvision",["Legacy of Phlegethos"],[],[],[],[]),
         'Glasya':             ([30,"-","-","-"],"Darkvision",["Legacy of Malbolge"],[],[],[],[]),
         'Levistus':           ([30,"-","-","-"],"Darkvision",["Legacy of Stygia"],[],[],[],[]),
         'Mammon':             ([30,"-","-","-"],"Darkvision",["Legacy of Minauros"],[],[],[],[]),
         'Mephistopheles':     ([30,"-","-","-"],"Darkvision",["Legacy of Cania"],[],[],[],[]),
         'Zariel':             ([30,"-","-","-"],"Darkvision",["Legacy of Avernus"],[],[],[],[]),
         'Variant':            ([30,30,"-","-"],"Darkvision",["Devil's Tongue","Hellfire","Winged"],[],[],[],[]),

         'Aarakocra':          ([30,"W","-","-"],"Normal",["Talons","Wind Caller"],["Aarakocra"],[],[],[]),

         'Aasimar':            ([30,"-","-","-"],"Darkvision",["Healing Hands","Light Bearer","Extra Language"],["Necrotic","Radiant"],[],[],[]),
         'Protector':          ([30,"W","-","-"],"Darkvision",["Radiant Soul"],[],[],[],[]),
         'Scourge':            ([30,"-","-","-"],"Darkvision",["Radiant Consumption"],[],[],[],[]),
         'Fallen':             ([30,"-","-","-"],"Darkvision",["Necrotic Shroud"],[],[],[],[]),

         'Changeling':         ([30,"-","-","-"],"Normal",["Changeling Instincts","Shapechanger","Extra Language"],[],[],[],[]),

         'Deep Gnome':         ([30,"-","-","-"],"Superior Darkvision",["Gift of the Svirfneblin","Svirfneblin Camouflage","Extra Language"],[],["Intelligence(S)","Wisdom(S)","Charisma(S)"],[],[]),

         'Duergar':            ([30,"-","-","-"],"Superior Darkvision",["Duergar Magic","Extra Language"],["Poison"],["Poisoned","Charmed","Stunned"],[],[]),

         'Eladrin':            ([30,"-","-","-"],"Darkvision",["Fey Step","Eladrin Trance","Extra Language"],["Perception"],["Charmed"],[],[]),

         'Fairy':              ([30,"W","-","-"],"Normal",["Fairy Magic","Extra Language"],[],[],[],[]),

         'Firbolg':            ([30,"-","-","-"],"Normal",["Firbolg Magic","Hidden Step","Powerful Build","Speech of Beast and Leaf","Extra Language"],[],[],[],[]),

         'Air':                ([35,"-","-","-"],"Darkvision",["Unending Breath","Mingle with the Wind","Extra Language"],["Lightning"],[],[],[]),
         'Fire':               ([30,"-","-","-"],"Darkvision",["Reach to the Blaze","Extra Language"],["Fire"],[],[],[]),
         'Water':              ([30,"-","W","-"],"Darkvision",["Amphibious","Call to the Wave","Extra Language"],["Acid"],[],[],[]),
         'Earth':              ([30,"-","-","-"],"Darkvision",["Earth Walk","Merge with Stone","Extra Language"],[],[],[],[]),

         'Githyanki':          ([30,"-","-","-"],"Normal",["Astral Knowledge","Githyanki Psionics"],["Psychic","Gith"],[],[],[]),
         'Githzerai':          ([30,"-","-","-"],"Normal",["Githzerai Psionics"],["Gith"],["Charmed","Frightened"],[],[]),

         'Goliath':            ([30,"-","-","-"],"Normal",["Little Giant","Mountain Born","Stone's Endurance","Extra Language"],["Athletics","Cold"],[],[],[]),

         'Harengon':           ([30,"-","-","-"],"Normal",["Lucky Footwork","Rabbit Hop","Extra Language"],["Initiative","Perception"],[],[],[]),

         'Kenku':              ([30,"-","-","-"],"Normal",["Expert Duplication","Kenku Recall","Mimicry","Extra Language"],[],[],[],[]),

         'Locathah':           ([30,"-","30","-"],"Normal",["Limited Amphibiousness"],["Athletics","Perception","Aquan"],["Charmed","Frightened","Paralysed","Poisoned","Stunned"],["Sleep"],[12,"Dex"]),

         'Owlin':              ([30,"W","-","-"],"Superior Darkvision",[],["Stealth"],[],[],[]),

         'Satyr':              ([35,"-","-","-"],"Normal",["Ram","Mirthful Leap","Reveler","Extra Language"],["Performance","Peruasion"],["Spells"],[],[]),

         'Sea Elf':            ([30,"-","W","-"],"Darkvision",["Child of the Sea","Friend of the Sea","Trance - Sea Elf","Extra Language"],["Cold","Perception"],["Charmed"],[],[]),

         'Shadar-Kai':         ([30,"-","-","-"],"Darkvision",["Blessing of the Raven Queen","Trance - Shadar-Kai","Extra Language"],["Perception","Necrotic"],["Charmed"],[],[]),

         'Tabaxi':             ([30,"-","-","W"],"Darkvision",["Cat's Claws","Feline Agility","Extra Language"],["Perception","Stealth"],[],[],[]),

         'Tortle':             ([30,"-","-","-"],"Normal",[],["Only Shield","Hold Breath","Claws","Nature's Intuition","Shell Defense","Extra Language"],[],[],[17,"-"]),

         'Triton':             ([30,"-","W","-"],"Darkvision",["Amphibious","Control Air and Water","Emissary of the Sea","Extra Language"],["Cold"],[],[],[]),

         'Verdan':             ([30,"-","-","-"],"Normal",["Black Blood Healing","Limited Telepathy","Extra Language"],["Persuasion"],["Wisdom","Charisma"],[],[]),

         'Warforged':          ([30,"-","-","-"],"Normal",["Constructed Resilience","Sentry's Rest","Integrated Protection","Specialised Design","Extra Language"],["Poison"],["Poisoned"],["Sleep","Disease"],["Plus 1"]),

         'Bugbear':            ([30,"-","-","-"],"Darkvision",["Long-Limbed","Powerful Build","Surprise Attack","Extra Language"],["Stealth"],["Charmed"],[],[]),

         'Centaur':            ([30,"-","-","-"],"Normal",["Natural Affinity","Hooves","Equine Build","Charge","Extra Language"],[],[],[],[]),

         'Goblin':             ([30,"-","-","-"],"Darkvision",["Fury of the Small","Nimble Escape","Extra Language"],[],["Charmed"],[],[]),

         'Grung':              ([25,"-","-","25"],"Normal",["Poisonous Skin","Standing Leap","Water Dependency","Amphibious"],["Perception","Poison","Grung"],["Poisoned"],[],[]),

         'Hobgoblin':          ([30,"-","-","-"],"Darkvision",["Fey Gift","Fortune from the Many","Extra Language"],[],["Charmed"],[],[]),

         'Kobold':             ([30,"-","-","-"],"Darkvision",["Draconic Cry","Extra Language"],[],[],[],[]),
         'Craftiness':         ([30,"-","-","-"],"Darkvision",["Kobold Legacy: Craftiness"],[],[],[],[]),
         'Defiance':           ([30,"-","-","-"],"Darkvision",["Kobold Legacy: Defiance"],[],[],[],[]),
         'Draconic Sorcery':   ([30,"-","-","-"],"Darkvision",["Kobold Legacy: Draconic Sorcery"],[],[],[],[]),

         'Lizardfolk':         ([30,"-","W","-"],"Normal",["Bite","Hold Breath","Hungry Jaws","Nature's Intuition","Extra Language"],[],[],[],[13,"Dex"]),

         'Minotaur':           ([30,"-","-","-"],"Normal",["Horns","Goring Rush","Hammering Horns","Labyrinthine Recall","Extra Language"],[],[],[],[]),

         'Orc':                ([30,"-","-","-"],"Darkvision",["Adrenaline Rush","Powerful Build","Relentless Endurance","Extra Language"],[],[],[],[]),

         'Shifter':            ([30,"-","-","-"],"Darkvision",["Bestial Instincts","Shifting","Extra Language"],[],[],[],[]),

         'Yuan-Ti':            ([30,"-","-","-"],"Darkvision",["Serpentine Spellcasting","Extra Language"],["Poison"],["Poisoned","Spells"],[],[]),

         }    


Class_profs = { # hit dice = (HIT DI, avg), armour, weapons, tools, saves, skills = (number, available), starting = (equipment, gold)
"-": ([],[],[],[],[],[],[]),

"Artificer": (
[8,5], 

["Light","Medium","Shield"],

["Simple"], 

["Thieves' Tools","Tinker's Tools", "Artisan Tool of Choice"], 

["Con","Int"], 

[2, ["Arcana","History","Investigation","Medicine","Nature","Perception","Sleight of Hand"]], 

[
[(2, "Simple"),("Light Crossbow"),("Studded Leather","Scale Mail"),("Thieves' Tools"),("Dungeoneer's Pack")], 
[5,4,10]
] 

), 

"Barbarian": (
[12,7], 
["Light","Medium","Shield"],
["Simple","Martial"], 
[], 
["Str","Con"], 
[2, ["Animal Handling","Athletics","Intimidation","Nature","Perception","Survival"]], 
[
[("Greataxe","Martial Melee"),((2,"Handaxe"),"Simple"),("Explorer's Pack"),(4,"Javelin")], 
[2,4,10]
] 

), 

"Bard": (
[8,5], 
["Light"],
["Simple","Hand Crossbow","Rapier","Longsword","Shortsword"], 
[(3,"Musical Instrument")], 
["Dex","Charisma"], 
[3, ["All"]], 
[
[("Rapier","Longsword", "Simple"),("Leather"),("Dagger"),("Lute","Musical Instrument"),("Diplomat's Pack","Entertainer's Pack")], 
[5,4,10]
]
), 

"Cleric": (
[8,5], 
["Light","Medium","Shield"],
["Simple"], 
[], 
["Wis","Cha"],
[2, ["History","Insight","Medicine","Persuasion","Religion"]], 
[
[("Mace", "Warhammer"),("Light Crossbow", "Simple"),("Leather","Scale Mail","Chain Mail"),("Shield","Holy Symbol"),("Priest's Pack", "Explorer's Pack")], 
[5,4,10]
] 
), 

"Druid":[
(8,5), 
["Light","Medium","Shield"],
["Club", "Dagger", "Dart", "Javelin", "Mace", "Quarterstaff", "Scimitar", "Sickle", "Sling", "Spear"], 
["Herbalism Kit"], 
["Int","Wis"], 
(2, ["Arcana","Animal Handling","Insight","Medicine","Nature","Perception","Religion","Survival"]), 
(
[("Shield", "Simple"),("Scimitar","Simple"),("Leather"),("Druidic Focus"),("Explorer's Pack")], 
(2,4,10)
) 
], 

"Fighter": [
(10,6), 
["Light","Medium","Heavy","Shield"],
["Simple","Martial"], 
[], 
["Str","Con"], 
(2, ["Acrobatics","Animal Handling","Athletics","History","Insight","Intimidation","Perception","Survival"]), 
(
[("Chain", ("Leather","Longbow")),("Martial"),("Martial", "Shield"),("Light Crossbow",(2,"Handaxe")),("Dungeoneer's Pack", "Explorer's Pack")], 
(5,4,10)
) 
], 


"Monk": [
(8,5), 
[],
["Simple","Shortsword"], 
[("Musical Instrument", "Artisan Tool")], 
["Str","Dex"], 
(2, ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]), 
(
[("Shortsword", "Simple"),(10, "Dart"),("Dungeoneer's Pack", "Explorer's Pack")], 
(5,4,1)
) 
], 

"Paladin": [
(10,6), 
["Light","Medium","Heavy","Shield"],
["Simple","Martial"], 
[], 
["Wis","Cha"], 
(2, ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]), 
(
[("Chain"),("Martial"),("Martial", "Shield"),("Holy Symbol"),((5, "Javelin"), "Simple Melee"),("Priest's Pack", "Explorer's Pack")], 
(5,4,10)
) 
], 

"Ranger": [
(10,6), 
["Light","Medium","Shield"],
["Simple","Martial"], 
[], 
["Str","Dex"], 
(2, ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]), 
(
[((2,"Shortsword"),(2, "Simple")),("Longbow"),("Leather","Scale Mail"),("Dungeoneer's Pack", "Explorer's Pack")], 
(5,4,10)
) 
], 

"Rogue": [
(8,5), 
["Light"],
["Simple","Hand Crossbow", "Longsword", "Rapier", "Shortsword"], 
["Thieves' Tools"], 
["Dex","Int"], 
(4, ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]), 
(
[("Rapier", "Shortsword"),("Shortbow", "Shortsword"),("Leather"),(2,"Dagger"),("Thieves' Tools"),("Burglar's Pack","Dungeoneer's Pack", "Explorer's Pack")], 
(4,4,10)
) 
], 

"Sorcerer": [
(6,4), 
[],
["Daggers", "Dart", "Sling", "Quarterstaff", "Light Crossbow"], 
[], 
["Con","Cha"], 
(2, ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]), 
(
[("Simple","Light Crossbow"),("Component Pouch","Arcane Focus"),(2,"Dagger"),("Dungeoneer's Pack", "Explorer's Pack")], 
(3,4,10)
) 
], 

"Warlock": [
(8,5), 
["Light"],
["Simple"], 
[], 
["Wis","Cha"], 
(2, ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]), 
(
[("Simple","Light Crossbow"),("Simple"),("Component Pouch","Arcane Focus"),("Leather"),(2,"Dagger"),("Dungeoneer's Pack","Scholar's Pack")], 
(4,4,10)
) 
], 

"Wizard": [
(6,4), 
[],
["Daggers", "Dart", "Sling", "Quarterstaff", "Light Crossbow"], 
[], 
["Int","Wis"], 
(2, ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]), 
(
[("Quarterstaff","Dagger"),("Component Pouch","Arcane Focus"),("Spellbook"),("Scholar's Pack", "Explorer's Pack")], 
(4,4,10)
) 
]

}












# ------------------------------------------------------------------ FEATS ---------------------------------------------------------------------------------------------------------------------------------


Feat_dict = {
    "Alert": "• +5 bonus to initiative\n• You can't be surprised while conscious\n• Other creatures don't gain advantage on attack rolls against you from being hidden",
    
    "Athlete": "• Increase Strength or Dexterity by 1 (max 20)\n• Climbing doesn't cost extra movement\n• Standing up from prone uses only 5 feet of movement\n• Running jump distance increased with only 5 feet running start",
    
    "Actor": "• Increase Charisma by 1 (max 20)\n• Advantage on Deception and Performance checks to mimic speech/sounds\n• Can mimic creature's speech after hearing for 1 minute",
    
    "Charger": "• When you use Dash action, you can make one melee weapon attack or shove as bonus action\n• If you move at least 10 feet in straight line, gain +5 to attack's damage or push target 10 feet away",
    
    "Crossbow Expert": "• Ignore loading property of crossbows\n• No disadvantage on ranged attacks within 5 feet\n• When you attack with one-handed weapon, can make bonus action attack with hand crossbow",
    
    "Defensive Duelist": "• When wielding finesse weapon you're proficient with, use reaction to add proficiency bonus to AC against one melee attack",
    
    "Dual Wielder": "• +1 AC when wielding separate melee weapons\n• Can dual wield non-light weapons\n• Can draw/stow two weapons at once",
    
    "Dungeon Delver": "• Advantage on Perception/Investigation to detect secret doors\n• Advantage on saves vs traps\n• Resistance to trap damage\n• Can search for traps at normal pace",
    
    "Durable": "• Increase Constitution by 1 (max 20)\n• When rolling Hit Dice to regain HP, minimum recovery = twice Constitution modifier",
    
    "Elemental Adept": "• Choose acid, cold, fire, lightning, or thunder damage\n• Spells ignore resistance to chosen damage type\n• Treat 1s on damage dice as 2s for chosen damage type",
    
    "Grappler": "• Advantage on attacks vs creatures you're grappling\n• Can use action to try to pin grappled creature (both restrained)\n• Can grapple creatures up to one size larger",
    
    "Great Weapon Master": "• On critical hit or reducing creature to 0 HP, make melee weapon attack as bonus action\n• Before melee attack with heavy weapon, take -5 penalty to attack roll for +10 damage",
    
    "Healer": "• Stabilize creature with healer's kit (no check required)\n• As action, heal 1d6+4+hit dice number of HP to creature with healer's kit (once per rest)",
    
    "Heavily Armored": "• Increase Strength by 1 (max 20)\n• Gain proficiency with heavy armor",
    
    "Heavy Armor Master": "• Increase Strength by 1 (max 20)\n• While wearing heavy armor, non-magical bludgeoning/piercing/slashing damage reduced by 3",
    
    "Inspiring Leader": "• Spend 10 minutes inspiring companions (up to 6 creatures)\n• Each gains temporary HP = level + Charisma modifier\n• Once per short/long rest",
    
    "Keen Mind": "• Increase Intelligence by 1 (max 20)\n• Always know which way is north\n• Know number of hours before next sunrise/sunset\n• Accurately recall anything seen/heard in past month",
    
    "Lightly Armored": "• Increase Strength or Dexterity by 1 (max 20)\n• Gain proficiency with light armor",
    
    "Linguist": "• Increase Intelligence by 1 (max 20)\n• Learn three languages\n• Create ciphers that others can't decipher without magic",
    
    "Lucky": "• Gain 3 luck points (regain after long rest)\n• Spend luck point to roll additional d20 on attack/save/ability check\n• Choose which d20 to use",
    
    "Mage Slayer": "• Advantage on saves vs spells cast within 5 feet\n• When creature within 5 feet casts spell, use reaction to make melee attack\n• When damaging concentrating creature, it has disadvantage on concentration save",
    
    "Magic Initiate": "• Choose class: learn two cantrips and one 1st-level spell from that class's list\n• Can cast 1st-level spell once per long rest using spellcasting ability or original ability",
    
    "Martial Adept": "• Learn two maneuvers from Battle Master archetype\n• Gain one superiority die (d6)\n• Die is used for maneuver saves and refreshes on short/long rest",
    
    "Medium Armor Master": "• No disadvantage on Stealth from medium armor\n• Can add +3 Dexterity modifier to AC (instead of +2) with medium armor",
    
    "Mobile": "• Speed increases by 10 feet\n• Dash action difficult terrain costs no extra movement\n• After melee attack (hit or miss), don't provoke opportunity attacks from that creature",
    
    "Moderately Armored": "• Increase Strength or Dexterity by 1 (max 20)\n• Gain proficiency with medium armor and shields",
    
    "Mounted Combatant": "• Advantage on melee attacks vs unmounted creatures smaller than mount\n• Can force attack targeting mount to target you instead\n• Mount takes no damage on successful Dexterity save (half on fail)",
    
    "Observant": "• Increase Intelligence or Wisdom by 1 (max 20)\n• +5 bonus to passive Perception and Investigation\n• Can read lips of creatures you can see speaking language you know",
    
    "Polearm Master": "• Make bonus action attack with opposite end of glaive/halberd/quarterstaff (d4)\n• Opportunity attacks when creatures enter your reach with glaive/halberd/pike/quarterstaff",
    
    "Resilient": "• Choose one ability score, increase by 1 (max 20)\n• Gain proficiency in saving throws using that ability",
    
    "Ritual Caster": "• Choose class, learn two 1st-level ritual spells from that class\n• Can copy ritual spells into ritual book (time and cost)\n• Can cast ritual spells from book",
    
    "Savage Attacker": "• Once per turn, reroll melee weapon damage dice and use either total",
    
    "Sentinel": "• Opportunity attacks stop target's movement\n• Can make opportunity attacks even if target took Disengage\n• When creature within 5 feet attacks target other than you, use reaction to make melee attack",
    
    "Sharpshooter": "• No disadvantage on long range attacks\n• Ignore half and three-quarters cover\n• Before ranged attack, take -5 penalty to attack roll for +10 damage",
    
    "Shield Master": "• Add shield's AC bonus to Dexterity saves vs spells/effects targeting only you\n• Use reaction to take no damage on successful Dexterity save (instead of half)\n• Shove as bonus action after Attack action",
    
    "Skilled": "• Gain proficiency in any combination of three skills or tools",
    
    "Skulker": "• Hide when only lightly obscured\n• Missed ranged attacks don't reveal position\n• No disadvantage on Perception checks in dim light",
    
    "Spell Sniper": "• Double spell attack range\n• Ignore half and three-quarters cover with spell attacks\n• Learn one cantrip requiring spell attack",
    
    "Tavern Brawler": "• Increase Strength or Constitution by 1 (max 20)\n• Proficiency with improvised weapons\n• Unarmed strike uses d4\n• Grapple as bonus action after hitting with unarmed strike or improvised weapon",
    
    "Tough": "• Gain 2 additional HP per level (retroactive)\n• +2 HP at 1st level",
    
    "War Caster": "• Advantage on Constitution saves for concentration\n• Can perform somatic components with weapons/shields in hands\n• Can use reaction to cast spell (single target) instead of opportunity attack",
    
    "Weapon Master": "• Increase Strength or Dexterity by 1 (max 20)\n• Gain proficiency with four weapons of choice",

    # RACIAL OPTIONAL FEATS (Tasha's Cauldron of Everything)
    "Bountiful Luck": "Halfling Only\n• When ally you can see within 30 feet rolls 1 on d20, use reaction to let them reroll",
    
    "Dragon Fear": "Dragonborn Only\n• Increase Strength/Constitution/Charisma by 1 (max 20)\n• Replace Breath Weapon with exhalation of fear (Wisdom save or frightened for 1 minute)",
    
    "Dragon Hide": "Dragonborn Only\n• Increase Strength/Constitution/Charisma by 1 (max 20)\n• Grow retractable claws (1d4 slashing, finesse)\n• Scales grant AC 13 + Dexterity modifier when unarmored",
    
    "Dwarven Fortitude": "Dwarf Only\n• Increase Constitution by 1 (max 20)\n• When you take Dodge action, can spend Hit Die to heal (roll + Constitution modifier)",
    
    "Elven Accuracy": "Elf or Half-Elf Only\n• Increase Dexterity/Intelligence/Wisdom/Charisma by 1 (max 20)\n• When you have advantage on attack roll using Dexterity/Intelligence/Wisdom/Charisma, reroll one die",
    
    "Fade Away": "Gnome Only\n• Increase Dexterity or Intelligence by 1 (max 20)\n• When you take damage, use reaction to turn invisible until end of next turn or attack/cast spell",
    
    "Fey Teleportation": "High Elf Only\n• Increase Intelligence or Charisma by 1 (max 20)\n• Learn Misty Step, can cast once per long rest using Intelligence/Charisma",
    
    "Flames of Phlegethos": "Tiefling Only\n• Increase Intelligence or Charisma by 1 (max 20)\n• Reroll fire damage 1s, must use new roll\n• When casting fire spell, shed dim light and creatures provoke opportunity attacks",
    
    "Infernal Constitution": "Tiefling Only\n• Increase Constitution by 1 (max 20)\n• Resistance to cold and poison damage\n• Advantage on saves vs poison",
    
    "Orcish Fury": "Half-Orc Only\n• Increase Strength or Constitution by 1 (max 20)\n• Proficiency with one weapon of choice\n• When you hit with weapon attack, roll one additional damage die\n• When Relentless Endurance triggers, make weapon attack as reaction",
    
    "Second Chance": "Halfling Only\n• Increase Dexterity/Constitution/Charisma by 1 (max 20)\n• When creature hits you with attack, use reaction to force reroll (once per rest)",
    
    "Squat Nimbleness": "Dwarf or Small Race Only\n• Increase Strength or Dexterity by 1 (max 20)\n• Speed increases by 5 feet\n• Advantage on escape attempts from grapples\n• Proficiency in Acrobatics or Athletics",
    
    "Wood Elf Magic": "Wood Elf Only\n• Learn one druid cantrip\n• Learn Longstrider or Pass Without Trace, can cast once per long rest using Wisdom",
    
    # XANATHAR'S GUIDE TO EVERYTHING FEATS
    "Chef": "• Increase Constitution or Wisdom by 1 (max 20)\n• Cook special food during short rest, creatures gain 1d8 temp HP\n• Cook special treats (4), eat as bonus action to regain 1d8 HP\n• Gain proficiency with cook's utensils",
    
    "Crusher": "• Increase Strength or Constitution by 1 (max 20)\n• Once per turn when hitting with bludgeoning attack, push target 5 feet\n• Critical hit gives advantage on attacks vs that creature until start of next turn",
    
    "Eldritch Adept": "• Prerequisite: Spellcasting or Pact Magic feature\n• Learn one Eldritch Invocation (meets prerequisites)\n• Can change invocation on level up",
    
    "Fey Touched": "• Increase Intelligence/Wisdom/Charisma by 1 (max 20)\n• Learn Misty Step and one 1st-level divination/enchantment spell\n• Can cast each once per long rest using spellcasting ability",
    
    "Fighting Initiate": "• Learn one Fighting Style option\n• Can be changed on level up",
    
    "Gunner": "• Increase Dexterity by 1 (max 20)\n• Ignore loading property of firearms\n• No disadvantage on ranged attacks within 5 feet\n• Proficiency with firearms",
    
    "Metamagic Adept": "• Prerequisite: Spellcasting or Pact Magic feature\n• Learn two Metamagic options\n• Gain 2 sorcery points (refresh on long rest)",
    
    "Piercer": "• Increase Strength or Dexterity by 1 (max 20)\n• Once per turn, reroll piercing damage die\n• Critical hit with piercing weapon rolls one additional damage die",
    
    "Poisoner": "• Proficiency with poisoner's kit\n• Apply poison to weapon as bonus action\n• Creatures have disadvantage on poison save if below half HP\n• Create potent poison (1 hour, 100gp)",
    
    "Shadow Touched": "• Increase Intelligence/Wisdom/Charisma by 1 (max 20)\n• Learn Invisibility and one 1st-level illusion/necromancy spell\n• Can cast each once per long rest using spellcasting ability",
    
    "Skill Expert": "• Increase one ability score by 1 (max 20)\n• Gain proficiency in one skill\n• Gain expertise in one skill you're proficient with",
    
    "Slasher": "• Increase Strength or Dexterity by 1 (max 20)\n• Critical hit reduces target's speed to 0 until start of your next turn\n• When hitting with slashing weapon, target has disadvantage on attacks until start of your next turn",
    
    "Telekinetic": "• Increase Intelligence/Wisdom/Charisma by 1 (max 20)\n• Learn Mage Hand (invisible if you know it)\n• As bonus action, shove creature 5 feet (Strength save)",
    
    "Telepathic": "• Increase Intelligence/Wisdom/Charisma by 1 (max 20)\n• Learn Detect Thoughts, can cast once per long rest using spellcasting ability\n• Can communicate telepathically with creatures you can see within 60 feet",
    
    # TASHA'S CAULDRON ADDITIONAL FEATS
    "Artificer Initiate": "• Learn one cantrip and one 1st-level spell from Artificer list\n• Can cast 1st-level spell once per long rest using Intelligence\n• Gain proficiency with one type of artisan's tools",
    
    "Gift of the Gem Dragon": "• Increase Intelligence/Wisdom/Charisma by 1 (max 20)\n• When taking damage from creature within 10 feet, use reaction to push them 10 feet (Constitution save)\n• Can use once per long rest",
    
    "Gift of the Chromatic Dragon": "• As bonus action, imbue weapon with elemental damage for 1 minute\n• As reaction, gain resistance to acid/cold/fire/lightning/poison damage until start of next turn\n• Each use recharges after long rest",
    
    "Gift of the Metallic Dragon": "• Learn Cure Wounds, can cast once per long rest using spellcasting ability\n• As reaction, protect creature within 5 feet with protective wings (+1d4 to AC vs one attack)",
    
    "Strixhaven Initiate": "• Choose Strixhaven college, learn two cantrips and one 1st-level spell from that college\n• Can cast 1st-level spell once per long rest using spellcasting ability",
    
    # ONE D&D/2024 UPDATES
    "Charger": "• When you use Dash action, can make one weapon attack as bonus action with +1d8 damage\n• If you move at least 20 feet, push target 10 feet (Strength save)",
    
    "Grappler": "• Advantage on attacks vs grappled creatures\n• Can grapple as bonus action\n• Creatures you grapple have speed 0 and can't benefit from bonuses to speed",
    
    "Heavy Armor Master": "• Increase Strength by 1 (max 20)\n• While wearing heavy armor, bludgeoning/piercing/slashing damage reduced by 3\n• When hit by critical hit, damage reduced by extra 5",
    
    "Lightly Armored": "• Increase Strength or Dexterity by 1 (max 20)\n• Gain proficiency with light armor\n• Gain proficiency with shields if not already proficient",
    
    "Lucky": "• Gain 3 luck points (regain 1 after short rest, all after long rest)\n• Spend luck point after rolling d20 to roll additional d20, choose which to use",
    
    "Magic Initiate": "• Choose Arcane/Divine/Primal magic, learn two cantrips and one 1st-level spell from that list\n• Can cast 1st-level spell at lowest level once per long rest",
    
    "Martial Adept": "• Learn two maneuvers from Battle Master\n• Gain two superiority dice (d6)\n• Regain one die after short rest, all after long rest",
    
    "Savage Attacker": "• Once per turn, reroll weapon damage dice and use either total\n• When you score critical hit, roll one additional weapon damage die",
    
    "Tavern Brawler": "• Increase Strength or Constitution by 1 (max 20)\n• Unarmed strike uses d4\n• Proficiency with improvised weapons\n• When you hit with unarmed strike or improvised weapon, can grapple as bonus action",
    
    "Tough": "• Gain 2 additional HP per level\n• When you roll Hit Die to regain HP, minimum recovery = twice Constitution modifier",
    
    "War Caster": "• Advantage on Constitution saves for concentration\n• Can perform somatic components with weapons/shields in hands\n• Can use reaction to cast spell (single target) instead of opportunity attack"
}










all_ability_data = {
    # Barbarian abilities
    "Extra Attack": "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.",

    "Ability Score Improvement": "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."
}



# ------------------------------------------------------------ class dicts -------------------------------------------------------------------------------------------------------------------------

arti_dict = {}


barb_dict = {
            "Rage": "In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.\n\nWhile raging, you gain the following benefits if you aren't wearing heavy armor:\n• You have advantage on Strength checks and Strength saving throws\n• When you make a melee weapon attack using Strength, you gain a +2 bonus to damage rolls\n• You have resistance to bludgeoning, piercing, and slashing damage\n\nYour rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then.",
           
            "Unarmored Defense": "While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
            
            "Danger Sense": "You gain an uncanny sense of when things nearby aren't as they should be, giving you an edge when you dodge away from danger.\n\nYou have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated.",
            
            "Reckless Attack": "Starting at 2nd level, you can throw aside all concern for defense to attack with fierce desperation.\n\nWhen you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.",
            
            "Fast Movement": "Starting at 5th level, your speed increases by 10 feet while you aren't wearing heavy armor.",
            
            "Feral Instinct": "By 7th level, your instincts are so honed that you have advantage on initiative rolls.\n\nAdditionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn.",
            
            "Instinctive Pounce": "At 7th level, as part of the bonus action you take to enter your rage, you can move up to half your speed.",
            
            "Brutal Critical": "Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack.\nThis increases to two additional dice at 13th level and three additional dice at 17th level.",
            
            "Relentless Rage": "Starting at 11th level, your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead.\nEach time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10.",
           
            "Persistent Rage": "Beginning at 15th level, your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it.",      
}

bard_dict = {}

cler_dict = {}

drui_dict = {}

figh_dict = {}

monk_dict = {}


pala_dict = {
"Divine Sense": "The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like heavenly music in your ears. As an action, you can open your awareness to detect such forces. Until the end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity (the vampire Count Strahd von Zarovich, for instance). Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the Hallow spell.\nYou can use this feature a number of times equal to 1 + your Charisma modifier. When you finish a long rest, you regain all expended uses.",

#"Lay on Hands": "",
"Fighting Style": "",
"Spellcasting":"",
"Divine Smite":"",
"Divine Health": "",
"Harness Divine Power (Optional)":"",
"Ability Score Improvement":"",
"Martial Versatility (Optional)":"",
"Aura of Protection":"",
"Aura of Courage":"",
"Improved Divine Smite":"",
"Cleansing Touch":"",
"Aura improvements":""
}

rang_dict = {
}

rogu_dict = {
}

sorc_dict = {
}

wiza_dict = {
}

warl_dict = {
}

# -------------------------------------------------------------- subclass dicts -------------------------------------------------------------------------------------------------------------------------

zeal_dict = {
            "Divine Fury" : "Starting when you choose this path at 3rd level, you can channel divine fury into your weapon strikes. While you're raging, the first creature you hit on each of your turns with a weapon attack takes extra damage equal to 1d6 + half your Barbarian level. The extra damage is necrotic or radiant; you choose the type of damage when you gain this feature.",
            
            "Warrior of the Gods": "At 3rd level, your soul is marked for endless battle. If a spell, such as Raise Dead, has the sole effect of restoring you to life (but not undeath), the caster doesn't need material components to cast the spell on you.",
           
            "Fanatical Focus": "Starting at 6th level, the divine power that fuels your rage can protect you. If you fail a saving throw while raging, you can reroll it, and you must use the new roll. You can use this ability only once per rage.",
            
            "Zealous Presence": "At 10th level, you learn to channel divine power to inspire zealotry in others. As a bonus action, you unleash a battle cry infused with divine energy. Up to ten other creatures of your choice within 60 feet of you that can hear you gain advantage on attack rolls and saving throws until the start of your next turn. \nOnce you use this feature, you can’t use it again until you finish a long rest.",
           
            "Rage beyond Death": "Beginning at 14th level, the divine power that fuels your rage allows you to shrug off fatal blows.\n\nWhile you're raging, having 0 hit points doesn’t knock you unconscious. You still must make death saving throws, and you suffer the normal effects of taking damage while at 0 hit points. However, if you would die due to failing death saving throws, you don’t die until your rage ends, and you die then only if you still have 0 hit points."
}

ance_dict = {
            "Ancestral Protectors": "Starting when you choose this path at 3rd level, spectral warriors appear when you enter your rage. While you're raging, the first creature you hit with an attack on your turn becomes the target of the warriors, which hinder its attacks. Until the start of your next turn, that target has disadvantage on any attack roll that isn't against you, and when the target hits a creature other than you with an attack, that creature has resistance to the damage dealt by the attack. The effect on the target ends early if your rage ends.",
            
            "Spirit Shield": "Beginning at 6th level, the guardian spirits that aid you can provide supernatural protection to those you defend. If you are raging and another creature you can see within 30 feet of you takes damage, you can use your reaction to reduce that damage by 2d6.\n\nWhen you reach certain levels in this class, you can reduce the damage by more: by 3d6 at 10th level and by 4d6 at 14th level.",

            "Consult the Spirits": "At 10th level, you gain the ability to consult with your ancestral spirits. When you do so, you cast the Augury or Clairvoyance spell, without using a spell slot or material components. Rather than creating a spherical sensor, this use of clairvoyance invisibly summons one of your ancestral spirits to the chosen location. Wisdom is your spellcasting ability for these spells.\nAfter you cast either spell in this way, you can't use this feature again until you finish a short or long rest.",

            "Vengeful Ancestors": "At 14th level, your ancestral spirits grow powerful enough to retaliate. When you use your Spirit Shield to reduce the damage of an attack, the attacker takes an amount of force damage that your Spirit Shield prevents."
}

batt_dict = {
            "Restriction: Dwarves Only": "Only dwarves can follow the Path of the Battlerager. The battlerager fills a particular niche in dwarven society and culture.\nYour DM can lift this restriction to better suit the campaign. The restriction exists for the Forgotten Realms. It might not apply to your DM's setting or your DM's version of the Realms.",

            "Battlerager Armor": "When you choose this path at 3rd level, you gain the ability to use spiked armor as a weapon.\n\nWhile you are wearing spiked armor and are raging, you can use a bonus action to make one melee weapon attack with your armor spikes against a target within 5 feet of you. If the attack hits, the spikes deal 1d4 piercing damage. You use your Strength modifier for the attack and damage rolls.\n\nAdditionally, when you use the Attack action to grapple a creature, the target takes 3 piercing damage if your grapple check succeeds.",

            "Reckless Abandon": "Beginning at 6th level, when you use Reckless Attack while raging, you also gain temporary hit points equal to your Constitution modifier (minimum of 1). They vanish if any of them are left when your rage ends.",

            "Battlerager Charge": "Beginning at 10th level, you can take the Dash action as a bonus action while you are raging.",

            "Spiked Retribution": "Starting at 14th level, when a creature within 5 feet of you hits you with a melee attack, the attacker takes 3 piercing damage if you are raging, aren't incapacitated, and are wearing spiked armor."
}

beas_dict = {}

bers_dict = {}

gian_dict = {}

            



            
            
            
        
        # Class-specific abilities
CLASS_ABILITIES_LIST = {


            "Artificer": [
(1, ["Magical Tinkering", "Spellcasting"]),
(2, ["Infuse Item"]),
(3, ["The Right Tool for the Job"]),
(4,["Ability Score Improvement"]),
(6,["Tool Expertise"]),
(7,["Flash of Genius"]),
(8,["Ability Score Improvement"]),
(10,["Magic Item Adept"]),
(11,["Spell-Storing Item"]),
(12,["Ability Score Improvement"]),
(14,["Magic Item Savant"]),
(16,["Ability Score Improvement"]),
(18,["Magic Item Master"]),
(19,["Ability Score Improvement"]),
(20,["Soul of Artifice"])
],

            "Barbarian": [
(1,["Rage", "Unarmored Defense"]),
(2,["Reckless Attack", "Danger Sense"]),
(4,["Ability Score Improvement"]),
(5,["Extra Attack","Fast Movement"]),
(7,["Feral Instinct","Instinctive Pounce"]),
(8,["Ability Score Improvement"]),
(9,["Brutal Critical"]),
(10,["Primal Knowledge (Optional)"]),
(11,["Relentless Rage"]),
(12,["Ability Score Improvement"]),
(13,["Brutal Critical (2 dice)"]),
(15,["Persistent Rage"]),
(16,["Ability Score Improvement"]),
(17,["Brutal Critical (3 dice)"]),
(18,["Indomitable Might"]),
(19,["Ability Score Improvement"]),
(20,["Primal Champion"])
],
            
            "Bard": [
(1,["Spellcasting", "Bardic Inspiration (d6)"]),
(2,["Jack of All Trades", "Song of Rest (d6)", "Magical Inspiration (Optional)"]),
(3,["Expertise"]),
(4,["Ability Score Improvement","Bardic Versatility (Optional)"]),
(5,["Bardic Inspiration (d8)", "Font of Inspiration"]),
(6, ["Countercharm"]),
(7,["Feral Instinct","Instinctive Pounce"]),
(8,["Ability Score Improvement", "Bardic Versatility (Optional)"]),
(9,["Song of Rest (d8)"]),
(10,["Bardic Inspiration (d10)", "Expertise", "Magical Secrets"]),
(12,["Ability Score Improvement", "Bardic Versatility (Optional)"]),
(13,["Song of Rest (d10)"]),
(14,["Magical Secrets"]),
(15,["Bardic Inspiration (d12)"]),
(16,["Ability Score Improvement", "Bardic Versatility (Optional)"]),
(17,["Song of Rest (d12)"]),
(18,["Magical Secrets"]),
(19,["Ability Score Improvement", "Bardic Versatility (Optional)"]),
(20,["Superior Inspiration"])
],

            "Cleric":[
(1,["Spellcasting", "Divine Domain"]),
(2,["Channel Divinity (x1)", "Harness Divine Power (Optional)"]),
(4,["Ability Score Improvement", "Cantrip Versatility (Optional)"]),
(5,["Destroy Undead (CR 1/2)"]),
(6,["Channel Divinity (x2)"]),
(8,["Ability Score Improvement", "Destroy Undead (CR 1)", "Cantrip Versatility (Optional)"]),
(10,["Divine Intervention"]),
(11,["Destroy Undead (CR 2)"]),
(12,["Ability Score Improvement", "Cantrip Versatility (Optional)"]),
(14,["Destroy Undead (CR 3)"]),
(16,["Ability Score Improvement", "Cantrip Versatility (Optional)"]),
(17,["Destroy Undead (CR 4)"]),
(18,["Channel Divinity (x3)"]),
(19,["Ability Score Improvement", "Cantrip Versatility (Optional)"]),
(20,["Divine Intervention improvement"])
],

            "Druid": [
(1,["Druidic", "Spellcasting"]),
(2,["Wild Shape", "Wild Companion (Optional)"]),
(4,["Wild Shape improvement", "Ability Score Improvement", "Cantrip Versatility (Optional)"]),
(8,["Wild Shape improvement", "Ability Score Improvement", "Cantrip Versatility (Optional)"]),
(12,["Ability Score Improvement", "Cantrip Versatility (Optional)"]),
(16,["Ability Score Improvement", "Cantrip Versatility (Optional)"]),
(18,["Timeless Body", "Beast Spells"]),
(19,["Ability Score Improvement", "Cantrip Versatility (Optional)"]),
(20,["Archdruid"])
],

            "Fighter": [
(1,["Fighting Style", "Second Wind"]),
(2,["Action Surge (x1)"]),
(4,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(5,["Extra Attack (x1)"]),
(6,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(8,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(9,["Indomitable (x1)"]),
(11,["Extra Attack (x2)"]),
(12,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(13,["Indomitable (x2)"]),
(14,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(16,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(17,["Action Surge (x2)", "Indomitable (x3)"]),
(19,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(20,["Extra Attack (x3)"])
],


            "Monk": [
(1,["Unarmored Defense", "Martial Arts"]),
(2,["Ki, Unarmored Movement", "Dedicated Weapon (Optional)"]),
(3,["Deflect Missiles", "Ki-Fueled Attack (Optional)"]),
(4,["Ability Score Improvement", "Slow Fall", "Quickened Healing (Optional)"]),
(5,["Extra Attack", "Stunning Strike", "Focused Aim (Optional)"]),
(6,["Ki-Empowered Strikes"]),
(7,["Evasion", "Stillness of Mind"]),
(8,["Ability Score Improvement"]),
(9,["Unarmored Movement improvement"]),
(10,["Purity of Body"]),
(12,["Ability Score Improvement"]),
(13,["Tongue of the Sun and Moon"]),
(14,["Diamond Soul"]),
(15,["Timeless Body"]),
(16,["Ability Score Improvement"]),
(18,["Empty Body"]),
(19,["Ability Score Improvement"]),
(20,["Perfect Self"])
        ],

            "Paladin": [
(1,["Divine Sense", "Lay on Hands"]),
(2,["Fighting Style", "Spellcasting", "Divine Smite"]),
(3,["Divine Health", "Harness Divine Power (Optional)"]),
(4,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(5,["Extra Attack"]),
(6,["Aura of Protection"]),
(8,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(10,["Aura of Courage"]),
(11,["Improved Divine Smite"]),
(12,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(14,["Cleansing Touch"]),
(16,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(18,["Aura improvements"]),
(19,["Ability Score Improvement", "Martial Versatility (Optional)"])
        ],


            "Ranger": [
(1,["Favored Enemy", "Natural Explorer", "Deft Explorer (Optional)", "Favored Foe (Optional)"]),
(2,["Fighting Style", "Spellcasting", "Spellcasting Focus (Optional)"]),
(3,["Primeval Awareness", "Primal Awareness (Optional)"]),
(4,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(5,["Extra Attack"]),
(6,["Favored Enemy Improvement", "Natural Explorer Improvement", "Deft Explorer Improvement (Optional)"]),
(8,["Ability Score Improvement", "Land's Stride", "Martial Versatility (Optional)"]),
(10,["Natural Explorer Improvement", "Hide in Plain Sight", "Deft Explorer Feature (Optional)", "Nature's Veil (Optional)"]),
(12,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(14,["Favored Enemy Improvement", "Vanish"]),
(16,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(18,["Feral Senses"]),
(19,["Ability Score Improvement", "Martial Versatility (Optional)"]),
(20,["Foe Slayer"])
        ],

            "Rogue": [
(1,["Expertise", "Sneak Attack", "Thieves Cant"]),
(2,["Cunning Action"]),
(3,["Steady Aim (Optional)"]),
(4,["Ability Score Improvement"]),
(5,["Uncanny Dodge"]),
(6,["Expertise"]),
(7,["Evasion"]),
(8,["Ability Score Improvement"]),
(10,["Ability Score Improvement"]),
(11,["Reliable Talent"]),
(12,["Ability Score Improvement"]),
(14,["Blindsense"]),
(15,["Slippery Mind"]),
(16,["Ability Score Improvement"]),
(18,["Elusive"]),
(19,["Ability Score Improvement"]),
(20,["Stroke of Luck"])
        ],

            "Sorcerer": [
(1,["Spellcasting"]),
(2,["Font of Magic"]),
(3,["Metamagic"]),
(4,["Ability Score Improvement", "Sorcerous Versatility (Optional)"]),
(5,["Magical Guidance (Optional)"]),
(8,["Ability Score Improvement", "Sorcerous Versatility (Optional)"]),
(10,["Metamagic"]),
(12,["Ability Score Improvement", "Sorcerous Versatility (Optional)"]),
(16,["Ability Score Improvement", "Sorcerous Versatility (Optional)"]),
(17,["Metamagic"]),
(19,["Ability Score Improvement", "Sorcerous Versatility (Optional)"]),
(20,["Sorcerous Restoration"])
        ],

            "Warlock": [
(1,["Pact Magic"]),
(2,["Eldritch Invocations"]),
(3,["Pact Boon"]),
(4,["Ability Score Improvement", "Eldritch Versatility (Optional)"]),
(8,["Ability Score Improvement", "Eldritch Versatility (Optional)"]),
(11,["Mystic Arcanum (6th level)"]),
(12,["Ability Score Improvement", "Eldritch Versatility (Optional)"]),
(13,["Mystic Arcanum (7th level)"]),
(15,["Mystic Arcanum (8th level)"]),
(16,["Ability Score Improvement", "Eldritch Versatility (Optional)"]),
(17,["Mystic Arcanum (9th level)"]),
(19,["Ability Score Improvement", "Eldritch Versatility (Optional)"]),
(20,["Eldritch Master"])
        ],

            "Wizard": [
(1,["Spellcasting, Arcane Recovery"]),
(3,["Cantrip Formulas (Optional)"]),
(4,["Ability Score Improvement"]),
(8,["Ability Score Improvement"]),
(12,["Ability Score Improvement"]),
(16,["Ability Score Improvement"]),
(18,["Spell Mastery"]),
(19,["Ability Score Improvement"]),
(20,["Signature Spells"])
        ],



        
"Ancestral Guardian": [
(3,["Ancestral Protectors"]),
(6,["Spirit Shield"]), 
(10,["Consult the Spirits"]), 
(14,[ "Vengeful Ancestors"])
],

"Battlerager": [
(3,["Restriction: Dwarves Only", "Battlerager Armor"]),
(6,["Reckless Abandon"]), 
(10,["Battlerager Charge"]), 
(14,[ "Spiked Retribution"])
],

"Beast": [
(3,["Form of the Beast"]),
(6,["Bestial Soul"]), 
(10,["Infectious Fury"]), 
(14,[ "Call the Hunt"])
],

"Berserker": [
(3,["Frenzy"]),
(6,["Mindless Rage"]), 
(10,["Intimidating Presence"]), 
(14,[ "Retaliation"])
],

"Giant": [
(3,["Giant’s Power", "Giant’s Havoc"]),
(6,["Elemental Cleaver"]), 
(10,["Mighty Impel"]), 
(14,[ "Demiurgic Colossus"])
],

"Zealot": [
(3,["Divine Fury", "Warrior of the Gods"]),
(6,["Fanatical Focus"]), 
(10,["Zealous Presence"]), 
(14,[ "Rage beyond Death"])
],

"Zealot": [
(3,["Divine Fury", "Warrior of the Gods"]),
(6,["Fanatical Focus"]), 
(10,["Zealous Presence"]), 
(14,[ "Rage beyond Death"])
],

"Zealot": [
(3,["Divine Fury", "Warrior of the Gods"]),
(6,["Fanatical Focus"]), 
(10,["Zealous Presence"]), 
(14,[ "Rage beyond Death"])
],

}










CLASS_BASED_DICT = {

"Artificer": arti_dict,
"Barbarian": barb_dict,
"Bard": bard_dict,
"Cleric": cler_dict,
"Druid": drui_dict,
"Fighter": figh_dict,
"Monk": monk_dict,
"Paladin": pala_dict,
"Ranger": rang_dict,
"Rogue": rogu_dict,
"Sorcerer": sorc_dict,
"Warlock": warl_dict,
"Wizard": wiza_dict,

"Zealot": zeal_dict,
"Ancestral Guardian": ance_dict,
"Battlerager": batt_dict,
"Beast": beas_dict,
"Berserker": bers_dict,
"Giant": gian_dict,


}



def setup_ability_data(self):
    """Legacy method for backward compatibility"""
    self.class_abilities = CLASS_ABILITIES_LIST
    self.subclass_abilities = SUBCLASS_ABILITIES
    self.class_based_dict = CLASS_BASED_DICT

