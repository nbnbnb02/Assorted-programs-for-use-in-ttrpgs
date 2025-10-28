#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 23:52:18 2025

@author: nicholasbyrne
"""
import random
# Character Creator
 
# 
# =============================================================================
def CC(option, multiclass, class_list="better"):            
# =============================================================================
    
    # Lists
    # Race
    Lineages = {
            "Common": ['Dragonborn','Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Tiefling'],
            "Exotic": ['Aarakocra', 'Aasimar', 'Changeling', 'Deep Gnome', 'Duergar', 'Eladrin', 'Fairy', 'Firbolg', 
            'Genasi', 'Githyanki', 'Githzerai', 'Goliath', 'Harengon', 'Kenku', 'Locathah', 'Owlin', 'Satyr', 'Sea Elf', 
            'Shadar-Kai', 'Tabaxi', 'Tortle', 'Triton', 'Verdan', 'Warforged'],
            "Monstrous": ['Bugbear', 'Centaur', 'Goblin', 'Grung', 'Hobgoblin', 'Kobold', 'Lizardfolk', 'Minotaur', 
            'Orc', 'Shifter', 'Yuan-Ti']}
    sublist = ['Dragonborn','Dwarf','Elf','Gnome','Halfling','Tiefling','Aasimar','Shifter','Genasi']
    Dragonborn = {"Chromatic": ['Black', 'Blue', 'Green', 'Red', 'White'], 
                  "Gem": ['Amethyst', 'Crystal', 'Emerald', 'Saphire', 'Topaz'],
                  "Metallic": ['Brass', 'Bronze', 'Copper', 'Gold', 'Silver']}
    Dwarf = ['Hill', 'Mountain']
    Elf = ['Dark', 'High', 'Wood', 'Pallid']
    Gnome = ['Forest', 'Rock']
    Halfling = ['Lightfoot', 'Stout', 'Ghostwise', 'Lotsuden']
    Tiefling = {"Norm sub":['Asmodeus', 'Baalzebul', 'Dispater', 'Fierna', 'Glasya', 'Levistus', 'Mammon', 
                            'Mephistopheles', 'Zariel'],
                "Variant": ['Variant']}
    Aasimar = ['Protector', 'Scourge', 'Fallen']
    Shifter = ['Werebear', 'Wererat', 'Weretiger', 'Werewolf (wolf)', 'Werewolf (dog)']
    Genasi = ['Air', 'Fire', 'Water', 'Earth']
    
    
    skin_tone = ['Very dark','Dark','Slightly Darker', 'Average Tone', 'Slightly Pale', 'Pale', 'Very Pale']
    skin_vibrance = ['Vivid','Bright','Average Vibrance', 'Dull', 'De-saturated']

    skin_normal = ['Very dark','Brown','Tan', 'Average Tan', 'Pale', 'Ghostly White', 'Asian']
    skin_unnatural = ['Black','Grey','White/Silver', 'Red', 'Green', 'Blue', 'Yellow/Gold', 'Orange/Copper/Bronze', 
    'Pink', 'Purple','Brown']
    skin_Gobo = ['Green','Brown','Grey','Yellow']
    skin_Fur = ['Black','Brown','Grey','White', 'Almond','Reddish']

    unnaturalC_races = {'Tiefling', 'Aarakocra', 'Eladrin', 'Fairy','Firbolg', 'Kenku', 'Locathah', 'Satyr', 'Sea Elf',
    'Tabaxi', 'Tortle', 'Triton', 'Verdan', 'Grung','Kobold', 'Lizardfolk', 'Shifter', 'Warforged', 'Yuan-Ti'}
    normalC_races = {'Dwarf','Elf','Gnome','Half-Elf','Halfling','Human','Aasimar','Genasi','Satyr','Shifter'}
    GoboC_races = {'Half-Orc','Githyanki','Githzerai','Goblin','Hobgoblin','Orc'}
    FurC_races = {'Harengon','Bugbear','Centaur','Minotaur','Owlin'}
    TonalC_races = {'Changeling','Dragonborn','Deep Gnome','Duergar','Goliath','Sea Elf','Shadar-Kai'}

    H1to2 = ['Fairy']
    H2to3 = ['Kobold']
    H26to36 = ['Halfling','Grung']
    H3to4 = ['Gnome','Deep Gnome','Goblin','Verdan']
    H36to5 = ['Dwarf','Duergar','Harengon']  
    H46to6 = ['Kenku','Changeling','Owlin','Tortle']
    H410to64 = ['Aasimar','Aarakocra','Genasi','Human','Tiefling','Lizardfolk','Elf','Eladrin','Sea Elf','Shadar-Kai',
    'Half-Elf','Half-Orc','Hobgoblin','Yuan-Ti','Tabaxi','Triton','Locathah','Satyr'] 
    H55to7 = ['Githyanki','Githzerai','Dragonborn','Orc','Centaur','Shifter','Warforged']
    H62to8 = ['Bugbear','Firbolg','Goliath','Minotaur']
    
    Height_tuples = [
        (H1to2 , ['1\'0\"','1\'1\"','1\'2\"','1\'3\"','1\'4\"','1\'5\"','1\'6\"','1\'7\"','1\'8\"','1\'9\"','1\'10\"',
    '1\'11\"','2\'0\"']),
    (H2to3 , ['2\'0\"','2\'1\"','2\'2\"','2\'3\"','2\'4\"','2\'5\"','2\'6\"','2\'7\"','2\'8\"','2\'9\"','2\'10\"',
    '2\'11\"','3\'0\"']),
    (H26to36 , ['2\'6\"','2\'7\"','2\'8\"','2\'9\"','2\'10\"','2\'11\"','3\'0\"','3\'1\"','3\'2\"','3\'3\"','3\'4\"',
    '3\'5\"','3\'6\"']),
    (H3to4 , ['3\'0\"','3\'1\"','3\'2\"','3\'3\"','3\'4\"','3\'5\"','3\'6\"','3\'7\"','3\'8\"','3\'9\"','3\'10\"',
    '3\'11\"','4\'0\"']),
    (H36to5 , ['3\'6\"','3\'7\"','3\'8\"','3\'9\"','3\'10\"','3\'11\"','4\'0\"','4\'1\"','4\'2\"','4\'3\"','4\'4\"',
    '4\'5\"','4\'6\"','4\'7\"','4\'8\"','4\'9\"','4\'10\"','4\'11\"','5\'0\"']),
    (H46to6 , ['4\'6\"','4\'7\"','4\'8\"','4\'9\"','4\'10\"','4\'11\"','5\'0\"','5\'1\"','5\'2\"','5\'3\"','5\'4\"',
    '5\'5\"','5\'6\"','5\'7\"','5\'8\"','5\'9\"','5\'10\"','5\'11\"','6\'0\"']),
    (H410to64 , ['4\'10\"','4\'11\"','5\'0\"','5\'1\"','5\'2\"','5\'3\"','5\'4\"','5\'5\"','5\'6\"','5\'7\"','5\'8\"',
    '5\'9\"','5\'10\"','5\'11\"','6\'0\"','6\'1\"','6\'2\"','6\'3\"','6\'4\"']),
    (H55to7 , ['5\'5\"','5\'6\"','5\'7\"','5\'8\"','5\'9\"','5\'10\"','5\'11\"','6\'0\"','6\'1\"','6\'2\"','6\'3\"',
    '6\'4\"','6\'5\"','6\'6\"','6\'7\"','6\'8\"','6\'9\"','6\'10\"','6\'11\"','7\'0\"']),
    (H62to8 , ['6\'2\"','6\'3\"','6\'4\"','6\'5\"','6\'6\"','6\'7\"','6\'8\"','6\'9\"','6\'10\"','6\'11\"','7\'0\"',
    '7\'1\"','7\'2\"','7\'3\"','7\'4\"','7\'5\"','7\'6\"','7\'7\"','7\'8\"','7\'9\"','7\'10\"','7\'11\"','8\'0\"'])
    ]
    
    
    
    #Body
    BodyType = ['Malnourished','Lithe','Skinny','Average Body','Toned','Jacked','Athletic','Chubby','Plump','Fat']
    BodyTypeWarforged = ['Lithe','Skinny','Average Body','Toned','Jacked','Athletic']
    body = random.choice(BodyType)
    bodywarforged = random.choice(BodyTypeWarforged)
    
    # Age
    Age = ['Adolescent','Young Adult', 'Adult','Middle Age','Retiring','Old Age','Geriatric']    
    
    # Background
    Backgrounds = ['Anthropologist', 'Archaeologist', 'Athlete', 'Charlatan', 'City Watch', 'Clan Crafter', 
    'Cloistered Scholar', 'Courtier', 'Criminal', 'Entertainer', 'Faceless', 'Faction Agent', 'Far Traveler', 
    'Feylost', 'Fisher', 'Folk Hero', 'Giant Foundling', 'Gladiator', 'Guild Artisan', 'Guild Merchant', 
    'Haunted One', 'Hermit', 'House Agent', 'Inheritor', 'Investigator (SCAG)', 'Investigator (VRGR)', 'Knight', 
    'Knight of the Order', 'Marine', 'Mercenary Veteran', 'Noble', 'Outlander', 'Pirate', 'Rewarded', 'Ruined', 
    'Rune Carver', 'Sage', 'Sailor', 'Shipwright', 'Smuggler', 'Soldier', 'Spy', 'Urban Bounty Hunter', 'Urchin',
    'Uthgardt Tribe Member','Waterdhavian Noble','Witchlight Hand']
    
    # Classes
    
    
    Classes_all = {"Artificer": ['Alchemist', 'Armourer', 'Artillerist', 'Battle Smith'], 
    "Barbarian": ['Ancestral guardian', 'Battlerager', 'Beast', 'Berserker', 'Giant', 'Storm Herald', 
    'Totem Warrior', 'Wild Magic', 'Zealot'], 
    "Bard": ['Creation', 'Eloquence', 'Glamour', 'Lore', 'Spirits', 'Swords', 'Valour', 'Whispers'], 
    "Cleric": ['Arcana', 'Death', 'Forge', 'Grave', 'Knowledge', 'Life', 'Light', 'Nature', 'Order', 'Peace', 
    'Tempest', 'Trickery', 'Twilight', 'War'],
    "Druid": ['Dreams', 'Land', 'Moon', 'Shepherd', 'Spores', 'Stars', 'Wildfire'], 
    "Fighter": ['Arcane Archer', 'Bannerete', 'Battle Master', 'Cavalier', 'Champion', 'Echo Knight', 
    'Eldritch Knight', 'Psi Warrior', 'Rune Knight', 'Samurai'], 
    "Monk": ['Mercy', 'Ascendant Dragon', 'Astral Self', 'Drunken Master', 'Four Elements', 'Kensei', 'Long Death', 
    'Open Hand', 'Shadow', 'Sun Soul'],
    "Paladin": ['Ancients', 'Conquest', 'Crown', 'Devotion', 'Glory', 'Redemption', 'Vengeance', 'Watchers', 
    'Oathbreaker'], 
    "Ranger": ['Beast Master', 'Drakewarden', 'Fey Wanderer', 'Gloom Stalker', 'Horizon Walker', 'Hunter', 
    'Monster Slayer', 'Swarmkeeper'], 
    "Rogue": ['Arcane Trickster', 'Assassin', 'Inquisitive', 'Mastermind', 'Phantom', 'Scout', 'Soulknife', 
    'Swashbuckler', 'Thief'], 
    "Sorcerer": ['Aberrant Mind', 'Clockwork Soul', 'Draconic Bloodline', 'Divine Soul', 'Lunar Sorcery', 
    'Shadow Magic', 'Storm Sorcery', 'Wild Magic'], 
    "Warlock": ['Archfey', 'Celestial', 'Fathomless', 'Fiend', 'The Genie', 'Great Old One', 'Hexblade', 'Undead', 
    'Undying'], 
    "Wizard": ['Abjuration', 'Bladesinging', 'Chronurgy', 'Conjuration', 'Divination', 'Enchantment', 
    'Evocation', 'Graviturgy', 'Illusion', 'Necromancy', 'Order of Scribes', 'Transmutation', 'War Magic']}
    
    Classes_better = {
        "Artificer": ['Alchemist', 'Armourer', 'Artillerist', 'Battle Smith'], 
    "Barbarian": ['Ancestral Guardian', 'Berserker', 'Giant', 'Totem Warrior', 'Zealot'], 
    "Bard": ['Eloquence', 'Lore', 'Valour'], 
    "Cleric": ['Forge', 'Grave', 'Life', 'Light', 'Peace', 'Tempest', 'Trickery', 'Twilight'],
    "Druid": ['Dreams', 'Moon', 'Shepherd', 'Stars', 'Wildfire'], 
    "Fighter": ['Battle Master', 'Cavalier', 'Echo Knight', 'Eldritch Knight', 'Rune Knight'], 
    "Monk": ['Mercy', 'Kensei', 'Open Hand', 'Shadow'],
    "Paladin": ['Ancients', 'Conquest', 'Devotion', 'Redemption', 'Vengeance', 'Watchers', 'Oathbreaker'], 
    "Ranger": ['Beast Master', 'Drakewarden', 'Fey Wanderer', 'Gloom Stalker', 'Horizon Walker', 'Swarmkeeper'], 
    "Rogue": ['Arcane Trickster', 'Assassin', 'Scout', 'Soulknife', 'Swashbuckler'], 
    "Sorcerer": ['Aberrant Mind', 'Clockwork Soul', 'Divine Soul', 'Lunar Sorcery', 'Shadow Magic', 'Wild Magic'], 
    "Warlock": ['Archfey', 'Fathomless', 'Fiend', 'The Genie', 'Hexblade', 'Undead'], 
    "Wizard": ['Abjuration', 'Bladesinging', 'Chronurgy', 'Divination', 'Enchantment', 'Illusion', 'Necromancy', 
    'Order of Scribes']
    }
    
    
    S1 = ['Armourer','Totem Warrior','Eloquence','Lore','Peace','Twilight','Moon','Battle Master','Echo Knight',
          'Rune Knight','Vengeance','Gloom Stalker','Arcane Trickster','Soulknife','Swashbuckler','Divine Soul',
          'Aberrant Mind','Clockwork Soul','The Genie','Hexblade','Fiend','Enchantment','Chronurgy',
          'Lunar Sorcery']
    SA1 = ['Forge','Grave','Life','Light','Tempest','Shephard','Eldritch Knight','Kensei','Shadow','Conquest',
           'Divination']
    A1 = ['Artillerist','Battle Smith','Ancestral Guardian','Zealot','Stars','Mercy','Open Hand','Oathbreaker',
          'Redemption','Watchers','Beast Master','Swarmkeeper','Drakewarden','Scout','Wild Magic','Shadow Magic',
          'Archfey','Fathomless','Undead','Illusion','Necromancy','Bladesinging','Order of Scribes']
    AB1 = ['Berserker','Giant','Valour','Swords','Trickery','Dreams','Wildfire','Cavalier','Ancients','Devotion',
           'Horizon Walker','Fey Wanderer','Assassin','Abjuration']
    B1 = ['Alchemist','Beast','Storm Herald','Creation','Glamour','Order','Land','Champion','Psi Warrior',
          'Astral Self','Long Death','Glory','Mastermind','Phantom','Thief','Draconic Bloodline','Celestial',
          'Great Old One','Conjuration','Evocation']
    BC1 = ['Battlerager','Nature','Arcane Archer','Samurai','War Magic']
    C1 = ['Wild Magic','Spirits','Arcana','Death','Knowledge','War','Spores','Drunken Master','Crown','Hunter',
          'Monster Slayer','Inquisitive','Storm Sorcery','Transmutation','Graviturgy']
    CD1 = ['Whispers']
    D1 = ['Bannerete','Ascendant Dragon','Four Elements','Sun Soul','Undying']
    
    S = ['Barbarian/Fighter','Fighter/Barbarian','Fighter/Cleric','Monk/Cleric','Monk/Ranger','Monk/Rogue',
    'Paladin/Bard','Paladin/Sorcerer','Ranger/Fighter','Ranger/Rogue','Rogue/Druid','Rogue/Fighter','Rogue/Ranger',
    'Sorcerer/Warlock','Sorcerer/Paladin','Warlock/Paladin','Warlock/Sorcerer']
    A = ['Artificer/Fighter','Artificer/Rogue','Artificer/Wizard','Barbarian/Paladin','Barbarian/Rogue','Bard/Cleric',
    'Bard/Paladin','Bard/Sorcerer','Cleric/Fighter','Druid/Barbarian','Druid/Cleric','Druid/Paladin','Druid/Ranger',
    'Fighter/Paladin','Fighter/Ranger','Fighter/Rogue','Fighter/Wizard','Monk/Druid','Monk/Fighter','Paladin/Barbarian',
    'Paladin/Fighter','Paladin/Warlock','Ranger/Monk','Rogue/Artificer','Rogue/Bard','Rogue/Cleric','Rogue/Monk',
    'Rogue/Wizard','Warlock/Fighter','Wizard/Artificer','Wizard/Cleric','Wizard/Fighter']
    B = ['Artificer/Cleric','Artificer/Paladin','Barbarian/Cleric','Barbarian/Druid','Barbarian/Monk','Barbarian/Ranger',
    'Bard/Fighter','Bard/Rogue','Cleric/Monk','Cleric/Rogue','Cleric/Druid','Cleric/Paladin','Druid/Fighter','Druid/Monk',
    'Fighter/Artificer','Fighter/Bard','Monk/Barbarian','Paladin/Cleric','Paladin/Rogue','Ranger/Barbarian','Ranger/Cleric',
    'Ranger/Druid','Rogue/Barbarian','Rogue/Paladin','Rogue/Sorcerer','Sorcerer/Bard','Sorcerer/Cleric','Sorcerer/Fighter',
    'Sorcerer/Rogue','Warlock/Barbarian','Warlock/Bard','Warlock/Cleric','Warlock/Ranger','Warlock/Rogue','Wizard/Rogue',
    'Wizard/Sorcerer']
    C = ['Artificer/Bard','Artificer/Ranger','Artificer/Sorcerer','Barbarian/Bard','Bard/Artificer','Bard/Ranger',
    'Cleric/Artificer','Cleric/Ranger','Cleric/Warlock','Cleric/Wizard','Druid/Rogue','Druid/Sorcerer','Fighter/Druid','Fighter/Monk',
    'Fighter/Sorcerer','Monk/Sorcerer','Monk/Warlock','Monk/Wizard','Paladin/Artificer','Paladin/Druid','Ranger/Artificer',
    'Ranger/Sorcerer','Rogue/Warlock','Sorcerer/Artificer','Sorcerer/Wizard','Warlock/Artificer','Warlock/Monk',
    'Warlock/Wizard','Wizard/Bard','Wizard/Paladin']
    D = ['Artificer/Barbarian','Artificer/Druid','Artificer/Monk','Artificer/Warlock','Barbarian/Artificer',
    'Barbarian/Sorcerer','Barbarian/Warlock','Barbarian/Wizard','Bard/Barbarian','Bard/Druid','Bard/Monk','Bard/Wizard',
    'Cleric/Barbarian','Cleric/Bard','Cleric/Sorcerer','Druid/Artificer','Druid/Bard','Druid/Warlock','Druid/Wizard',
    'Fighter/Warlock','Monk/Artificer','Monk/Bard','Monk/Paladin','Paladin/Monk','Paladin/Ranger','Paladin/Wizard',
    'Ranger/Bard','Ranger/Paladin','Ranger/Warlock','Ranger/Wizard','Sorcerer/Barbarian','Sorcerer/Druid','Sorcerer/Monk',
    'Sorcerer/Ranger','Warlock/Druid','Wizard/Barbarian','Wizard/Druid','Wizard/Monk','Wizard/Ranger','Wizard/Warlock']
    
    'Nature'
    AS_dict = {
        'Str Con - Dex - Wis - Int Cha' : ['Barbarian'],
        'Str Cha - Con - Dex - Int Wis' : ['Paladin'],
        'Str/Dex - Con - Str/Dex Wis Cha - Int' : ['Battle Master','Champion','Echo Knight','Samurai'],
        'Str Con - Wis - Dex - Int Cha' : ['Cavalier', 'Rune Knight'],
        'Str/Dex - Con Int - Str/Dex Wis - Cha' : ['Eldritch Knight','Psi Warrior'],
        'Str/Dex Con - Cha - Str/Dex Wis - Int' : ['Purple Dragon Knight'],
        
        'Dex Int - Con - Wis - Str Cha' : ['Arcane Archer', 'Bladesinging'],
        'Dex - Con Int - Wis Cha - Str' : ['Inquisitive','Mastermind','Phantom','Soulknife'],
        'Dex - Int - Con - Wis Cha - Str' : ['Arcane Trickster'],
        'Dex - Con Cha - Int Wis - Str' : ['Assassin','Thief'],
        'Dex - Con Cha - Str Wis - Int' : ['Swashbuckler'],
        'Dex - Wis - Con - Str Int Cha' : ['Monk','Ranger'],
        'Dex Wis - Con - Cha - Str Int' : ['Trickery'],
        'Dex Con Wis - Int - Str Cha' : ['Wildfire'],
        'Dex Wis - Con - Str Int Cha' : ['Spores'],
        'Dex  - Wis - Con Int - Str Cha' : ['Scout'],
        
        'Con Wisdom - Dex - Cha - Str Int' : ['Peace'],

        'Int - Dex Con - Wis - Str Cha' : ['Artillerist','Battle Smith','Chronurgy','Order of Scribes',
                                           'Abjuration','Divination','Enchantment','Evocation','Illusion',
                                           'Transmutation','War Magic'],
        'Int - Con - Dex - Str Wis Cha' : ['Graviturgy','Necromancy'],
        'Int - Dex/Con - Dex/Con - Str Wis Cha' : ['Armourer'],
        'Int - Dex Con - Str Wis Cha' : ['Alchemist'],

        'Wis - Con - Str/Dex Cha - Str/Dex Int' : ['Arcana','Light','Nature','Order','War'],
        'Wis - Con - Dex - Str Int Cha' : ['Grave'],
        'Wis - Con Int - Dex - Str Cha' : ['Knowledge'],
        'Wis - Str Con - Dex Cha - Int' : ['Life','Forge','Tempest','Twilight'],
        'Wis - Dex Con Cha - Str Int' : ['Trickery'],
        'Wis - Dex Con - Str Int Cha' : ['Dreams'],
        'Wis - Dex Con - Int - Str Cha' : ['Stars','Land'],
        'Wis - Con - Str Dex Int - Cha' : ['Moon'],
        'Wis - Dex - Con Int - Str Cha' : ['Shepherd'],

        'Cha - Dex Con - Wis - Str Int' : ['Bard'],
        'Cha - Con - Dex - Str Int Wis' : ['Sorcerer','Warlock'],
        }
    
    m_tier_print =  [(S,'S'),(A,'A'),(B,'B'),(C,'C'),(D,'D')]
    tier_print = [
        (S1,'S'),(SA1,'S/A'),(A1,'A'),(AB1,'A/B'),(B1,'B'),(BC1,'B/C'),(C1,'C'),(CD1,'C/D'),(D1,'D')
        ]
    
    
    # Sex
    sex = ['Male', 'Female', 'Other']
    Other_sex = ['They/Them', 'It/Thing']
    
    
    # Alignment
    Align_First = ['Lawful', 'Neutral', 'Chaotic']
    Align_Second = ['Good', 'Neutral', 'Evil']
    
    
    # Personality
    P1 = ['Kind', 'Rude', 'Humble', 'Arrogant', 'Gentle', 'Cruel', 'Polite',
    'Blunt', 'Outgoing', 'Reserved', 'Cheerful','Brooding', 'Sensitive', 'Callous',
    'Easygoing', 'Aggressive', 'Energetic', 'Quiet', 'Patient', 'Rash']
    P2 = ['Loyal', 'Two-Faced', 'Brave', 'Cowardly', 'Honest', 'Liar', 'Generous',
    'Selfish', 'Diligent', 'Careless', 'Responsible','Unreliable', 'Shy', 'Impulsive',
    'Attentive', 'Reckless', 'Frugal', 'Extravagant', 'Mischievious', 'Obedient']
    P3 = ['Open-Minded', 'Prejudiced', 'Creative', 'Cunning', 'Decisive', 'Indecisive',
    'Wise', 'Naive', 'Sincere', 'Sarcastic','Orderly', 'Messy', 'Hardworking',
    'Lazy', 'Mature', 'Immature', 'Modest', 'Vain', 'Persistent', 'Meek']
    P4 = ['Intelligent', 'Ignorant', 'Assertive', 'Hesitant', 'Spoiled', 'Cautious',
    'Reasonable', 'Stubborn', 'Emotional', 'Apathetic','Funny', 'Serious', 'Charming',
    'Moody', 'Independent', 'Dependent', 'Determined', 'Petty', 'Pious', 'Paranoid']
    PT = ['ISFP-A', 'ISFP-T', 'ISFJ-A', 'ISFJ-T', 'ISTP-A', 'ISTP-T', 'ISTJ-A', 'ISTJ-T', 
    'INFP-A', 'INFP-T', 'INFJ-A', 'INFJ-T', 'INTP-A', 'INTP-T', 'INTJ-A', 'INTJ-T', 
    'ESFP-A', 'ESFP-T', 'ESFJ-A', 'ESFJ-T', 'ESTP-A', 'ESTP-T', 'ESTJ-A', 'ESTJ-T', 
    'ENFP-A', 'ENFP-T', 'ENFJ-A', 'ENFJ-T', 'ENTP-A', 'ENTP-T', 'ENTJ-A', 'ENTJ-T']
    
    
    # Additional Details
    A_D = ['Smoking', 'Loud voice', 'Playing with hair', 'Excessive drinking', 'Has an accent', 
    'Vision problems', 'Lip biting', 'Gambling addiction', 'Tendency to cheat', 'Has a stutter', 'Knuckle cracking',
    'Tendency to lie', 'Nail biting', 'Excessive swearing', 'A sweet tooth', 'Difficulty with hearing', 
    'Likes to eat', 'Sings/whistles', 'Uses third person', 'Soft voice']
    
    
    # EYES
    First_roll = ['Dark Brown', 'Chestnut Brown', 'Light Brown', 'Hazel', 'Blue-Gray', 'Blue-green', 'Green', 
    'Amber', 'Black', 'Unusual']
    Second_roll = ['Bright orange', 'Purple', 'White', 'Lavender', 'Fuschia', 'Golden Yellow', 'Black sclera', 
    'Red', 'Pale Pink', 'Vivid Green', 'Cyan']
    
    
    # Sexuality
    Other_sexuality = ['Pansexual', 'Asexual', 'Aromantic']
    def Race():
        selected_Lineage = random.choice(list(Lineages.keys()))
        # Select a random race from the chosen lineage
        selected_race = random.choice(Lineages[selected_Lineage])
        
        tot_subrace = ""
        tot_subrace_spec = ""
        
        if selected_race in sublist:
            if selected_race == 'Dragonborn':
                tot_subrace = random.choice(list(Dragonborn.keys()))
                tot_subrace_spec = random.choice(Dragonborn[tot_subrace])
            elif selected_race == 'Dwarf':
                tot_subrace = random.choice(list(Dwarf))
            elif selected_race == 'Elf':
                tot_subrace = random.choice(list(Elf))        
            elif selected_race == 'Gnome':
                tot_subrace = random.choice(list(Gnome))
            elif selected_race == 'Halfling':
                tot_subrace = random.choice(list(Halfling))
            elif selected_race == 'Tiefling':
                tot_subrace = random.choice(list(Tiefling.keys()))
                if tot_subrace == "Norm sub":
                    tot_subrace_spec = random.choice(Tiefling[tot_subrace])
            elif selected_race == 'Aasimar':
                tot_subrace = random.choice(list(Aasimar))            
            elif selected_race == 'Shifter':
                tot_subrace = random.choice(list(Shifter))
            elif selected_race == 'Genasi':
                tot_subrace = random.choice(list(Genasi))
                
            if selected_race == 'Dragonborn' or selected_race == 'Teifling':
                prace = f"Race: {tot_subrace_spec}-{tot_subrace}-{selected_race}"
            else:
                prace = f"Race: {tot_subrace}-{selected_race}"
        else:
            prace = f"Race: {selected_race}"
        
        # HEIGHT 
        H_res = ""
        for i,j in Height_tuples:
            if selected_race in i:
                H_res = f"Height: {random.choice(j)}"
            
        # BODY TYPE
        BT_res = ""
        if selected_race == 'Warforged':
            BT_res = (f"Body Type: {bodywarforged}")
        else:
            BT_res = (f"Body Type: {body}")
        
        # SKIN 
        S_res = ""
        if selected_race in unnaturalC_races:
            S_res = (f"Skin Tone: {random.choice(skin_unnatural)} ({random.choice(skin_vibrance)}, {random.choice(skin_tone)})")
        elif selected_race in normalC_races:
            S_res = (f"Skin Tone: {random.choice(skin_normal)} ({random.choice(skin_vibrance)})")
        elif selected_race in GoboC_races:
            S_res = (f"Skin Tone: {random.choice(skin_Gobo)} ({random.choice(skin_vibrance)}, {random.choice(skin_tone)})")
        elif selected_race in FurC_races:
            S_res = (f"Skin Tone: {random.choice(skin_Fur)} ({random.choice(skin_vibrance)}, {random.choice(skin_tone)})")
        elif selected_race in TonalC_races:
            S_res = (f"Skin Tone:  {random.choice(skin_vibrance)}, {random.choice(skin_tone)}")
        else:
            S_res = ('!!problem with skin code!!')
            
        R_H_BT_S = f"{prace}\n{H_res}\n{BT_res}\n{S_res}"
        return  R_H_BT_S
     
    def AGE():
        age_choice = random.choice(Age)
        A_res = f"Age: {age_choice}"
        return A_res
        
    def Background():
        
        selected_background = random.choice(Backgrounds)
        B_res = f"Background: {selected_background}"
        return B_res

    # IMPORTANT!!!   add background choices below

    def LVL():
        level = random.randint(3, 20)
        lvl_msg = f"Level {level}"
        if multiclass == 1:
            level_split = random.randint(1, level-1)
            level_split2 = level - level_split
            maxlvl = max(level_split,level_split2)
            minlvl = min(level_split,level_split2)
            lvl_msg += f"\nMulticlass Levels: {maxlvl},{minlvl}"
        return lvl_msg
    
    def CLASS():
        # ------------------------------------------------
        if class_list == "all":
            chosen_option_set = Classes_all
        else:
            chosen_option_set = Classes_better
        # ------------------------------------------------
        # then it picks from chosen class options
        SC = random.choice(list(chosen_option_set.keys()))
        SC2 = random.choice(list(chosen_option_set.keys()))
        
        while SC2 == SC:
            SC2 = random.choice(list(chosen_option_set.keys()))
            
        multiclass_combo = f"{SC}/{SC2}"
        multiclass_combo_rev = f"{SC2}/{SC}"
        
        SSC = random.choice(chosen_option_set[SC])
        SSC2 = random.choice(chosen_option_set[SC2])
        

        ASscore1 = ''
        if multiclass == 1:
            SC_list = [SC,SC2,SSC,SSC2]
        elif multiclass == 0:
            SC_list = [SC,SSC]
            
        for el in SC_list:
            for key in AS_dict.keys():
                x  = AS_dict.get(key)
                if el in x:
                    ASscore1 += f"\n                {key}"
        
        if multiclass == 1:
            # MULTICLASSES
            Multi_score = 'n/A'
            result = f"Class:      {SC}({SSC})/{SC2}({SSC2})"
            
            for i,j in m_tier_print:
                if multiclass_combo in i:
                    Multi_score = j
                    
            result += f"   {Multi_score}-Tier"
            result += f"\n            {SC2}({SSC2})/{SC}({SSC})"
            
            Multi_score2 = 'n/A'
            for i,j in m_tier_print:
                if multiclass_combo_rev in i:
                    Multi_score2 = j
                    
            result += f"   {Multi_score2}-Tier"
            result += f"\nAbility Scores (Most to Least): {ASscore1}"
            
        else:   # for no multiclass, translate variable name of tier to print str
            for i,j in tier_print:
                if SSC in i:
                    subScore = j
            result = f"Class: {SC}({SSC}) {subScore}-Tier\nAbility Scores (Most to Least): {ASscore1}"
            
        return result


    def Sex():
        sex_choice = random.choice(sex)
        other_choice = random.choice(Other_sex)
        sex_res = "n/A"
        if sex_choice == 'Other':
            sex_res = f"Sex: {other_choice}"
        else:
            sex_res = f"Sex: {sex_choice}"
        return sex_res

    def Alignment():
        A_C_1 = random.choice(Align_First)
        A_C_2 = random.choice(Align_Second)
        A_res = "n/A"
        if A_C_1 == 'Neutral' and A_C_2 == 'Neutral':
            A_res = "Alignment: True Neutral"
        else:
            A_res = f"Alignment: {A_C_1} {A_C_2}" 
        return A_res

    def Personality():
        selected_P1 = random.choice(P1) 
        selected_P2 = random.choice(P2) 
        selected_P3 = random.choice(P3) 
        selected_P4 = random.choice(P4) 
        selected_PT = random.choice(PT)
        P_res = f"Personality:  {selected_P1}, {selected_P2}, {selected_P3}, {selected_P4}\nPersonality Type:  {selected_PT}"
        return P_res
    
    def Additional_details():
        selected_A_D = random.choice(A_D) 
        AD_res = f"Additional Detail:  {selected_A_D}"
        return AD_res

    def EYES():
        s_1 = random.choice(First_roll) 
        s_2 = random.choice(Second_roll)
        E_res = ""
        if s_1 == 'Unusual':
            E_res = f"Eye Colour: Unusual ({s_2})"
        else:
            E_res = f"Eye Colour: {s_1}"
        return E_res

    def SEXUALITY():
        #Straight(35.5),Gay(7.5),Bisexual(5.4),Other(1.6)
        #35,8,5,2 = 70,16,10,4 => 70,86,96,10
        number = random.randint(1, 100)
        other_choice = random.choice(Other_sexuality)
        if number <= 70:
            S_res = 'Sexuality: Heterosexual'
        elif number <= 86 and number > 70:
            S_res = 'Sexuality: Homoseexual'
        elif number <= 96 and number > 86:
            S_res = 'Sexuality: Bisexual'
        elif number <= 100 and number > 96:
            S_res = f"Sexuality: {other_choice}"
        else:
            S_res = 'problem with Sexuality'
        return S_res

    

    Final_msg = f"\nYour randomly generated {option}:"
    
    if option == "Level":
        Final_msg += f"\n{LVL()}"
    elif option == "Background":
        Final_msg += f"\n{Background()}" 
    elif option == "Alignment":
        Final_msg += f"\n{Alignment()}"
    elif option == "Class":
        Final_msg += f"\n{CLASS()}"
    elif option == "Additional_details":
        Final_msg += f"\n{Additional_details()}"
    elif option == "Personality":
        Final_msg += f"\n{Personality()}"
    elif option == "Sexuality":
        Final_msg += f"\n{SEXUALITY()}"
    elif option == "Sex":
        Final_msg += f"\n{Sex()}"
    elif option == "Race":
        Final_msg += f"\n{Race()}"
    elif option == "Age":
        Final_msg += f"\n{AGE()}"
    elif option == "Eyes":
        Final_msg += f"\n{EYES()}"
    elif option == "Character":
        Final_msg += "\n===================================================================="
        Final_msg += f"\n{LVL()}"
        Final_msg += f"\n{Background()}"  
        Final_msg += f"\n{Alignment()}"
        Final_msg += f"\n{CLASS()}"
        Final_msg += "\n--------------------------------------------------------------------"
        Final_msg += f"\n{Additional_details()}"
        Final_msg += f"\n{Personality()}"
        Final_msg += f"\n{SEXUALITY()}"
        Final_msg += f"\n{Sex()}"
        Final_msg += "\n--------------------------------------------------------------------"
        Final_msg += f"\n{Race()}"
        Final_msg += f"\n{AGE()}"
        Final_msg += f"\n{EYES()}"
        Final_msg += "\n===================================================================="
        
    return Final_msg
    
def AS():
    above15 = int(input("How many above 14?: "))
    while above15 > 6:
        print("Only six rolls dude")
        above15 = int(input("How many above 14?: "))       
    sub10 = int(input("How many below 10?: "))
    while sub10 > 6 - above15:
        print(f"Only {6 - above15} rolls left dude")
        sub10 = int(input("How many below 10?: "))
    mintot = int(input("Minimum Total: "))
    while mintot < 0 or mintot > ((6 - sub10)*18 + sub10*9):
        print("Impossible total given limits")
        mintot = int(input("Minimum Total: "))
    
    
    
    while True: #Rolls
        total_sum = 0
        Roll_list = []

        for R in range(6):
        # 4d6 - lowest
            rolls = [random.randint(1, 6) for _ in range(4)]
            rollR = sum(rolls) - min(rolls)
        # sum  &  list of rolls
            total_sum += rollR
            Roll_list += [ rollR ]
    # sort list highest to lowest
        Roll_list.sort(reverse=True)
    #get two highest
        Roll_list_max = []
        for i in range(0, above15):
            Roll_list_max.append(Roll_list[i])
        
    
   
        sub10_count = 0
        for i in range(6):
            if Roll_list[i] < 10:
                sub10_count += 1 
        
        if min(Roll_list_max) >= 15 and sub10_count >= sub10:
            if total_sum > mintot:
            #print (Roll_list_max)
                #print (f"\nRolls & Total: :  {Roll_list} = {total_sum}") - old print location
                #print (f"Total: {total_sum}")
                break
    
    # ASI
    oddlist = [3,5,7,9,11,13,15,17]

    odd_element = []
    odd_count = 0
    for i in range(6): #  count odd numbers
        if Roll_list[i] in oddlist:
            odd_count += 1 
            odd_element.append(Roll_list[i])
    
    
    
    
    # choose n value for testing
    while odd_count != 2:
        while True:
            total_sum = 0
            Roll_list = []

            for R in range(6):
            # 4d6 - lowest
                rolls = [random.randint(1, 6) for _ in range(4)]
                rollR = sum(rolls) - min(rolls)
            # sum  &  list of rolls
                total_sum += rollR
                Roll_list += [ rollR ]
        # sort list highest to lowest
            Roll_list.sort(reverse=True)
        #get two highest
            Roll_list_max = []
            for i in range(0, above15):
                Roll_list_max.append(Roll_list[i])
            
        
       
            sub10_count = 0
            for i in range(6):
                if Roll_list[i] < 10:
                    sub10_count += 1 
            
            if min(Roll_list_max) >= 15 and sub10_count >= sub10:
                if total_sum > mintot:
                    #print (Roll_list_max)
                    # print (f"\nRolls & Total: :  {Roll_list} = {total_sum}")
                    break
        
        # ASI
        oddlist = [3,5,7,9,11,13,15,17]

        odd_element = []
        odd_count = 0
        for i in range(6):
            if Roll_list[i] in oddlist:
                odd_count += 1 
                odd_element.append(Roll_list[i])
                
    print (f"\nRolls & Total: :  {Roll_list} = {total_sum}")
    print (f"\nOdd Elements({odd_count}):  {odd_element}")
    
        
    
    # ASI's
   
    plus1elements = []
    n = 0
    for i in range(6): # helps function dunno how
        if n < 3:
            if Roll_list[i] in oddlist:
                n += 1 # no. odd 
                plus1elements.append(Roll_list[i])
    
        # n = 3 seems good
    Roll_list_original = Roll_list
    Roll_list_update = Roll_list
    
    #plus2elements = []     problem still with 18,16,16,9,9,8 to 19,16,16,9,9,8 balance. especially with number < 10
    if n == 2: # 2 odd numbers
    # vary or balance stats
        vary_balance = str(input("Vary or Balance ASI's?: ", ))
        flag = True
        while flag:
            if vary_balance.lower() != 'vary' or vary_balance.lower() != 'balance':
                flag = False
            else:
                print ("Invalid input")
                vary_balance = input("Vary or Balance AS's: ")
        
        #print (f"Rolls + ASI 0: {Roll_list}")   
        if vary_balance.lower() == 'balance':
            for i in range(0,6):
                if Roll_list[i] in odd_element:
                    Roll_list[i] += 1
            Roll_list[0] += 1
            print (f"Rolls & ASI:      {Roll_list}")
        
        if vary_balance.lower() == 'vary':
              
            #print(odd_element)
            Roll_list_2check = Roll_list_original
            for i in range(0,6):
                if Roll_list_update[i] == max(odd_element):
                    Roll_list_2check.remove(Roll_list_update[i])
                    add_back = Roll_list_update[i]+1
                    #print(add_back)
                    break
            #print (f"Rolls post +1: {Roll_list_update}") # works func 845-852
            
             
            for i in range(0,6):
                if Roll_list_2check[i] == max(Roll_list_2check):
                    Roll_list_2check[i] += 2
                    #print (f"Roll +2: {Roll_list_2check[i]}[{i}]") 
                    Roll_list_2check.append(add_back)
                    Roll_list_2check.sort(reverse = True)
                    break
            print (f"Rolls & ASI:      {Roll_list_2check}")   

    if n == 1: # works
        #print (f"odd elements: {odd_element}")
        
        for i in range(5): 
            if Roll_list_original[i] not in oddlist:
                Roll_list_update[i] += 2
                print (f"Rlu +2: {Roll_list_update[i]}")
                break 
        for i in range(5):
            if Roll_list_original[i] in oddlist:
                Roll_list_update[i] += 1
                print (f"Rlu +1: {Roll_list_update[i]}")
                break
          
        print (f"Rolls + ASI:      {Roll_list_update}") 
    if n == 0: # works
        vary_balance = str(input("Vary or Balance ASI's?: ", ))
        flag = True
        while flag:
            if vary_balance.lower() != 'vary' or vary_balance.lower() != 'balance':
                flag = False
            else:
                print ("Invalid input")
                vary_balance = input("Vary or Balance AS's: ")
        if vary_balance.lower() == 'vary':
            Roll_list[0] += 2
            Roll_list[1] += 1
        if vary_balance.lower() == 'balance':
            if Roll_list[0] == Roll_list[1]:
                Roll_list[1] += 1
                Roll_list[2] += 2
            else:
                Roll_list[0] += 1
                Roll_list[1] += 2
        
                
        print (f"Rolls & ASI:      {Roll_list}") 
        
    if n >= 3: # works (highest evn if odd, gets +2)
    # vary or balance stats
        vary_balance = str(input("Vary or Balance ASI's?: ", ))
        flag = True
        while flag:
            if vary_balance.lower() != 'vary' or vary_balance.lower() != 'balance':
                flag = False
            else:
                print ("Invalid input")
                vary_balance = input("Vary or Balance AS's: ")
                
        #print (f"Rolls + ASI 0: {Roll_list}")   
        if vary_balance.lower() == 'balance':
            b = 0
            for i in range(0,6):
                if Roll_list[i] in oddlist:
                    Roll_list[i] += 1
                    b += 1
                if b == 3:
                    break
            #print(f"b is {b}")
            print (f"Rolls & ASI:      {Roll_list}") 
        
        if vary_balance.lower() == 'vary':
              
            #print(f"odd: {odd_element}")
            #print(f"max odd: {max(odd_element)}")
            Roll_list_2check = Roll_list_original
            new_numb = 0
            
            for i in range(0,6):
                if Roll_list_update[i] == max(odd_element):
                    
                    new_numb += Roll_list_update[i] +1
                    
                    #print(i)
                    Roll_list_2check.remove(Roll_list_update[i])
                    break
                    
            
            #print (f"Rolls post +1: {Roll_list_update}") 
            
            Roll_list_2check.sort(reverse = True)
            Roll_list_2check[0] += 2
            #print (f"Roll +2: {Roll_list_2check[i]}[{i}]") 
            Roll_list_2check.append(new_numb)
            Roll_list_2check.sort(reverse = True)
            print (f"Rolls & ASI:      {Roll_list_2check}")   


print (CC("character",1))    

     

        
    
    
    
    
        
                
    
        
    
        

    