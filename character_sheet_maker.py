#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 13:21:38 2025

@author: nicholasbyrne
"""
import os
import json
import tkinter as tk

from tkinter import scrolledtext, messagebox, filedialog, ttk
import CC_maker_data
from CC_maker_data import subclass_dict, Lineages, all_ability_data, CLASS_BASED_DICT, CLASS_ABILITIES_LIST, Race_feats2, ADV, Immunities
import random




barb_level_dict = {
        1: [2,2,2],
        2: [2,2,2],
        3: [2,3,2],
        4: [2,3,2],
        5: [3,3,2],
        6: [3,4,2],
        7: [3,4,2],
        8: [3,4,2],
        9: [4,4,3],
        10: [4,4,3],
        11: [4,4,3],
        12: [4,5,3],
        13: [5,5,3],
        14: [5,5,3],
        15: [5,5,3],
        16: [5,5,4],
        17: [6,6,4],
        18: [6,6,4],
        19: [6,6,4],
        20: [6,6,4]
	}

class CS_app:
    
    
    
    def __init__(self, root):
        self.root = root
        self.save_file_path = os.path.join(os.getcwd(), "character_data.json")
        self.root.title("D&D General Application")
        self.root.geometry("1200x700")
        self.root.minsize(1430,835)
        self.setup_ui()
        self.use_3d6 = tk.BooleanVar()
        self.use_3d6.set(False)
        
        self.load_info_on_startup()

    def load_info_on_startup(self):
        """Load character data when the app starts"""
        if os.path.exists(self.save_file_path):
            self.load_info()
            self.refresh()  # Refresh after loading
        else:
            # If no save file, just refresh with defaults
            self.refresh()
        
    def setup_ui(self):
        # Configure window background
        self.root.config(bg="maroon")
        
        self.title_frame = tk.Frame(self.root,bg="black")
        self.title_frame.pack(side=tk.TOP,fill=tk.BOTH)
        
        #------------------ Name ---------------------------------------
        self.name_frame = tk.Frame(self.title_frame, bg="dim grey", padx=5, pady=0)
        self.name_frame.pack(side=tk.LEFT, expand=False)
        
        self.name_text = scrolledtext.ScrolledText(
            self.name_frame,
            wrap=tk.WORD,
            width=30,
            height=1,
            font=("Helvetica Neue", 25),
            bg="gray7",
            fg="white",
            padx=5,
            pady=0,
            relief=tk.SUNKEN,
            bd=3)
        self.name_text.pack(side=tk.TOP, padx=5,pady=5)
        self.name_text.insert(tk.END, "Baermon Stoneblade")
        
        self.c_name_frame = tk.Frame(self.name_frame, bg="dim grey", padx=0, pady=0)
        self.c_name_frame.pack(side=tk.TOP, expand=False, fill=tk.X, padx=5,pady=0)
        
        self.c_name_label = tk.Label(
            self.c_name_frame ,
            text="• Character Name •",
            font=("Times New Roman", 12),
            bg="dim grey",
            fg="black")
        self.c_name_label.pack(side=tk.LEFT, pady=0)
        
        
        #------------------ title details ---------------------------------------------------
        self.title_det_frame = tk.Frame(self.title_frame, bg="black", padx=5, pady=5)
        self.title_det_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        self.Class_frame = tk.Frame(self.title_det_frame, bg="blue", padx=5, pady=5)
        self.Class_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.C1_frame = tk.Frame(self.Class_frame, bg="dim grey", padx=5, pady=5)
        self.C1_frame.pack(side=tk.LEFT, expand=False, fill=tk.BOTH)
        self.C2_frame = tk.Frame(self.Class_frame, bg="dim grey", padx=5, pady=5)
        self.C2_frame.pack(side=tk.LEFT, expand=False, fill=tk.BOTH)

        self.class1_frame = tk.Frame(self.C1_frame, bg="dim grey", padx=0, pady=3)
        self.class1_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        self.subclass1_frame = tk.Frame(self.C1_frame, bg="dim grey", padx=0, pady=3)
        self.subclass1_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        self.class2_frame = tk.Frame(self.C2_frame, bg="dim grey", padx=0, pady=3)
        self.class2_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        self.subclass2_frame = tk.Frame(self.C2_frame, bg="dim grey", padx=0, pady=3)
        self.subclass2_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)

        self.Race_frame = tk.Frame(self.title_det_frame, bg="red", padx=5, pady=5)
        self.Race_frame.pack(side=tk.LEFT, expand=True , fill=tk.BOTH)
        self.race_frame = tk.Frame(self.Race_frame, bg="dim grey", padx=5, pady=2)
        self.race_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        self.subrace_frame = tk.Frame(self.Race_frame, bg="dim grey", padx=5, pady=2)
        self.subrace_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        self.background_frame = tk.Frame(self.Race_frame, bg="dim grey", padx=5, pady=2)
        self.background_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        

        self.BGR_frame = tk.Frame(self.title_det_frame, bg="green", padx=5, pady=5)
        self.BGR_frame.pack(side=tk.LEFT, expand=False, fill=tk.BOTH)
        self.type_frame = tk.Frame(self.BGR_frame, bg="dim grey", padx=5, pady=0)
        self.type_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        self.bgr_frame = tk.Frame(self.BGR_frame, bg="dim grey", padx=5, pady=0)
        self.bgr_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        self.align_frame = tk.Frame(self.BGR_frame, bg="dim grey", padx=5, pady=0)
        self.align_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        
        #-------------------------------------------------------  CLASS 1 ----------------------------------------------------------------
        tk.Label(self.class1_frame, text="1st CLASS: ").pack(side="left",padx=0,pady=0)
        self.class_combobox = ttk.Combobox(
        self.class1_frame,
            values=["-","Artificer","Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"],
            state="readonly",
            width=12,
            font=("Helvetica", 13),background="dim grey")
        self.class_combobox.set("Barbarian")  # Default: "-"
        self.class_combobox.pack(side="left",padx=0,pady=0)
        self.class_combobox.bind('<<ComboboxSelected>>', self.on_selected)
        self.class_combobox.bind('<<ComboboxSelected>>', self.set_saves)

        self.lvl_Entry = tk.Entry(self.class1_frame, width=3)
        self.lvl_Entry.insert(0, 5)
        self.lvl_Entry.pack(side="left",padx=0,pady=0)
        self.lvl_Entry.bind('<Return>', lambda e: self.refresh())
        
        tk.Label(self.subclass1_frame, text="1st SUBCLASS:").pack(side="left",padx=0,pady=0)
        self.subclass_combobox = ttk.Combobox(
        self.subclass1_frame,
        values=CC_maker_data.subclass_dict["Barbarian"],  # Start with Barbarian subclasses
        state="readonly",
        width=14,
        font=("Helvetica", 13))
        self.subclass_combobox.current(0)
        self.subclass_combobox.pack(side="left",padx=0,pady=0)
        self.subclass_combobox.bind('<<ComboboxSelected>>', self.on_selected)
        
        #-------------------------------------------------------  CLASS 2 ----------------------------------------------------------------
        tk.Label(self.class2_frame, text="2nd CLASS: ").pack(side="left",padx=0,pady=0)
        self.class_combobox2 = ttk.Combobox(
        self.class2_frame,
            values=["-","Artificer","Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"],
            state="readonly",
            width=12,
            font=("Helvetica", 13),background="dim grey")
        self.class_combobox2.set("-")  # Default: "-"
        self.class_combobox2.pack(side="left",padx=0,pady=0)
        self.class_combobox2.bind('<<ComboboxSelected>>', self.on_selected)

        self.lvl_Entry2 = tk.Entry(self.class2_frame, width=3)
        self.lvl_Entry2.insert(0, 5)
        self.lvl_Entry2.pack(side="left",padx=0,pady=0)
        self.lvl_Entry2.bind('<Return>', lambda e: self.refresh())
        
        tk.Label(self.subclass2_frame, text="2nd SUBCLASS:").pack(side="left",padx=0,pady=0)
        self.subclass_combobox2 = ttk.Combobox(
        self.subclass2_frame,
        values=CC_maker_data.subclass_dict["-"],  # Start with - subclasses
        state="readonly",
        width=14,
        font=("Helvetica", 13))
        self.subclass_combobox2.current(0)
        self.subclass_combobox2.pack(side="left",padx=0,pady=0)
        self.subclass_combobox2.bind('<<ComboboxSelected>>', self.on_selected)


        
        # --------------------- RACE ------------------------------------------------------------------------------------------------------------------------------------------------------------
        tk.Label(self.race_frame, text="RACE:").pack(side="left",padx=0,pady=0)
        self.race_combobox = ttk.Combobox(
        self.race_frame,
            values= ['Dragonborn','Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Tiefling',
            'Aarakocra', 'Aasimar', 'Changeling', 'Deep Gnome', 'Duergar', 'Eladrin', 'Fairy', 'Firbolg', 
            'Genasi', 'Githyanki', 'Githzerai', 'Goliath', 'Harengon', 'Kenku', 'Locathah', 'Owlin', 'Satyr', 'Sea Elf', 
            'Shadar-Kai', 'Tabaxi', 'Tortle', 'Triton', 'Verdan', 'Warforged',
            'Bugbear', 'Centaur', 'Goblin', 'Grung', 'Hobgoblin', 'Kobold', 'Lizardfolk', 'Minotaur', 
            'Orc', 'Shifter', 'Yuan-Ti'],
            state="readonly",
            width=17,
            font=("Helvetica", 12),background="dim grey")
        self.race_combobox.set('Dwarf')  # Default: "-"
        self.race_combobox.pack(side="left",padx=0,pady=0)
        
        self.race_combobox.bind('<<ComboboxSelected>>', self.on_selected)
        
        tk.Label(self.subrace_frame, text="SUBRACE:").pack(side="left",padx=0,pady=0)
        self.subrace_combobox = ttk.Combobox(
        self.subrace_frame,
        values=CC_maker_data.Lineages['Dwarf'],  # Start with Barbarian subclasses
        state="readonly",
        width=12,
        font=("Helvetica", 10))
        self.subrace_combobox.current(0)
        self.subrace_combobox.pack(side="left",padx=0,pady=0)
        
        self.subrace_combobox.bind('<<ComboboxSelected>>', self.on_selected)
        

        tk.Label(self.background_frame, text="BACKGROUND:").pack(side="left",padx=0,pady=0)
        self.background_combobox = ttk.Combobox(
        self.background_frame,
        values=[
"-",
"Acolyte",
"Anthropologist",
"Archaeologist",
"Athlete",
"Charlatan",
"City Watch",
"Clan Crafter",
"Cloistered Scholar",
"Courtier",
"Criminal",
"Entertainer",
"Faceless",
"Faction Agent",
"Far Traveler",
"Feylost",
"Fisher",
"Folk Hero",
"Giant Foundling",
"Gladiator",
"Guild Artisan",
"Guild Merchant",
"Haunted One",
"Hermit",
"House Agent",
"Inheritor",
"Investigator (SCAG)",
"Investigator (VRGR)",
"Knight",
"Knight of the Order",
"Marine",
"Mercenary Veteran",
"Noble",
"Outlander",
"Pirate",
"Rewarded",
"Ruined",
"Rune Carver",
"Sage",
"Sailor",
"Shipwright",
"Smuggler",
"Soldier",
"Spy",
"Urban Bounty Hunter",
"Urchin",
"Uthgardt Tribe Member",
"Waterdhavian Noble",
"Witchlight Hand"
],  
        state="readonly",
        width=12,
        font=("Helvetica", 10))
        self.background_combobox.current(0)
        self.background_combobox.pack(side="left",padx=0,pady=0)
        self.background_combobox.bind('<<ComboboxSelected>>', self.apply_bgr)
        

       
        self.type_Entry = tk.Entry(self.type_frame, width=8)
        self.type_Entry.insert(0, "Humanoid")
        self.type_Entry.pack(side="right",padx=0,pady=0)   
        tk.Label(self.type_frame, text="Type:").pack(side="right",padx=0,pady=0)

        
        
        self.align_Entry = tk.Entry(self.align_frame, width=10)
        self.align_Entry.insert(0, "Neutral Good")
        self.align_Entry.pack(side="right",padx=0,pady=0)
        tk.Label(self.align_frame, text="Alignment:").pack(side="right",padx=0,pady=0)  
#%% Buttons
        #------------------------------------------------------------------------------------
        self.top_buttons_frame = tk.Frame(self.root,bg="white")
        self.top_buttons_frame.pack(side=tk.TOP,fill=tk.BOTH,pady=0)
        
        self.junk_text = scrolledtext.ScrolledText(
            self.top_buttons_frame,
            wrap=tk.WORD,
            width=20,
            height=1,
            font=("Helvetica Neue", 10),
            bg="gray7",
            fg="white",
            padx=5,
            pady=0,
            relief=tk.SUNKEN,
            bd=3)
        self.junk_text.pack(side=tk.LEFT, padx=5,pady=0)
        
        
        self.Public_Button = tk.Button(self.top_buttons_frame, text="Public", command = self.public, font=("Times New Roman", 8, "bold"),
        bg="dim grey",fg="white",padx=5,pady=5,relief=tk.RAISED,bd=3)
        self.Public_Button.pack(side=tk.LEFT)
        
        self.GM_Button = tk.Button(self.top_buttons_frame, text="GM", command = self.gm, font=("Times New Roman", 8, "bold"),
        bg="dim grey",fg="white",padx=5,pady=5,relief=tk.RAISED,bd=3)
        self.GM_Button.pack(side=tk.LEFT)
        
        self.save_button = tk.Button(self.top_buttons_frame, text="💾 Save Info", command=self.save_info, font=("Times New Roman", 8, "bold"),
        bg="dim grey",fg="white",padx=5,pady=5,relief=tk.RAISED,bd=3)
        self.save_button.pack(side=tk.LEFT)

        self.load_button = tk.Button(self.top_buttons_frame, text="📂 Load Info", command=self.load_info, font=("Times New Roman", 8, "bold"),
        bg="dim grey",fg="white",padx=5,pady=5,relief=tk.RAISED,bd=3)
        self.load_button.pack(side=tk.LEFT)
        
        self.Cog_Button = tk.Button(self.top_buttons_frame, text="•", command = self.cog, font=("Times New Roman", 8, "bold"),
        bg="dim grey",fg="white",padx=5,pady=5,relief=tk.RAISED,bd=3)
        self.Cog_Button.pack(side=tk.RIGHT)
        
        self.Spells_Button = tk.Button(self.top_buttons_frame, text="Spells", command = self.spells, font=("Times New Roman", 8, "bold"),
        bg="dim grey",fg="white",padx=5,pady=5,relief=tk.RAISED,bd=3)
        self.Spells_Button.pack(side=tk.RIGHT)
        
        self.Bio_Button = tk.Button(self.top_buttons_frame, text="Bio", command = self.bio, font=("Times New Roman", 8, "bold"),
        bg="dim grey",fg="white",padx=5,pady=5,relief=tk.RAISED,bd=3)
        self.Bio_Button.pack(side=tk.RIGHT)
        
        self.Core_Button = tk.Button(self.top_buttons_frame, text="Core", command = self.core, font=("Times New Roman", 8, "bold"),
        bg="dim grey",fg="white",padx=5,pady=5,relief=tk.RAISED,bd=3)
        self.Core_Button.pack(side=tk.RIGHT)
        
        self.Refresh_Button = tk.Button(self.top_buttons_frame, text="Refresh", command = self.refresh, font=("Times New Roman", 8, "bold"),
        bg="dim grey",fg="white",padx=5,pady=5,relief=tk.RAISED,bd=3)
        self.Refresh_Button.pack(side=tk.TOP)
        
        

#%% Frames     
        
        
        #-------------------------------------------------------------------------------------------
        self.lower_frame = tk.Frame(self.root,bg="gray9")
        self.lower_frame.pack(side=tk.TOP,fill=tk.Y,padx=5,pady=5)
        
        
        
        self.AS_frame = tk.Frame(self.lower_frame,bg="gray15")
        self.AS_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=5,pady=5)
        
        self.SAVE_frame = tk.Frame(self.lower_frame,bg="gray15")
        self.SAVE_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=5,pady=5)
        #-----------------------------------------------------------------------------------------
        self.MID_frame = tk.Frame(self.lower_frame,bg="orange")
        self.MID_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=5,pady=5)
        
        self.MID_TOP1_frame = tk.Frame(self.MID_frame,bg="yellow")
        self.MID_TOP1_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=3)

        self.MID_TOP_frame = tk.Frame(self.MID_frame,bg="yellow")
        self.MID_TOP_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=3)
        
        self.MID_MID_frame = tk.Frame(self.MID_frame,bg="blue")
        self.MID_MID_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=3)

        self.MID_PROF_frame = tk.Frame(self.MID_frame,bg="blue")
        self.MID_PROF_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=3)
        #-----------------------------------------------------------------------------------------
        self.MID_RIGHT_frame = tk.Frame(self.lower_frame,bg="brown")
        self.MID_RIGHT_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=5,pady=5)
        
        self.ability_selector_frame = self.create_ability_selector(self.MID_RIGHT_frame)
        
#%% ABILITY SCORES
        self.STR_frame = tk.Frame(self.AS_frame,bg="gray15")

        self.STR_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=5)
        self.DEX_frame = tk.Frame(self.AS_frame,bg="gray15")
        self.DEX_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=5)
        self.CON_frame = tk.Frame(self.AS_frame,bg="gray15")
        self.CON_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=5)
        self.INT_frame = tk.Frame(self.AS_frame,bg="gray15")
        self.INT_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=5)
        self.WIS_frame = tk.Frame(self.AS_frame,bg="gray15")
        self.WIS_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=5)
        self.CHA_frame = tk.Frame(self.AS_frame,bg="gray15")
        self.CHA_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=5)

        self.cha_Entry = tk.Entry(self.CHA_frame, width=2, font=("Times New Roman", 12, "bold"))
        self.cha_Entry.insert(0, 10)
        self.cha_Entry.pack(side="top",padx=0,pady=0)
        self.cha_mod_output = tk.Text(
            self.CHA_frame,
            wrap=tk.WORD,
            width=2,
            height=1,
            font=("Helvetica Neue", 25),
            bg="orange",
            fg="white",
            padx=5,
            pady=0,
            relief=tk.SUNKEN,
            bd=3)
        self.cha_mod_output.pack(side=tk.TOP, padx=5,pady=0)
        self.cha_mod_output.insert(tk.END, CS_app.calc_mod(self,self.cha_Entry.get()))
        self.cha_mod_output.config(state='disabled')
        self.cha_label = tk.Label(self.CHA_frame , text="CHARISMA",
            font=("Helvetica Neue", 10, "bold"),
            bg="dim grey",
            fg="black")
        self.cha_label.pack(side=tk.TOP, pady=0)

        self.wis_Entry = tk.Entry(self.WIS_frame, width=2, font=("Times New Roman", 12, "bold"))
        self.wis_Entry.insert(0, 10)
        self.wis_Entry.pack(side="top",padx=0,pady=0)
        self.wis_mod_output = tk.Text(
            self.WIS_frame,
            wrap=tk.WORD,
            width=2,
            height=1,
            font=("Helvetica Neue", 25),
            bg="orange",
            fg="white",
            padx=5,
            pady=0,
            relief=tk.SUNKEN,
            bd=3)
        self.wis_mod_output.pack(side=tk.TOP, padx=5,pady=0)
        self.wis_mod_output.insert(tk.END, CS_app.calc_mod(self,self.wis_Entry.get()))
        self.wis_mod_output.config(state='disabled')
        self.wis_label = tk.Label(self.WIS_frame , text="WISDOM",
            font=("Helvetica Neue", 10, "bold"),
            bg="dim grey",
            fg="black")
        self.wis_label.pack(side=tk.TOP, pady=0)
        
        self.int_Entry = tk.Entry(self.INT_frame, width=2, font=("Times New Roman", 12, "bold"))
        self.int_Entry.insert(0, 10)
        self.int_Entry.pack(side="top",padx=0,pady=0)
        self.int_mod_output = tk.Text(
            self.INT_frame,
            wrap=tk.WORD,
            width=2,
            height=1,
            font=("Helvetica Neue", 25),
            bg="orange",
            fg="white",
            padx=5,
            pady=0,
            relief=tk.SUNKEN,
            bd=3)
        self.int_mod_output.pack(side=tk.TOP, padx=5,pady=0)
        self.int_mod_output.insert(tk.END, CS_app.calc_mod(self,self.int_Entry.get()))
        self.int_mod_output.config(state='disabled')
        self.int_label = tk.Label(self.INT_frame , text="INTELLIGENCE",
            font=("Helvetica Neue", 10, "bold"),
            bg="dim grey",
            fg="black")
        self.int_label.pack(side=tk.TOP, pady=0)
        
        self.con_Entry = tk.Entry(self.CON_frame, width=2, font=("Times New Roman", 12, "bold"))
        self.con_Entry.insert(0, 10)
        self.con_Entry.pack(side="top",padx=0,pady=0)
        self.con_mod_output = tk.Text(
            self.CON_frame,
            wrap=tk.WORD,
            width=2,
            height=1,
            font=("Helvetica Neue", 25),
            bg="orange",
            fg="white",
            padx=5,
            pady=0,
            relief=tk.SUNKEN,
            bd=3)
        self.con_mod_output.pack(side=tk.TOP, padx=5,pady=0)
        self.con_mod_output.insert(tk.END, CS_app.calc_mod(self,self.con_Entry.get()))
        self.con_mod_output.config(state='disabled')
        self.con_label = tk.Label(self.CON_frame , text="CONSTITUTION",
            font=("Helvetica Neue", 10, "bold"),
            bg="dim grey",
            fg="black")
        self.con_label.pack(side=tk.TOP, pady=0)
        
        self.dex_Entry = tk.Entry(self.DEX_frame, width=2, font=("Times New Roman", 12, "bold"))
        self.dex_Entry.insert(0, 10)
        self.dex_Entry.pack(side="top",padx=0,pady=0)
        self.dex_mod_output = tk.Text(
            self.DEX_frame,
            wrap=tk.WORD,
            width=2,
            height=1,
            font=("Helvetica Neue", 25),
            bg="orange",
            fg="white",
            padx=5,
            pady=0,
            relief=tk.SUNKEN,
            bd=3)
        self.dex_mod_output.pack(side=tk.TOP, padx=5,pady=0)
        self.dex_mod_output.insert(tk.END, CS_app.calc_mod(self,self.dex_Entry.get()))
        self.dex_mod_output.config(state='disabled')
        self.dex_label = tk.Label(self.DEX_frame , text="DEXTERITY",
            font=("Helvetica Neue", 10, "bold"),
            bg="dim grey",
            fg="black")
        self.dex_label.pack(side=tk.TOP, pady=0)
        
        self.str_Entry = tk.Entry(self.STR_frame, width=2, font=("Times New Roman", 12, "bold"))
        self.str_Entry.insert(0, 10)
        self.str_Entry.pack(side="top",padx=0,pady=0)
        self.str_mod_output = tk.Text(
            self.STR_frame,
            wrap=tk.WORD,
            width=2,
            height=1,
            font=("Helvetica Neue", 25),
            bg="orange",
            fg="white",
            padx=5,
            pady=0,
            relief=tk.SUNKEN,
            bd=3)
        self.str_mod_output.pack(side=tk.TOP, padx=5,pady=0)
        self.str_mod_output.insert(tk.END, CS_app.calc_mod(self,self.str_Entry.get()))
        self.str_mod_output.config(state='disabled')
        
        self.str_label = tk.Label(self.STR_frame , text="STRENGTH",
            font=("Helvetica Neue", 10, "bold"),
            bg="dim grey",
            fg="black")
        self.str_label.pack(side=tk.TOP, pady=0)
        
        ability_entries = [self.str_Entry, self.dex_Entry, self.con_Entry, 
                   self.int_Entry, self.wis_Entry, self.cha_Entry]

        for entry in ability_entries:
            entry.bind('<Return>', lambda e: self.refresh())
    
#%% INSPIRATION, PROFICIENCY BONUS
        self.INSP_frame = tk.Frame(self.MID_TOP1_frame,bg="gray7")
        self.INSP_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=0)
        
        self.var1 = tk.IntVar()
        INSP_check = tk.Checkbutton(self.INSP_frame, text='INSPIRATION',font=("Times New Roman",14, "bold"), variable=self.var1, onvalue=1, offvalue=0)
        INSP_check.pack(padx=5, pady=0)
        
        self.PROF_frame = tk.Frame(self.SAVE_frame,bg="gray7")
        self.PROF_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=3)
    
        self.prof_output = tk.Text(self.PROF_frame,wrap=tk.WORD,width=1,height=1,font=("Times New Roman", 13),
            bg="gray7",fg="white",padx=5,pady=0,relief=tk.SUNKEN,bd=3)
        self.prof_output.pack(side=tk.LEFT, padx=5,pady=0)
        
        tk.Label(self.PROF_frame, text="PROFICIENCY BONUS", font=("Times New Roman", 17, "bold")).pack(side="left",padx=0,pady=0)
        
        
                
#%% SAVES       
        self.save_frame = tk.Frame(self.SAVE_frame,bg="gray7")
        self.save_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=5)
        tk.Label(self.save_frame, text="SAVING THROWS").pack(fill=tk.X,side="top",padx=5,pady=5)

        self.str_frame = tk.Frame(self.save_frame,bg="gray15")
        self.str_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=0)
        self.dex_frame = tk.Frame(self.save_frame,bg="gray15")
        self.dex_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=0)
        self.con_frame = tk.Frame(self.save_frame,bg="gray15")
        self.con_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=0)
        self.int_frame = tk.Frame(self.save_frame,bg="gray15")
        self.int_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=0)
        self.wis_frame = tk.Frame(self.save_frame,bg="gray15")
        self.wis_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=0)
        self.cha_frame = tk.Frame(self.save_frame,bg="gray15")
        self.cha_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=5,pady=0)
        
        self.str_save = tk.IntVar()
        self.dex_save = tk.IntVar()
        self.con_save = tk.IntVar()
        self.int_save = tk.IntVar()
        self.wis_save = tk.IntVar()
        self.cha_save = tk.IntVar()
        
        cha_save_check = tk.Checkbutton(self.cha_frame, variable=self.cha_save, onvalue=1, offvalue=0)
        cha_save_check.pack(side="left", padx=0, pady=0)
        self.cha_save_res = tk.Text(self.cha_frame,wrap=tk.WORD,width=2,height=1,font=("Times New Roman", 10,"bold"),
            bg="gray7",fg="white",padx=5,pady=0,relief=tk.SUNKEN,bd=3)
        self.cha_save_res.pack(side=tk.LEFT, padx=5,pady=0)
        tk.Label(self.cha_frame, text="Charisma").pack(side="left",padx=0,pady=0)
        
        wis_save_check = tk.Checkbutton(self.wis_frame, variable=self.wis_save, onvalue=1, offvalue=0)
        wis_save_check.pack(side="left", padx=0, pady=0)
        self.wis_save_res = tk.Text(self.wis_frame,wrap=tk.WORD,width=2,height=1,font=("Times New Roman", 10,"bold"),
            bg="gray7",fg="white",padx=5,pady=0,relief=tk.SUNKEN,bd=3)
        self.wis_save_res.pack(side=tk.LEFT, padx=5,pady=0)
        tk.Label(self.wis_frame, text="Wisdom").pack(side="left",padx=0,pady=0)
        
        int_save_check = tk.Checkbutton(self.int_frame, variable=self.int_save, onvalue=1, offvalue=0)
        int_save_check.pack(side="left", padx=0, pady=0)
        self.int_save_res = tk.Text(self.int_frame,wrap=tk.WORD,width=2,height=1,font=("Times New Roman", 10,"bold"),
            bg="gray7",fg="white",padx=5,pady=0,relief=tk.SUNKEN,bd=3)
        self.int_save_res.pack(side=tk.LEFT, padx=5,pady=0)
        tk.Label(self.int_frame, text="Intelligence").pack(side="left",padx=0,pady=0)
        
        con_save_check = tk.Checkbutton(self.con_frame, variable=self.con_save, onvalue=1, offvalue=0)
        con_save_check.pack(side="left", padx=0, pady=0)
        self.con_save_res = tk.Text(self.con_frame,wrap=tk.WORD,width=2,height=1,font=("Times New Roman", 10,"bold"),
            bg="gray7",fg="white",padx=5,pady=0,relief=tk.SUNKEN,bd=3)
        self.con_save_res.pack(side=tk.LEFT, padx=5,pady=0)
        tk.Label(self.con_frame, text="Constitution").pack(side="left",padx=0,pady=0)
        
        dex_save_check = tk.Checkbutton(self.dex_frame, variable=self.dex_save, onvalue=1, offvalue=0)
        dex_save_check.pack(side="left", padx=0, pady=0)
        self.dex_save_res = tk.Text(self.dex_frame,wrap=tk.WORD,width=2,height=1,font=("Times New Roman", 10,"bold"),
            bg="gray7",fg="white",padx=5,pady=0,relief=tk.SUNKEN,bd=3)
        self.dex_save_res.pack(side=tk.LEFT, padx=5,pady=0)
        tk.Label(self.dex_frame, text="Dexterity").pack(side="left",padx=0,pady=0)
        
        str_save_check = tk.Checkbutton(self.str_frame, variable=self.str_save, onvalue=1, offvalue=0)
        str_save_check.pack(side="left", padx=0, pady=0)
        self.str_save_res = tk.Text(self.str_frame,wrap=tk.WORD,width=2,height=1,font=("Times New Roman", 10,"bold"),
            bg="gray7",fg="white",padx=5,pady=0,relief=tk.SUNKEN,bd=3)
        self.str_save_res.pack(side=tk.LEFT, padx=5,pady=0)
        tk.Label(self.str_frame, text="Strength").pack(side="left",padx=0,pady=0)
        
#%% SKILLS

        
        
        # Skills Frame# Skills Frame
        
        
        
        
        
        self.Skills_frame = tk.Frame(self.SAVE_frame,bg="gray7")
        self.Skills_frame.pack(side=tk.TOP,fill=tk.Y,padx=5,pady=0)
        tk.Label(self.Skills_frame, text="SKILLS").pack(fill=tk.X,side="top",padx=5,pady=5)
        
        # Create frames and widgets for each skill
        self.Acrobatics_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Acrobatics_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Animal_Handling_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Animal_Handling_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Arcana_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Arcana_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Athletics_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Athletics_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Deception_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Deception_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.History_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.History_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Insight_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Insight_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Intimidation_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Intimidation_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Investigation_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Investigation_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Medicine_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Medicine_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Nature_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Nature_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Perception_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Perception_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Performance_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Performance_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Persuasion_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Persuasion_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Religion_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Religion_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Sleight_of_Hand_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Sleight_of_Hand_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Stealth_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Stealth_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)
        self.Survival_frame = tk.Frame(self.Skills_frame, bg="gray15")
        self.Survival_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=0)

        # Create IntVars for each skill checkbox
        self.Acrobatics_skill = tk.IntVar()
        self.Animal_Handling_skill = tk.IntVar()
        self.Arcana_skill = tk.IntVar()
        self.Athletics_skill = tk.IntVar()
        self.Deception_skill = tk.IntVar()
        self.History_skill = tk.IntVar()
        self.Insight_skill = tk.IntVar()
        self.Intimidation_skill = tk.IntVar()
        self.Investigation_skill = tk.IntVar()
        self.Medicine_skill = tk.IntVar()
        self.Nature_skill = tk.IntVar()
        self.Perception_skill = tk.IntVar()
        self.Performance_skill = tk.IntVar()
        self.Persuasion_skill = tk.IntVar()
        self.Religion_skill = tk.IntVar()
        self.Sleight_of_Hand_skill = tk.IntVar()
        self.Stealth_skill = tk.IntVar()
        self.Survival_skill = tk.IntVar()
        
        # Create skill result displays
        
        Acrobatics_skill_check = tk.Checkbutton(self.Acrobatics_frame, variable=self.Acrobatics_skill, onvalue=1, offvalue=0, height = 0)
        Acrobatics_skill_check.pack(side="left", padx=0, pady=0)
        self.Acrobatics_skill_res = tk.Text(self.Acrobatics_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"),bg="gray7", fg="white", bd=0,padx=5, pady=0, relief=tk.FLAT)
        self.Acrobatics_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Acrobatics_frame, text="Acrobatics (DEX)").pack(side="left", padx=0, pady=0)

        Animal_Handling_skill_check = tk.Checkbutton(self.Animal_Handling_frame, variable=self.Animal_Handling_skill, onvalue=1, offvalue=0, height=0)
        Animal_Handling_skill_check.pack(side="left", padx=0, pady=0)
        self.Animal_Handling_skill_res = tk.Text(self.Animal_Handling_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT,
bd=0)
        self.Animal_Handling_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Animal_Handling_frame, text="Animal Handling (WIS)").pack(side="left", padx=0, pady=0)
        
        Arcana_skill_check = tk.Checkbutton(self.Arcana_frame, variable=self.Arcana_skill, onvalue=1, offvalue=0)
        Arcana_skill_check.pack(side="left", padx=0, pady=0)
        self.Arcana_skill_res = tk.Text(self.Arcana_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Arcana_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Arcana_frame, text="Arcana (INT)").pack(side="left", padx=0, pady=0)

        Athletics_skill_check = tk.Checkbutton(self.Athletics_frame, variable=self.Athletics_skill, onvalue=1, offvalue=0, height=0)
        Athletics_skill_check.pack(side="left", padx=0, pady=0)
        self.Athletics_skill_res = tk.Text(self.Athletics_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Athletics_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Athletics_frame, text="Athletics (STR)").pack(side="left", padx=0, pady=0)

        Deception_skill_check = tk.Checkbutton(self.Deception_frame, variable=self.Deception_skill,fg="blue",onvalue=1, offvalue=0, height=0)
        Deception_skill_check.pack(side="left", padx=0, pady=0)
        self.Deception_skill_res = tk.Text(self.Deception_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Deception_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Deception_frame, text="Deception (CHA)").pack(side="left", padx=0, pady=0)

        History_skill_check = tk.Checkbutton(self.History_frame, variable=self.History_skill, onvalue=1, offvalue=0, height=0)
        History_skill_check.pack(side="left", padx=0, pady=0)
        self.History_skill_res = tk.Text(self.History_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.History_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.History_frame, text="History (INT)").pack(side="left", padx=0, pady=0)

        Insight_skill_check = tk.Checkbutton(self.Insight_frame, variable=self.Insight_skill, onvalue=1, offvalue=0, height=0)
        Insight_skill_check.pack(side="left", padx=0, pady=0)
        self.Insight_skill_res = tk.Text(self.Insight_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Insight_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Insight_frame, text="Insight (WIS)").pack(side="left", padx=0, pady=0)

        Intimidation_skill_check = tk.Checkbutton(self.Intimidation_frame, variable=self.Intimidation_skill, onvalue=1, offvalue=0, height=0)
        Intimidation_skill_check.pack(side="left", padx=0, pady=0)
        self.Intimidation_skill_res = tk.Text(self.Intimidation_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Intimidation_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Intimidation_frame, text="Intimidation (CHA)").pack(side="left", padx=0, pady=0)

        Investigation_skill_check = tk.Checkbutton(self.Investigation_frame, variable=self.Investigation_skill, onvalue=1, offvalue=0, height=0)
        Investigation_skill_check.pack(side="left", padx=0, pady=0)
        self.Investigation_skill_res = tk.Text(self.Investigation_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Investigation_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Investigation_frame, text="Investigation (INT)").pack(side="left", padx=0, pady=0)

        Medicine_skill_check = tk.Checkbutton(self.Medicine_frame, variable=self.Medicine_skill, onvalue=1, offvalue=0, height=0)
        Medicine_skill_check.pack(side="left", padx=0, pady=0)
        self.Medicine_skill_res = tk.Text(self.Medicine_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Medicine_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Medicine_frame, text="Medicine (WIS)").pack(side="left", padx=0, pady=0)

        Nature_skill_check = tk.Checkbutton(self.Nature_frame, variable=self.Nature_skill, onvalue=1, offvalue=0, height=0)
        Nature_skill_check.pack(side="left", padx=0, pady=0)
        self.Nature_skill_res = tk.Text(self.Nature_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief=tk.FLAT, bd=0)
        self.Nature_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Nature_frame, text="Nature (INT)").pack(side="left", padx=0, pady=0)

        Perception_skill_check = tk.Checkbutton(self.Perception_frame, variable=self.Perception_skill, onvalue=1, offvalue=0, height=0)
        Perception_skill_check.pack(side="left", padx=0, pady=0)
        self.Perception_skill_res = tk.Text(self.Perception_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Perception_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Perception_frame, text="Perception (WIS)").pack(side="left", padx=0, pady=0)

        Performance_skill_check = tk.Checkbutton(self.Performance_frame, variable=self.Performance_skill, onvalue=1, offvalue=0, height=0)
        Performance_skill_check.pack(side="left", padx=0, pady=0)
        self.Performance_skill_res = tk.Text(self.Performance_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Performance_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Performance_frame, text="Performance (CHA)").pack(side="left", padx=0, pady=0)

        Persuasion_skill_check = tk.Checkbutton(self.Persuasion_frame, variable=self.Persuasion_skill, onvalue=1, offvalue=0, height=0)
        Persuasion_skill_check.pack(side="left", padx=0, pady=0)
        self.Persuasion_skill_res = tk.Text(self.Persuasion_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Persuasion_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Persuasion_frame, text="Persuasion (CHA)").pack(side="left", padx=0, pady=0)

        Religion_skill_check = tk.Checkbutton(self.Religion_frame, variable=self.Religion_skill, onvalue=1, offvalue=0, height=0)
        Religion_skill_check.pack(side="left", padx=0, pady=0)
        self.Religion_skill_res = tk.Text(self.Religion_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Religion_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Religion_frame, text="Religion (INT)").pack(side="left", padx=0, pady=0)

        Sleight_of_Hand_skill_check = tk.Checkbutton(self.Sleight_of_Hand_frame, variable=self.Sleight_of_Hand_skill, onvalue=1, offvalue=0, height=0)
        Sleight_of_Hand_skill_check.pack(side="left", padx=0, pady=0)
        self.Sleight_of_Hand_skill_res = tk.Text(self.Sleight_of_Hand_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Sleight_of_Hand_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Sleight_of_Hand_frame, text="Sleight of Hand (DEX)").pack(side="left", padx=0, pady=0)

        Stealth_skill_check = tk.Checkbutton(self.Stealth_frame, variable=self.Stealth_skill, onvalue=1, offvalue=0, height=0)
        Stealth_skill_check.pack(side="left", padx=0, pady=0)
        self.Stealth_skill_res = tk.Text(self.Stealth_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Stealth_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Stealth_frame, text="Stealth (DEX)").pack(side="left", padx=0, pady=0)

        Survival_skill_check = tk.Checkbutton(self.Survival_frame, variable=self.Survival_skill, onvalue=1, offvalue=0, height=0)
        Survival_skill_check.pack(side="left", padx=0, pady=0)
        self.Survival_skill_res = tk.Text(self.Survival_frame, wrap=tk.WORD, width=2, height=1, font=("Times New Roman", 10, "bold"), bg="gray7", fg="white", padx=5, pady=0, relief= tk.FLAT, bd=0)
        self.Survival_skill_res.pack(side=tk.LEFT, padx=5, pady=0)
        tk.Label(self.Survival_frame, text="Survival (WIS)").pack(side="left", padx=0, pady=0)
                
#%% AC, INIT & SPEED
        
        
        
        self.ML_frame = tk.Frame(self.MID_TOP_frame,bg="gray14")               # armour, ac & init
        self.ML_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=0,pady=3)          
        self.MR_frame = tk.Frame(self.MID_TOP_frame,bg="gray14")               # sight & speed
        self.MR_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=0,pady=3)

        self.MLT_frame = tk.Frame(self.ML_frame,bg="gray14")                   # armour
        self.MLT_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3)
        self.MLB_frame = tk.Frame(self.ML_frame,bg="gray14")                   # ac & init
        self.MLB_frame.pack(side=tk.BOTTOM,fill=tk.BOTH,padx=0,pady=3)

        self.MRT_frame = tk.Frame(self.MR_frame,bg="gray14")                   # sight
        self.MRT_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3)
        self.MRB_frame = tk.Frame(self.MR_frame,bg="gray14")                   # speed
        self.MRB_frame.pack(side=tk.BOTTOM,fill=tk.BOTH,padx=0,pady=3)
        
        self.MLBL_frame = tk.Frame(self.MLB_frame,bg="gray14")                 # ac
        self.MLBL_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=0,pady=3)
        self.MLBR_frame = tk.Frame(self.MLB_frame,bg="gray14")                 # init
        self.MLBR_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=0,pady=3)
        
        # armour
        self.ARMOUR_list_switch = ttk.Combobox(
        self.MLT_frame,
            values=["-","Unarmoured Defense","Mithril Halfplate"],
            state="readonly",
            width=17,
            font=("Helvetica", 10),background="dim grey")
        self.ARMOUR_list_switch.current(0)  # Default: "all Classes"
        self.ARMOUR_list_switch.pack(pady=10)
        self.ARMOUR_list_switch.bind('<<ComboboxSelected>>', self.on_selected)
        
        self.AC_output = tk.Text(self.MLBL_frame,wrap=tk.WORD,width=3,height=1,font=("Times New Roman", 20),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.AC_output.pack(padx=5,pady=0)
        tk.Label(self.MLBL_frame, text="AC", font=("Times New Roman", 10, "bold")).pack(side="top",padx=0,pady=0)
        
    
        self.INIT_output = tk.Text(self.MLBR_frame,wrap=tk.WORD,width=2,height=1,font=("Times New Roman", 17),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.INIT_output.pack(side=tk.TOP, padx=5,pady=0)
        tk.Label(self.MLBR_frame, text="INITIATIVE", font=("Times New Roman", 10, "bold")).pack(side="top",padx=0,pady=0)
        
        self.SPEED_output = tk.Text(self.MRB_frame,wrap=tk.WORD,width=13,height=1,font=("Times New Roman", 17),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.SPEED_output.pack(side=tk.TOP, padx=5,pady=0)
        tk.Label(self.MRB_frame, text="Walking • Flying • Swimming • Climbing", font=("Times New Roman", 10, "bold")).pack(side="top",padx=0,pady=0)


        self.SIGHT_output = tk.Text(self.MRT_frame,wrap=tk.WORD,width=20,height=1,font=("Times New Roman", 17),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.SIGHT_output.pack(side=tk.TOP, padx=5,pady=0)
        tk.Label(self.MRT_frame, text="BRIGHT • DIM • DARK • BLIND", font=("Times New Roman", 10, "bold")).pack(side="top",padx=0,pady=0)
        
#%% HP
        self.health_frame = tk.Frame(self.MID_MID_frame,bg="gray8")
        self.health_frame.pack(side=tk.LEFT,fill=tk.NONE,padx=0,pady=3)

        self.HP_max_frame = tk.Frame(self.health_frame,bg="gray8")
        self.HP_max_frame.pack(side=tk.TOP,fill=tk.NONE,padx=0,pady=3)
        self.HP_frame = tk.Frame(self.health_frame,bg="gray8")
        self.HP_frame.pack(side=tk.TOP,fill=tk.NONE,padx=0,pady=3)
        self.THP_frame = tk.Frame(self.health_frame,bg="gray8")
        self.THP_frame.pack(fill=tk.NONE,padx=0,pady=3)
        
        
        self.HP_max_output = tk.Text(self.HP_max_frame,wrap=tk.WORD,width=3,height=1,font=("Times New Roman", 13),
            bg="gray7",fg="white",relief=tk.SUNKEN,bd=3)
        self.HP_max_output.pack(side=tk.LEFT, padx=5,pady=0)
        tk.Label(self.HP_max_frame, text=" MAX HP", font=("Times New Roman", 13, "bold")).pack(side="left",padx=0,pady=0)
        
        self.HP_entry = tk.Entry(self.HP_frame, width=3, font=("Times New Roman", 17, "bold"))
        self.HP_entry.pack(side=tk.TOP, padx=5,pady=0)
        self.HP_entry.insert(0,0)
        
        self.Temp_HP_entry = tk.Entry(self.HP_frame, width=3, font=("Times New Roman", 13, "bold"))
        self.Temp_HP_entry.pack(side=tk.LEFT, padx=5,pady=0)
        self.Temp_HP_entry.insert(0,0)
        tk.Label(self.THP_frame, text="Temp HP", font=("Times New Roman", 13, "bold")).pack(side="left",padx=0,pady=0)
#%% rests    
        self.rest_frame1 = tk.Frame(self.MID_MID_frame,bg="gray5")
        self.rest_frame1.pack(side=tk.TOP,fill=tk.NONE,padx=0,pady=3)
        self.rest_frame2 = tk.Frame(self.MID_MID_frame,bg="gray5")
        self.rest_frame2.pack(side=tk.TOP,fill=tk.NONE,padx=0,pady=3)
        
        self.SR_count_output = tk.Text(self.rest_frame1,wrap=tk.WORD,width=1,height=1,font=("Times New Roman", 13),
            bg="gray7",fg="white",relief=tk.SUNKEN,bd=3)
        self.SR_count_output.pack(side=tk.LEFT, padx=5,pady=0)
        #self.SR_count_output.insert("1.0", 0)
        self.SR_count_output.config(state='disabled')
        
        self.SR_Button = tk.Button(self.rest_frame1, text="Short Rest" ,command = self.Short_rest, font=("Times New Roman", 16, "bold"),
        bg="pink",fg="white",padx=5,pady=10,relief=tk.RAISED,bd=3)
        self.SR_Button.pack(side=tk.TOP)
        
        self.LR_Button = tk.Button(self.rest_frame2, text="Long Rest", command = self.Long_rest, font=("Times New Roman", 16, "bold"),
        bg="purple",fg="white",padx=5,pady=10,relief=tk.RAISED,bd=3)
        self.LR_Button.pack(side=tk.TOP)
        
# ------------------------------------------------------------ mid proficiencies --------------------------------------------------------------------------------------------------
       
        tk.Label(self.MID_PROF_frame, text="ARMOUR & WEAPON & LANGUAGE PROFS", font=("Times New Roman", 10, "bold")).pack(side="top",padx=0,pady=0)

        self.MP_PROF_frame = tk.Frame(self.MID_PROF_frame,bg="gray14")               
        self.MP_PROF_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3)
 
        self.ARMOUR_PROF_frame = tk.Frame(self.MP_PROF_frame,bg="gray14")               # armour prof
        self.ARMOUR_PROF_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3) 
	
        self.WEAPON_PROF_frame = tk.Frame(self.MP_PROF_frame,bg="gray14")               # weapon prof
        self.WEAPON_PROF_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3) 

        self.LANG_PROF_frame = tk.Frame(self.MP_PROF_frame,bg="gray14")               # language prof
        self.LANG_PROF_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3) 

        self.RESIST_frame = tk.Frame(self.MP_PROF_frame,bg="gray14")               # resistances
        self.RESIST_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3) 
       
        self.ADV_SAVE_frame = tk.Frame(self.MP_PROF_frame,bg="gray14")               # advantage on saves
        self.ADV_SAVE_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3) 

        self.Immunities_frame = tk.Frame(self.MP_PROF_frame,bg="gray14")               # immunities
        self.Immunities_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3) 



        tk.Label(self.ARMOUR_PROF_frame, text="ARMOUR:", font=("Times New Roman", 10, "bold")).pack(side="left",padx=0,pady=0)
        self.ARMOUR_PROF_output = tk.Text(self.ARMOUR_PROF_frame,state="disabled",wrap=tk.WORD,width=42,height=1,font=("Times New Roman", 10),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.ARMOUR_PROF_output.pack(side=tk.LEFT, padx=5,pady=0)
        
        tk.Label(self.WEAPON_PROF_frame, text="WEAPON: ", font=("Times New Roman", 10, "bold")).pack(side="left",padx=0,pady=0)
        self.WEAPON_PROF_output = tk.Text(self.WEAPON_PROF_frame,state="disabled",wrap=tk.WORD,width=42,height=1,font=("Times New Roman", 10),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.WEAPON_PROF_output.pack(side=tk.LEFT, padx=5,pady=0)
        
        tk.Label(self.LANG_PROF_frame, text="LANGUAGE:", font=("Times New Roman", 10, "bold")).pack(side="left",padx=0,pady=0)
        self.LANG_PROF_output = tk.Text(self.LANG_PROF_frame,state="disabled",wrap=tk.WORD,width=40,height=1,font=("Times New Roman", 10),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.LANG_PROF_output.pack(side=tk.LEFT, padx=5,pady=0)
        
        tk.Label(self.RESIST_frame, text="RESISTANCES:", font=("Times New Roman", 10, "bold")).pack(side="left",padx=0,pady=0)
        self.RESIST_output = tk.Text(self.RESIST_frame,state="disabled",wrap=tk.WORD,width=38,height=1,font=("Times New Roman", 10),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.RESIST_output.pack(side=tk.LEFT, padx=5,pady=0)

        tk.Label(self.ADV_SAVE_frame, text="ADV on SAVES:", font=("Times New Roman", 10, "bold")).pack(side="left",padx=0,pady=0)
        self.ADV_SAVE_output = tk.Text(self.ADV_SAVE_frame,state="disabled",wrap=tk.WORD,width=38,height=1,font=("Times New Roman", 10),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.ADV_SAVE_output.pack(side=tk.LEFT, padx=5,pady=0)

        tk.Label(self.Immunities_frame, text="Immunities:", font=("Times New Roman", 10, "bold")).pack(side="left",padx=0,pady=0)
        self.Immunities_output = tk.Text(self.Immunities_frame,state="disabled",wrap=tk.WORD,width=38,height=1,font=("Times New Roman", 10),
            bg="gray7",fg="white",relief=tk.GROOVE,bd=3)
        self.Immunities_output.pack(side=tk.LEFT, padx=5,pady=0)
        
        self.resource_frame = tk.Frame(self.MID_RIGHT_frame,bg="gray14")
        self.resource_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=0,pady=3)
        
        self.R1_frame = tk.Frame(self.MID_RIGHT_frame,bg="black")
        self.R1_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=0,pady=3)
        
        self.R1 = tk.IntVar()
        R1_check = tk.Checkbutton(self.R1_frame, variable=self.R1, onvalue=1, offvalue=0)
        R1_check.pack(side="left", padx=0, pady=0)
        self.R1_output = tk.Text(self.R1_frame,wrap=tk.WORD,width=1,height=1,font=("Times New Roman", 17),
            bg="gray7",fg="white",relief=tk.SUNKEN,bd=3)
        self.R1_output.pack(side=tk.LEFT, padx=5,pady=0)
        
        R1_name= tk.Label(self.R1_frame, text="R1", font=("Times New Roman", 17, "bold")).pack(side="left",padx=0,pady=0)
        



        
        
        
        
        self.lvl_total = int(self.lvl_Entry.get()) + int(self.lvl_Entry2.get())

#%%






    def public(self):
        try:
            self.junk_text.delete(1.0, tk.END)
            self.junk_text.insert(tk.END, "public")
            self.junk_text.see(tk.END)  # Scroll to bottom
        except ValueError:
            messagebox.showerror("Invalid input")
            
    def gm(self):
        try:
            self.junk_text.delete(1.0, tk.END)
            self.junk_text.insert(tk.END, "GM")
            self.junk_text.see(tk.END)  # Scroll to bottom
        except ValueError:
            messagebox.showerror("Invalid input")
            
    def core(self):
        try:
            self.junk_text.delete(1.0, tk.END)
            self.junk_text.insert(tk.END, "core")
            self.junk_text.see(tk.END)  # Scroll to bottom
        except ValueError:
            messagebox.showerror("Invalid input")
    def bio(self):
        try:
            self.junk_text.delete(1.0, tk.END)
            self.junk_text.insert(tk.END, "bio")
            self.junk_text.see(tk.END)  # Scroll to bottom
        except ValueError:
            messagebox.showerror("Invalid input")
    def spells(self):
        try:
            self.junk_text.delete(1.0, tk.END)
            self.junk_text.insert(tk.END, "spells")
            self.junk_text.see(tk.END)  # Scroll to bottom
        except ValueError:
            messagebox.showerror("Invalid input")
    def cog(self):
        try:
            self.junk_text.delete(1.0, tk.END)
            self.junk_text.insert(tk.END, "•")
            self.junk_text.see(tk.END)  # Scroll to bottom
        except ValueError:
            messagebox.showerror("Invalid input")
# --------------------------------------------------------------------- RESTS ------------------------------------------------------------------------------------------------

    def Short_rest(self):
        try:
            selected_class = self.class_combobox.get()
            former_hp = self.HP_entry.get()
            con_mod = int(self.con_mod_output.get("1.0", "end-1c").strip())
            sr_count = int(self.SR_count_output.get("1.0","end-1c").strip())
            new_sr_count = max(sr_count-1,0)
            # HP
            if sr_count > 0:
                if selected_class in CC_maker_data.subclass_dict:
                # Get the new subclass options
                    class_data = CC_maker_data.subclass_dict[selected_class]
                    hp_data = class_data[1]
                    hit_dice = hp_data[1]
                
                new_hp = int(former_hp) + int(random.randint(1, hit_dice)) + int(con_mod)
                
                self.HP_entry.delete(0, "end")
                self.HP_entry.insert(0, min(new_hp, int(self.HP_max_output.get("1.0","end-1c").strip())))
            
                self.SR_count_output.config(state='normal')
                self.SR_count_output.delete("1.0",tk.END)
                self.SR_count_output.insert("1.0", str(new_sr_count))
                self.SR_count_output.config(state='disabled')
            
            print(new_sr_count)
        except ValueError:
            messagebox.showerror("short rest gone wrong")
            
            
    def Long_rest(self):
        try:
            selected_class = self.class_combobox.get()
            former_hp = self.HP_entry.get()
            con_mod = int(self.con_mod_output.get("1.0", "end-1c").strip())
            # HP
            #if selected_class in CC_maker_data.subclass_dict:
                # Get the new subclass options
                #class_data = CC_maker_data.subclass_dict[selected_class]
                
                
            self.HP_entry.delete(0, "end")
            self.HP_entry.insert(0, int(self.calc_HP()))
            
            self.SR_count_output.config(state='normal')
            self.SR_count_output.delete("1.0",tk.END)
            self.SR_count_output.insert("1.0", int(self.lvl_Entry.get().strip()))
            self.SR_count_output.config(state='disabled')
        except ValueError:
            messagebox.showerror("Long rest gone wrong")
        
        
        
        
# --------------------------------------------------------------------- SIMPLE CALCS ------------------------------------------------------------------------------------------------

    
        
    def calc_AC(self):
        try: 
            if self.ARMOUR_list_switch.get() == "Mithril Halfplate":
                dex_mod = max(min(int(self.dex_mod_output.get("1.0", "end").strip()), 2),0)
                AC_res = 15 + int(dex_mod)
            elif self.ARMOUR_list_switch.get() == "Unarmoured Defense":
                dex_mod = max(int(self.dex_mod_output.get("1.0", "end").strip()),0)
                con_mod = max(int(self.con_mod_output.get("1.0", "end").strip()),0)
                AC_res = 10 + int(dex_mod) + int(con_mod)
            else:
                AC_res = "n/A" 
            return AC_res
        
        except ValueError:
                messagebox.showerror("Invalid input")
            
    def calc_HP(self):
        try:
            level = int(self.lvl_Entry.get())
            level2 = int(self.lvl_Entry2.get())
            con_mod = int(self.con_mod_output.get("1.0", "end").strip())
            max_HP = 0
            selected_class = self.class_combobox.get()
            selected_class2 = self.class_combobox2.get()
        
            if selected_class in CC_maker_data.subclass_dict and level >= 1:
                subclass_data = CC_maker_data.subclass_dict[selected_class]
                first_level_hp = subclass_data[1][0]  # First level HP
                subsequent_hp = subclass_data[1][1]   # HP per level after first
                
                max_HP += first_level_hp + (level-1) * subsequent_hp + level * con_mod

            if selected_class2 in CC_maker_data.subclass_dict and level2 >= 1:
                subclass_data = CC_maker_data.subclass_dict[selected_class2]
                
                subsequent_hp = subclass_data[1][1]   # HP per level after first
                
                max_HP += (level2) * subsequent_hp + level2 * con_mod
                
            if self.subrace_combobox.get() == "Hill":
                max_HP += (level + level2)

            return max_HP
        
        except ValueError:
            messagebox.showerror("calc_HP gone wrong")
            return 0
# ------------------------------------------------------------------------------ FIND INITIATIVE ------------------------------------------------------------
    def calc_init(self):
        try:
            initiative = 0
            initiative += int(self.dex_mod_output.get("1.0", "end").strip())
            
            return initiative
        
        except ValueError:
                messagebox.showerror("Invalid input")
                
# ------------------------------------------------------------------------------ FIND SPEED ------------------------------------------------------------
    def calc_speed(self):
        try:
            speed_text = ""
            walking = flying = swimming = climbing = 0
            Race = self.race_combobox.get()
            Subrace = self.subrace_combobox.get()
    
            # First, get base speed from race
            for race, data in CC_maker_data.Race_feats2.items():
                if race == Race:  
                    speed, sight, features, profs, adv, imm, ac = data
                    raw_walking, raw_flying, raw_swimming, raw_climbing = speed
                    
                    # Convert walking
                    if raw_walking == "-":
                        walking = 0
                    else:
                        walking = int(raw_walking)
                    
                    # Convert flying
                    if raw_flying == "-":
                        flying = 0
                    elif raw_flying == "W":
                        flying = walking
                    else:
                        flying = int(raw_flying)
                    
                    # Convert swimming
                    if raw_swimming == "-":
                        swimming = walking // 2  # Default half walking
                    elif raw_swimming == "W":
                        swimming = walking
                    else:
                        swimming = int(raw_swimming)
                    
                    # Convert climbing
                    if raw_climbing == "-":
                        climbing = walking // 2  # Default half walking
                    elif raw_climbing == "W":
                        climbing = walking
                    else:
                        climbing = int(raw_climbing)
                    
                    print(f"Race: walking={walking}, flying={flying}, swimming={swimming}, climbing={climbing}")
                    break
    
            # Then apply subrace modifiers if any
            if Subrace != "-":
                for race, data in CC_maker_data.Race_feats2.items():
                    if race == Subrace:   
                        sub_speed, sight, features, profs, adv, imm, ac = data
                        sub_walking, sub_flying, sub_swimming, sub_climbing = sub_speed
                        
                        # Handle subrace walking
                        if sub_walking != "-" and sub_walking != 0:
                            if sub_walking == "W":
                                # Keep existing walking
                                pass
                            else:
                                walking = int(sub_walking)  # Replace or add? Currently replaces
                        
                        # Handle subrace flying
                        if sub_flying != "-" and sub_flying != 0:
                            if sub_flying == "W":
                                flying = walking
                            else:
                                flying = int(sub_flying)
                        
                        # Handle subrace swimming
                        if sub_swimming != "-" and sub_swimming != 0:
                            if sub_swimming == "W":
                                swimming = walking
                            else:
                                swimming = int(sub_swimming)
                        
                        # Handle subrace climbing
                        if sub_climbing != "-" and sub_climbing != 0:
                            if sub_climbing == "W":
                                climbing = walking
                            else:
                                climbing = int(sub_climbing)
                        
                        print(f"After subrace: walking={walking}, flying={flying}, swimming={swimming}, climbing={climbing}")
                        break
    
            # Convert all to strings for display
            speed_text = f"{walking} • {flying} • {swimming} • {climbing}"
            
            if speed_text == "":  # error msg
                speed_text = "No Match"
                
            print(f"Final speed_text = {speed_text}")
            return speed_text
            
        except Exception as e:
            print(f"Error in calc_speed: {e}")
        import traceback
        traceback.print_exc()
        return "Error"



    def calc_sight(self):

        Race = self.race_combobox.get()
        Subrace = self.subrace_combobox.get()
        bright_text = "Normal"
        dim_text = "Dis"
        dark_text = 0
        blind_text = 0
    
        for race, data in CC_maker_data.Race_feats2.items():
            if race == Race:  
                speed, sight, features, profs, adv, imm, ac = data
                
                if sight == "Darkvision":
                    dark_text = 60
                    dim_text = bright_text
                if sight == "Superior Darkvision":
                    dark_text = 120
                    dim_text = bright_text
                if "Sunlight Sensitivity" in features:
                    bright_text = "Dis"
                break
    
        for race, data in CC_maker_data.Race_feats2.items():
            if race == Subrace:  
                speed, sight, features, profs, adv, imm, ac = data
                
                if sight == "Darkvision":
                    dark_text = 60
                    dim_text = bright_text
                if sight == "Superior Darkvision":
                    dark_text = 120
                    dim_text = bright_text
                if "Sunlight Sensitivity" in features:
                   bright_text = "Dis"
                break

        S_text = f"{bright_text} • {dim_text} • {dark_text} • {blind_text}"
        return S_text
                            




# ------------------------------------------------------------------------------ FIND ADV ON SAVES ------------------------------------------------------------
    def find_adv(self):
        try:
            ADV_text = ""
            ADV_list = []
            for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
               
                if race == self.race_combobox.get():
                    print(f"Race match found: {race}")
                    for cond in Adv:
                        if cond in CC_maker_data.ADV:
                            ADV_list.append(cond)
                    print(f"ADV_list = {ADV_list}")
                    break
               
            if race != "-":
                for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
                    if race == self.subrace_combobox.get():
                        for cond in Adv:
                            if cond in CC_maker_data.ADV and cond not in ADV_list:
                                ADV_list.append(cond)
                        print(f"ADV_list2 = {ADV_list}")
                        break

                for cond in ADV_list:
                    if cond == ADV_list[0]:
                        ADV_text += f"{cond}"
                    else: 
                        ADV_text += f", {cond}"
               
            return ADV_text if ADV_text else ""
        
        except Exception as e:
                print(f"Error: {e}")
                return "Error"

# ------------------------------------------------------------------------------ FIND Resistances ------------------------------------------------------------
    def find_Res(self):

        try:
            Res_text = ""
            Res_list = []
            for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
               
                if race == self.race_combobox.get():
                    for p in profs:
                        if p in CC_maker_data.Resistances:
                            Res_list.append(p)
                    print(f"Res_list = {Res_list}")
                    break
               
            if race != "-":
                for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
                    if race == self.subrace_combobox.get():
                        for p in profs:
                            if p in CC_maker_data.Resistances and p not in Res_list:
                                Res_list.append(p)
                        print(f"Res_list2 = {Res_list}")
                        break

                for p in Res_list:
                    if p == Res_list[0]:
                        Res_text += f"{p}"
                    else: 
                        Res_text += f", {p}"
               
            return Res_text if Res_text else ""
        
        except Exception as e:
                print(f"Error: {e}")
                return "Error"       

# ------------------------------------------------------------------------------ FIND Immunities ------------------------------------------------------------

    def find_Imm(self):
            print(" ---- find_Imm ---- ")
            try:
                immun_text = ""
                immun_list = []
                for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
                   
                    if race == self.race_combobox.get():
                        for cond in imm:
                            if cond in CC_maker_data.Immunities:
                                immun_list.append(cond)
                        print(f"immun_list = {immun_list}")
                        break
                   
                if race != "-":
                    for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
                        if race == self.subrace_combobox.get():
                            for cond in imm:
                                if cond in CC_maker_data.Immunities and cond not in immun_list:
                                    immun_list.append(cond)
                            print(f"immun_list2 = {immun_list}")
                            break
    
                    for cond in immun_list:
                        if cond == immun_list[0]:
                            immun_text += f"{cond}"
                        else: 
                            immun_text += f", {cond}"
                   
                return immun_text if immun_text else ""
            
            except Exception as e:
                    print(f"Error: {e}")
                    return "Error"      


# ------------------------------------------------------------------------------ FIND Armour ------------------------------------------------------------
    def find_Arm(self):
        print("\n\n ---- find_Arm ---- ")
        try:
            Arm_text = ""
            Arm_list = []
            for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
               
                if race == self.race_combobox.get():
                    for a in profs:
                        print(f"\nprof = {a}")
                        if a in CC_maker_data.Armour:
                            
                            if a == "Only Shield":
                                Arm_list.extend("No Armour","Shield")
                            else:
                                Arm_list.append(a)
                                print(f"{a} in Armour added to A_list")
                        else:
                            print(f"{a} not in Armour")
                    print(f"\n[{race}]Arm_list = {Arm_list}")
                    break
               
            if race != "-":
                for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
                    if race == self.subrace_combobox.get():
                        for a in profs:
                            print(f"\nprof = {a}")
                            if a in CC_maker_data.Armour and a not in Arm_list:
                                
                                if a == "Only Shield":
                                    Arm_list.extend("No Armour","Shield")
                                else:
                                    Arm_list.append(a)
                                    print(f"{a} in Armour added to Arm_list")
                            else:
                                print(f"{a} not in Armour")
                        print(f"\n[{race}]Arm_list2 = {Arm_list}")
                        break

            print(f"Class: {self.class_combobox.get()}")
            for Class, (hit_dice, armour, weapons, tools, saves, skills, equipment) in CC_maker_data.Class_profs.items():
                print(f"{Class}: {armour}")
                if Class == self.class_combobox.get():
                    for a in armour:
                        print(f"prof = {a}")
                        if a in CC_maker_data.Armour and a in Arm_list:
                            print(f"{a} already in Arm_list")
                        elif a in CC_maker_data.Armour and a not in Arm_list:
                            if a == "Only Shield":
                                Arm_list.extend("No Armour","Shield")
                            else:
                                Arm_list.append(a)
                                print(f"{a} in Armour added to A_list")
                        else:
                            print(f"{a} not in Armour")
                    print(f"\n[{Class}]Arm_list = {Arm_list}")
                    break

            


            for a in Arm_list:
                if a == Arm_list[0]:
                    Arm_text += f"{a}"
                else: 
                    Arm_text += f", {a}"
            
            return Arm_text if Arm_text else "None" 
        
        except Exception as e:
                print(f"Error: {e}")
                return "Error"      


# ------------------------------------------------------------------------------ FIND Weapons ------------------------------------------------------------
    def find_Weap(self):
        print("\n\n ---- find_Weap ---- ")
        try:
            W_text = ""
            W_list = []
            for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
               
                if race == self.race_combobox.get():
                    for w in profs:
                        print(f"\nprof = {w}")
                        if w in CC_maker_data.Weapons:
                            if w == "All_Weapons":
                                W_list.append("Simple")
                                W_list.append("Martial")
                            elif w == "Simple":
                                W_list.append("Simple")
                            elif w == "Martial":
                                W_list.append("Martial")
                            else:
                                W_list.append(w)
                                print(f"{w} in Weapons added to W_list")
                        else:
                            print(f"{w} not in Weapons")
                    print(f"\n[{race}]W_list = {W_list}")
                    break
               
            if race != "-":
                for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
                    if race == self.subrace_combobox.get():
                        for w in profs:
                            print(f"\nprof = {w}")
                            if w in CC_maker_data.Weapons and w not in W_list:
                                if w == "All_Weapons":
                                    W_list = ["Simple","Martial"]
                                if w == "Simple":
                                    W_list = ["Simple"]
                                if w == "Martial":
                                    W_list = ["Martial"]
                                else:
                                    W_list.append(w)
                                    print(f"{w} in Weapons added to W_list")
                            else:
                                print(f"{w} not in Weapons")
                        print(f"\n[{race}]W_list2 = {W_list}")
                        break

                for w in W_list:
                    if w == W_list[0]:
                        W_text += f"{w}"
                    else: 
                        W_text += f", {w}"
               
            return W_text if W_text else "" 
        
        except Exception as e:
                print(f"Error: {e}")
                return "Error"  

# ------------------------------------------------------------------------------ FIND Languages ------------------------------------------------------------
    def find_Lang(self):
        print("\n\n ---- find_Lang ---- ")
        try:
            L_text = ""
            L_list = []
            for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
               
                if race == self.race_combobox.get():
                    for L in profs:
                        print(f"\nprof = {L}")
                        if L in CC_maker_data.Languages:
                            L_list.append(L)
                            print(f"{L} in Languages added to L_list")
                        else:
                            print(f"{L} not in Languages")
                    print(f"\n[{race}]L_list = {L_list}")
                    break
               
            if race != "-":
                for race, (speed, sight, features, profs, Adv, imm, ac) in CC_maker_data.Race_feats2.items():
                    if race == self.subrace_combobox.get():
                        for L in profs:
                            print(f"\nprof = {L}")
                            if L in CC_maker_data.Languages and L not in L_list:
                                L_list.append(L)
                                print(f"{L} in Languages added to L_list")
                            else:
                                print(f"{L} not in Languages")
                        print(f"\n[{race}]L_list2 = {L_list}")
                        break

                L_text += "Common"
                for L in L_list:
                    L_text += f", {L}"
               
            return L_text if L_text else "None" 
        
        except Exception as e:
                print(f"Error: {e}")
                return "Error"      


# ------------------------------------------------------------------------------ calc mod, prof, save & bgr profs------------------------------------------------------------
    def calc_mod(self, score):
        try:
            new_mod_ouput = int(int(score)-10)//2  if int(score) >= 3 else -4
            return new_mod_ouput
        
        except ValueError:
                messagebox.showerror("Invalid input")

# finish calc_save. dependent on prof bonus, depend on level and table                
   
    def calc_prof(self, level):
         try:
             return int((int(level) - 1) // 4 + 2)
         
         except ValueError:
                 messagebox.showerror("Invalid input")
                 
    def calc_save_skill(self, AS_mod, checkbox,lvl):
        try:
            # Get proficiency bonus for the level
            prof_bonus = self.calc_prof(lvl)
        
            # Calculate save value: ability modifier + proficiency if checkbox is checked
            new_value = int(AS_mod) + (prof_bonus if checkbox.get() == 1 else 0)
            return new_value
        
        except ValueError:
            messagebox.showerror("Invalid input")
            return 0
    
# --------------------------------------------------------------------------- set skills ------------------------------------------------------------------------
    def apply_bgr(self, Event=None):
        try:
            bgr = self.background_combobox.get()
            print(f"Background: {bgr}")
    
            skill_vars = {
                "Acrobatics": self.Acrobatics_skill,
                "Animal Handling": self.Animal_Handling_skill,
                "Arcana": self.Arcana_skill,
                "Athletics": self.Athletics_skill,
                "Deception": self.Deception_skill,
                "History": self.History_skill,
                "Insight": self.Insight_skill,
                "Intimidation": self.Intimidation_skill,
                "Investigation": self.Investigation_skill,
                "Medicine": self.Medicine_skill,
                "Nature": self.Nature_skill,
                "Perception": self.Perception_skill,
                "Performance": self.Performance_skill,
                "Persuasion": self.Persuasion_skill,
                "Religion": self.Religion_skill,
                "Sleight of Hand": self.Sleight_of_Hand_skill,
                "Stealth": self.Stealth_skill,
                "Survival": self.Survival_skill
            }
    
            # First, unset previous background skills if they exist
            if hasattr(self, 'previous_background'):
                for b, profs in CC_maker_data.bgr_profs.items():
                    if b == self.previous_background:
                        print(f"Previous Background: {b}")
                        print(f"Profs: {profs}")
                        for prof in profs:
                            print(f"Prof: -{prof}-")
                            for skill_name, skill_var in skill_vars.items():
                                if skill_name in prof:
                                    print(f"Setting {skill_name} OFF")
                                    skill_var.set(0)
                                    break
                        break
    
            # Then set new background skills
            for b, profs in CC_maker_data.bgr_profs.items():
                if b == bgr:
                    print(f"Background found matching {bgr}: {b}")
                    print(f"Profs: {profs}")
                    for prof in profs:
                        print(f"Prof: -{prof}-")
                        for skill_name, skill_var in skill_vars.items():
                            if skill_name in prof:
                                print(f"Setting {skill_name} ON")
                                skill_var.set(1)
                                break
                    break
    
            # Store current background for next time
            self.previous_background = bgr
    
            # Refresh to update skill displays
            self.refresh()
    
        except Exception as e:
            print(f"Error in apply_bgr: {e}")
            import traceback
            traceback.print_exc()
            return "Error"
        

    def set_saves(self, Event=None):
        try:
            Class = self.class_combobox.get()
            print(f"Class: {Class}")
    
            save_vars = {
                "Str":     self.str_save,
                "Dex":    self.dex_save,
                "Con": self.con_save,
                "Int": self.int_save,
                "Wis":       self.wis_save,
                "Cha":     self.cha_save
            }
    
            # First, unset previous background skills if they exist
            if hasattr(self, 'previous_class'):
                for c, (HD, Arm, Weap, Tools, saves, skills, equip) in CC_maker_data.Class_profs.items():
                    if c == self.previous_class:
                        print(f"Previous Class: {c}")
                        print(f"Saves: {saves}")
                        for save in saves:
                            print(f"Save: -{save}-")
                            for save_name, save_var in save_vars.items():
                                if save_name in save:
                                    print(f"Setting {save_name} OFF")
                                    save_var.set(0)
                                    break
                        break
    
            # Then set new background skills
            for c, (HD, Arm, Weap, Tools, saves, skills, equip) in CC_maker_data.Class_profs.items():
                if c == Class:
                    print(f"Class found matching {Class}: {c}")
                    print(f"Saves: {saves}")
                    for save in saves:
                        print(f"Save: -{save}-")
                        for save_name, save_var in save_vars.items():
                            if save_name in save:
                                print(f"Setting {save_name} ON")
                                save_var.set(1)
                                break
                    break
    
            # Store current class for next time
            self.previous_class = Class
    
            # Refresh to update skill displays
            self.refresh()
    
        except Exception as e:
            print(f"Error in set_saves: {e}")
            import traceback
            traceback.print_exc()
            return "Error"
    

        
# --------------------------------------------------------------------- FEATURE FUNCTIONS ------------------------------------------------------------------------------------------------

#%% complex funcs     

    def on_selected(self, event=None):
        selected_class = self.class_combobox.get()
        selected_class2 = self.class_combobox2.get()
        selected_subclass = self.subclass_combobox.get()
        selected_subclass2 = self.subclass_combobox2.get()
        selected_race = self.race_combobox.get()
        
        
        if selected_class in CC_maker_data.subclass_dict:
            subclasses_data = CC_maker_data.subclass_dict[selected_class]
            subclasses = subclasses_data[0]
            self.subclass_combobox['values'] = subclasses
            
            # Set to first subclass option or keep current if available
            current_subclass = self.subclass_combobox.get()
            if current_subclass not in subclasses:
                self.subclass_combobox.set(subclasses[0] if subclasses else "")
            
            print(f"DEBUG: Class changed to {selected_class}, subclasses: {subclasses}")
        
        if selected_class2 in CC_maker_data.subclass_dict:
            subclasses_data = CC_maker_data.subclass_dict[selected_class2]
            subclasses = subclasses_data[0]
            self.subclass_combobox2['values'] = subclasses
            
            # Set to first subclass option or keep current if available
            current_subclass = self.subclass_combobox2.get()
            if current_subclass not in subclasses:
                self.subclass_combobox2.set(subclasses[0] if subclasses else "")
            
            print(f"DEBUG: Class changed to {selected_class2}, subclasses: {subclasses}")

        
        if selected_race in CC_maker_data.Lineages:
            # Get the new subrace options
            new_subraces = CC_maker_data.Lineages[selected_race]
            
            # Update the subrace combobox values
            self.subrace_combobox['values'] = new_subraces
            
            # Set to first subracee option or keep current if available
            current_subrace = self.subrace_combobox.get()
            if current_subrace not in new_subraces:
                self.subrace_combobox.set(new_subraces[0] if new_subraces else "")
            
            print(f"DEBUG: Race changed to {selected_race}, Subraces: {new_subraces}")
        
        self.update_abilities_by_class(selected_class, selected_subclass, selected_class2, selected_subclass2)
        self.refresh()
#%% 
    def update_bgr_profs():
        pass


#%%   feature funcs   
    def create_ability_selector(self, parent):
        """Create a permanently open ability selector with description display"""
        
        # Main frame for the ability selector
        main_frame = tk.Frame(parent, bg="gray14")
        main_frame.pack(fill=tk.NONE, side=tk.TOP,expand=False, padx=5, pady=5)
        
        # Title
        tk.Label(main_frame, text="ABILITIES & FEATURES", 
                font=("Times New Roman", 14, "bold"), bg="gray14", fg="white").pack(pady=5)
        
        # Container for list and description
        content_frame = tk.Frame(main_frame, bg="gray14")
        content_frame.pack(fill=tk.NONE, expand=False)
        
        # Left side - Ability list (permanently visible)
        list_frame = tk.Frame(content_frame, bg="gray15", relief=tk.SUNKEN, bd=1)
        list_frame.pack(side=tk.LEFT, fill=tk.NONE, padx=(0, 5))
        
        # Listbox with scrollbar
        list_label = tk.Label(list_frame, text="Select Ability:", 
                             font=("Helvetica", 10, "bold"), bg="gray15", fg="white")
        list_label.pack(pady=5)
        
        self.abilities_listbox = tk.Listbox(list_frame, 
                                           bg="grey12", 
                                           fg="white",
                                           selectbackground="black",
                                           selectforeground="white",
                                           font=("Helvetica", 11),
                                           height=11,
                                           )
        self.abilities_listbox.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=10, pady=0)
        
        list_scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
        list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.abilities_listbox.config(yscrollcommand=list_scrollbar.set)
        list_scrollbar.config(command=self.abilities_listbox.yview)
        
        # Right side - Description display
        desc_frame = tk.Frame(content_frame, bg="gray15", relief=tk.SUNKEN, bd=1)
        desc_frame.pack(side=tk.RIGHT, fill=tk.NONE, expand=False)
        
        desc_label = tk.Label(desc_frame, text="Description:", 
                             font=("Helvetica", 10, "bold"), bg="gray15", fg="white")
        desc_label.pack(pady=5)
        
        self.ability_desc_text = scrolledtext.ScrolledText(
            desc_frame,
            wrap=tk.WORD,
            bg="gray10",
            fg="white",
            font=("Helvetica", 13),
            
            
            state="disabled",
            height=10
        )
        self.ability_desc_text.pack(fill=tk.NONE, expand=False, padx=10,
        pady=0)
        
        # Bind selection event
        self.abilities_listbox.bind('<<ListboxSelect>>', self.on_ability_selected)
        
        return main_frame

    def on_ability_selected(self, event):
        """Handle ability selection and display description"""
        if not self.abilities_listbox.curselection():
            return
        
        index = self.abilities_listbox.curselection()[0]
        full_ability_text = self.abilities_listbox.get(index)
        
        if "] " in full_ability_text:
            ability_name = full_ability_text.split("] ", 1)[1]
        else:
            ability_name = full_ability_text

        Source_Initial = str(full_ability_text.split("]",1)[0]).strip("[")
        
	
        # Get description from your data store
        description = self.get_ability_description(Source_Initial, ability_name)
        
        # Update description text
        self.ability_desc_text.config(state="normal")
        self.ability_desc_text.delete(1.0, tk.END)
        self.ability_desc_text.insert(tk.END, description)
        self.ability_desc_text.config(state="disabled")
        
    
        
        
        

    def get_ability_description(self, source, ability_name):
        """Get description for a specific ability"""

        
        if ability_name in all_ability_data:
            return all_ability_data[ability_name]
    
    # Then check in CLASS_BASED_DICT:
        if source in CLASS_BASED_DICT:
            class_dict = CLASS_BASED_DICT[source]
            if ability_name in class_dict:
                return class_dict[ability_name]
            else:
                return f"Description not available for \"{ability_name}\" from \"{source}\""
        else:
            return f"Description not available for \'{ability_name}\' from \'{source}\'"
       
    
    
    


    def update_abilities_by_class(self, class_name, subclass_name, class_name2, subclass_name2):                    #"""Update the abilities list based on character class & subclass"""
        self.abilities_listbox.delete(0, tk.END)
        
        try:
            current_level = int(self.lvl_Entry.get().strip()) 
            current_level2 = int(self.lvl_Entry2.get().strip())
        except ValueError:
            current_level = 1
            current_level2 = 0
            
        all_abilities = []
        
        # Use the imported module-level constants instead of self attributes
        if class_name in CC_maker_data.CLASS_ABILITIES_LIST:
            Source_Initial = str(class_name).strip()
            for feat_level, abilities in CC_maker_data.CLASS_ABILITIES_LIST[class_name]:
                if feat_level <= current_level:
                    for ability in abilities:
                        all_abilities.append((feat_level, ability, Source_Initial))
    
        if class_name2 in CC_maker_data.CLASS_ABILITIES_LIST:
            Source_Initial = str(class_name2).strip()
            for feat_level, abilities in CC_maker_data.CLASS_ABILITIES_LIST[class_name2]:
                if feat_level <= current_level2:
                    for ability in abilities:
                        all_abilities.append((feat_level, ability, Source_Initial))
                        
        if subclass_name in CC_maker_data.CLASS_ABILITIES_LIST:             
            Source_Initial = str(subclass_name)
            for feat_level, abilities in CC_maker_data.CLASS_ABILITIES_LIST[subclass_name]:
                if feat_level <= current_level:
                    for ability in abilities:
                        all_abilities.append((feat_level, ability, Source_Initial))
                        
        if subclass_name2 in CC_maker_data.CLASS_ABILITIES_LIST:             
            Source_Initial = str(subclass_name2)
            for feat_level, abilities in CC_maker_data.CLASS_ABILITIES_LIST[subclass_name2]:
                if feat_level <= current_level2:
                    for ability in abilities:
                        all_abilities.append((feat_level, ability, Source_Initial))
                        
        # Sort by level
        all_abilities.sort(key=lambda x: x[0])
    
        # Add to listbox in sorted order
        for feat_level, ability, source in all_abilities:
            self.abilities_listbox.insert(tk.END, f"[{source}][{feat_level}] {ability}")
                        
        # Clear description when class changes
        self.ability_desc_text.config(state="normal")
        self.ability_desc_text.delete(1.0, tk.END)
        self.ability_desc_text.config(state="disabled")
        


    

        
#%% refresh, save, load          
    def refresh(self):
        try:
            
            current_level = int(self.lvl_Entry.get()) if 1 <= int(self.lvl_Entry.get()) <= 20 else 1
            
            entry_mod_dict = {
                self.str_Entry: self.str_mod_output,
                self.dex_Entry: self.dex_mod_output,
                self.con_Entry: self.con_mod_output,
                self.int_Entry: self.int_mod_output,
                self.wis_Entry: self.wis_mod_output,
                self.cha_Entry: self.cha_mod_output,
                
                }
            
            text_dict = {
                self.prof_output: (self.lvl_Entry, self.lvl_Entry2) 
                }
            
            save_dict = {
                self.str_mod_output: (self.str_save, self.str_save_res),
                self.dex_mod_output: (self.dex_save, self.dex_save_res),
                self.con_mod_output: (self.con_save, self.con_save_res),
                self.int_mod_output: (self.int_save, self.int_save_res),
                self.wis_mod_output: (self.wis_save, self.wis_save_res),
                self.cha_mod_output: (self.cha_save, self.cha_save_res),
                
                
                }
            
            # Skill mappings - FIXED: Use strings as keys instead of IntVar objects
            skill_dict = {
                # STR skills
                "Athletics": (self.str_mod_output, self.Athletics_skill, self.Athletics_skill_res),
                
                # DEX skills  
                "Acrobatics": (self.dex_mod_output, self.Acrobatics_skill, self.Acrobatics_skill_res),
                "Sleight_of_Hand": (self.dex_mod_output, self.Sleight_of_Hand_skill, self.Sleight_of_Hand_skill_res),
                "Stealth": (self.dex_mod_output, self.Stealth_skill, self.Stealth_skill_res),
                
                # INT skills
                "Arcana": (self.int_mod_output, self.Arcana_skill, self.Arcana_skill_res),
                "History": (self.int_mod_output, self.History_skill, self.History_skill_res),
                "Investigation": (self.int_mod_output, self.Investigation_skill, self.Investigation_skill_res),
                "Nature": (self.int_mod_output, self.Nature_skill, self.Nature_skill_res),
                "Religion": (self.int_mod_output, self.Religion_skill, self.Religion_skill_res),
                
                # WIS skills
                "Animal_Handling": (self.wis_mod_output, self.Animal_Handling_skill, self.Animal_Handling_skill_res),
                "Insight": (self.wis_mod_output, self.Insight_skill, self.Insight_skill_res),
                "Medicine": (self.wis_mod_output, self.Medicine_skill, self.Medicine_skill_res),
                "Perception": (self.wis_mod_output, self.Perception_skill, self.Perception_skill_res),
                "Survival": (self.wis_mod_output, self.Survival_skill, self.Survival_skill_res),
                
                # CHA skills
                "Deception": (self.cha_mod_output, self.Deception_skill, self.Deception_skill_res),
                "Intimidation": (self.cha_mod_output, self.Intimidation_skill, self.Intimidation_skill_res),
                "Performance": (self.cha_mod_output, self.Performance_skill, self.Performance_skill_res),
                "Persuasion": (self.cha_mod_output, self.Persuasion_skill, self.Persuasion_skill_res),
                
                
            }
            
            for AS,mod in entry_mod_dict.items():
                updated = int(AS.get()) if int(AS.get()) >= 3 else 3
                mod.config(state='normal')
                mod.delete(1.0, tk.END)
                mod.insert(tk.END, CS_app.calc_mod(self,updated))
                mod.see(tk.END)
                mod.config(state='disabled')
            
            for prof, (lvl, lvl2) in text_dict.items():
                updated = max(int(self.lvl_Entry.get()),0) + max(int(self.lvl_Entry2.get()),0)
                prof.config(state='normal')
                prof.delete(1.0, tk.END)
                prof.insert(tk.END, CS_app .calc_prof(self, updated))
                prof.see(tk.END)
                prof.config(state='disabled')
                
            # Update saving throws
            
            
            
            for mod_output, (save_checkbox, save_display) in save_dict.items():
                ability_mod = int(mod_output.get("1.0", "end").strip()) if mod_output.get("1.0", "end").strip() != None else 0
                save_display.config(state='normal')
                save_display.delete(1.0, tk.END)
                save_value = self.calc_save_skill(ability_mod, save_checkbox, current_level)
                save_display.insert(tk.END, save_value)
                save_display.see(tk.END)
                save_display.config(state='disabled')
            
            # Update skills - FIXED: Iterate through values instead of keys
            for skill_name, (ability_mod_output, skill_checkbox, skill_display) in skill_dict.items():
                ability_mod = int(ability_mod_output.get("1.0", "end").strip())
                skill_display.config(state='normal')
                skill_display.delete(1.0, tk.END)
                skill_value = self.calc_save_skill(ability_mod, skill_checkbox, current_level)
                skill_display.insert(tk.END, skill_value)
                skill_display.see(tk.END)
                skill_display.config(state='disabled')
              

            ref_dict = {
                self.AC_output: [self.calc_AC(),"calc_AC"],
                self.SIGHT_output: [self.calc_sight(),"calc_sight"],
                self.SPEED_output: [self.calc_speed(),"calc_speed"],
                self.ADV_SAVE_output: [self.find_adv(),"find_adv"],
                self.Immunities_output: [self.find_Imm(),"find_Imm"],
                self.RESIST_output: [self.find_Res(),"find_Res"],
                self.WEAPON_PROF_output: [self.find_Weap(),"find_Weap"],
                self.ARMOUR_PROF_output: [self.find_Arm(),"find_Arm"],
                self.LANG_PROF_output: [self.find_Lang(),"find_Lang"],
                self.INIT_output: [self.calc_init(),"calc_init"],
                self.HP_max_output: [self.calc_HP(),"calc_HP"]}
            
            for output, [result, func] in ref_dict.items():
               
                if result is None:
                    result = "None"
                print(f"DEBUG: Setting {output} as {result} using {func}")
                output.config(state='normal')
                output.delete(1.0, tk.END)
                
                output.insert(tk.END, result)
                output.see(tk.END)
                output.config(state='disabled')
                
            current_class = self.class_combobox.get()
            current_subclass = self.subclass_combobox.get()
            current_class2 = self.class_combobox2.get()
            current_subclass2 = self.subclass_combobox2.get()
            self.update_abilities_by_class(current_class, current_subclass, current_class2, current_subclass2)
            self.previous_background = self.background_combobox.get()
            self.previous_class = self.class_combobox.get()
            
                
                
                
            
                
        except ValueError:
            messagebox.showerror("Invalid input")
         
    def save_info(self):
        try:
            # Automated data collection - all fields in one place
            data = {
                # Character info
                "name": self.name_text.get("1.0", "end").strip(),
                "class": self.class_combobox.get(),  
                "subclass": self.subclass_combobox.get(),
                "class2": self.class_combobox2.get(),  
                "subclass2": self.subclass_combobox2.get(),
                "race": self.race_combobox.get(),
                "subrace": self.subrace_combobox.get(),
                "background": self.background_combobox.get(),
           
                "level": self.lvl_Entry.get(),
                "level2": self.lvl_Entry2.get(),
                "type": self.type_Entry.get(),
               
                "alignment": self.align_Entry.get(),
                
                
                # Ability scores
                "str": self.str_Entry.get(),
                "dex": self.dex_Entry.get(),
                "con": self.con_Entry.get(),
                "int": self.int_Entry.get(),
                "wis": self.wis_Entry.get(),
                "cha": self.cha_Entry.get(),
                
                # Inspiration
                "inspiration": self.var1.get(),
                
                "proficiency": self.prof_output.get("1.0","end").strip(),
                
                "str_save": self.str_save.get(),
                "dex_save": self.dex_save.get(),
                "con_save": self.con_save.get(),
                "int_save": self.int_save.get(),
                "wis_save": self.wis_save.get(),
                "cha_save": self.cha_save.get(),
                
                "Acrobatics_skill": self.Acrobatics_skill.get(),
                "Animal_Handling_skill": self.Animal_Handling_skill.get(),
                "Arcana_skill": self.Arcana_skill.get(),
                "Athletics_skill": self.Athletics_skill.get(),
                "Deception_skill": self.Deception_skill.get(),
                "History_skill": self.History_skill.get(),
                "Insight_skill": self.Insight_skill.get(),
                "Intimidation_skill": self.Intimidation_skill.get(),
                "Investigation_skill": self.Investigation_skill.get(),
                "Medicine_skill": self.Medicine_skill.get(),
                "Nature_skill": self.Nature_skill.get(),
                "Perception_skill": self.Perception_skill.get(),
                "Performance_skill": self.Performance_skill.get(),
                "Persuasion_skill": self.Persuasion_skill.get(),
                "Religion_skill": self.Religion_skill.get(),
                "Sleight_of_Hand_skill": self.Sleight_of_Hand_skill.get(),
                "Stealth_skill": self.Stealth_skill.get(),
                "Survival_skill": self.Survival_skill.get(),
                
                "ARMOUR_list_switch": self.ARMOUR_list_switch.get(),
                
                "HP": self.HP_entry.get(),
                "Temp_HP": self.Temp_HP_entry.get(),
                
                "SR_count": self.SR_count_output.get("1.0","end").strip()
                
                }
            
            print(f"DEBUG: Saving inspiration value: {self.var1.get()}")
            print(f"DEBUG: var1 type: {type(self.var1.get())}")

            with open(self.save_file_path, "w") as f:
                json.dump(data, f, indent=4)

            messagebox.showinfo("Saved", f"Character data saved to:\n{self.save_file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Could not save data:\n{e}")

    def load_info(self):
        try:
            if not os.path.exists(self.save_file_path):
                messagebox.showwarning("No Save Found", "No saved character data found yet.")
                return

            with open(self.save_file_path, "r") as f:
                data = json.load(f)

        # Define mapping between data keys and widget attributes
            field_mappings = {
                "name": ("name_text", "text_widget"),  # (attribute, widget_type)
                
                
                "class": ("class_combobox", "option"),
                "subclass": ("subclass_combobox", "option"),
                "class2": ("class_combobox2", "option"),
                "subclass2": ("subclass_combobox2", "option"),
                "race":     ("race_combobox", "option"),
                "subrace": ("subrace_combobox", "option"),
                "background": ("background_combobox", "option"),
                "level": ("lvl_Entry", "entry"),
                "level2": ("lvl_Entry2", "entry"),
                
                "type": ("type_Entry", "entry"),
                "alignment": ("align_Entry", "entry"),
                
                "str": ("str_Entry", "entry"),
                "dex": ("dex_Entry", "entry"), 
                "con": ("con_Entry", "entry"),
                "int": ("int_Entry", "entry"),
                "wis": ("wis_Entry", "entry"),
                "cha": ("cha_Entry", "entry"),
                
                "inspiration": ("var1","checkbox"),
                
                "str_save": ("str_save", "checkbox"),
                "dex_save": ("dex_save", "checkbox"),
                "con_save": ("con_save", "checkbox"),
                "int_save": ("int_save", "checkbox"),
                "wis_save": ("wis_save", "checkbox"),
                "cha_save": ("cha_save", "checkbox"),
                
                "Acrobatics_skill": ("Acrobatics_skill", "checkbox"),
                "Animal_Handling_skill": ("Animal_Handling_skill", "checkbox"),
                "Arcana_skill": ("Arcana_skill", "checkbox"),
                "Athletics_skill": ("Athletics_skill", "checkbox"),
                "Deception_skill": ("Deception_skill", "checkbox"),
                "History_skill": ("History_skill", "checkbox"),
                "Insight_skill": ("Insight_skill", "checkbox"),
                "Intimidation_skill": ("Intimidation_skill", "checkbox"),
                "Investigation_skill": ("Investigation_skill", "checkbox"),
                "Medicine_skill": ("Medicine_skill", "checkbox"),
                "Nature_skill": ("Nature_skill", "checkbox"),
                "Perception_skill": ("Perception_skill", "checkbox"),
                "Performance_skill": ("Performance_skill", "checkbox"),
                "Persuasion_skill": ("Persuasion_skill", "checkbox"),
                "Religion_skill": ("Religion_skill", "checkbox"),
                "Sleight_of_Hand_skill": ("Sleight_of_Hand_skill", "checkbox"),
                "Stealth_skill": ("Stealth_skill", "checkbox"),
                "Survival_skill": ("Survival_skill", "checkbox"),
                
                "ARMOUR_list_switch": ("ARMOUR_list_switch", "option"),
                
                "HP": ("HP_entry","entry"),
                "Temp_HP": ("Temp_HP_entry","entry"),
                
                "SR_count": ("SR_count_output","fixed_output")
                }

        # Restore all fields automatically
            for data_key, (widget_attr, widget_type) in field_mappings.items():
                if data_key in data and hasattr(self, widget_attr):
                    
                
                    if widget_type == "text_widget":
                        widget = getattr(self, widget_attr)
                        widget.config(state="normal")
                        widget.delete("1.0", "end")
                        widget.insert("end", str(data[data_key]))
                        widget.config(state="disabled")
                        
                    if widget_type  == "fixed_output":
                        print(f"DEBUG: Setting output-type {widget_attr} as {str(data[data_key])}")
                        widget = getattr(self, widget_attr)
                        widget.config(state='normal')
                        widget.delete("1.0", "end")
                        widget.insert("1.0", str(data[data_key]))
                        widget.config(state='disabled')
                        
                        
                    elif widget_type == "entry":
                        widget = getattr(self, widget_attr)
                        widget.delete(0, "end")
                        widget.insert(0, str(data[data_key]))
                    elif widget_type == "checkbox":
                        var_widget = getattr(self, widget_attr)
                        var_widget.set(int(data[data_key]))
                        print(f"DEBUG: Setting checkbox-type {widget_attr} to {int(data[data_key])}")
                    elif widget_type == "option":
                        opt_widget = getattr(self, widget_attr)
                        opt_widget.set(str(data[data_key]))
            
            if "class" in data:
            # Update subclass options based on loaded class
                self.on_selected()
            if "class2" in data:
                self.on_selected()
            # Set the subclass to the saved value after updating options
            if "subclass" in data:
                self.subclass_combobox.set(str(data["subclass"]))
            if "subclass2" in data:
                self.subclass_combobox2.set(str(data["subclass2"]))
                
            if "race" in data:
            # Update subrace options based on loaded race
                self.on_selected()
            # Set the subrace to the saved value after updating options
            if "subrace" in data:
                self.subrace_combobox.set(str(data["subrace"]))
                
            # messagebox.showinfo("Loaded", f"Character data loaded from:\n{self.save_file_path}")
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load data:\n{e}")


    

#%%            
if __name__ == "__main__":
    root = tk.Tk()
    app = CS_app(root)
    root.mainloop()



