#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 23 18:25:16 2025

@author: nicholasbyrne
"""


import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from CC_new import CC  # Make sure CC_new.py is in the same directory
from AS_imp import AS, AS2
from dmg_roll import dmg
from background import bgrnd, present_BACK


class CC_app:
    def __init__(self, root):
        self.root = root
        self.root.title("D&D General Application")
        self.root.geometry("1200x860")
        self.root.minsize(1440,855)
        self.setup_ui()
        self.use_3d6 = tk.BooleanVar()
        self.use_3d6.set(False)

    def setup_ui(self):
        # Configure window background
        self.root.config(bg="black")
        
        # Main Title Label
        self.title_label = tk.Label(
            self.root,
            text="Choose what functions you would like to use!",
            font=("Helvetica", 22, "bold"),
            bg="black",
            fg="white")
        self.title_label.pack(side=tk.TOP)

        
        
        
        # top frame placing
        self.top_frame = tk.Frame(self.root,bg="grey")
        self.top_frame.pack(side=tk.TOP,fill=tk.BOTH,pady=15)
        
        
        
        
        # DMG roller
        self.DMG_frame = tk.Frame(self.top_frame, bg="dim grey", padx=10, pady=20)
        self.DMG_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=5,pady=10)
        # Main Title Label
        self.DMG_title_label = tk.Label(
            self.DMG_frame ,
            text="🎲 Damage Roller🎲",
            font=("Helvetica", 20, "bold"),
            bg="black",
            fg="white")
        self.DMG_title_label.pack(side=tk.TOP, pady=0)
        
        self.HD_frame = tk.Frame(self.DMG_frame, bg="dim grey")
        self.HD_frame.pack(expand=True, fill=tk.Y,padx=5,pady=5)
        tk.Label(self.HD_frame, text="Enter weapon dice: ").pack(side="left",padx=15,pady=5)
        self.NoHD_Entry = tk.Entry(self.HD_frame, width=5)
        self.NoHD_Entry.insert(0, 2)
        self.NoHD_Entry.pack(side="left", pady=5)
        tk.Label(self.HD_frame, text="d",font=("Helvetica",18)).pack(side="left",pady=5)
        self.HD_Entry = tk.Entry(self.HD_frame, width=5)
        self.HD_Entry.insert(0, 6)
        self.HD_Entry.pack(side="right",pady=5)
        
        self.MODQ_frame = tk.Frame(self.DMG_frame, bg="dim grey")
        self.MODQ_frame.pack(expand=True, fill=tk.Y,padx=5,pady=0)
        tk.Label(self.MODQ_frame, text="Enter Strength & Magical bonus: ").pack(side="left",pady=5)
        self.MOD_frame = tk.Frame(self.DMG_frame, bg="dim grey")
        self.MOD_frame.pack(expand=True, fill=tk.Y,padx=5,pady=0)
        self.STR_Entry = tk.Entry(self.MOD_frame, width=5)
        self.STR_Entry.insert(0, 4)
        self.STR_Entry.pack(side="left", padx=10, pady=5)
        self.MAGIC_Entry = tk.Entry(self.MOD_frame, width=5)
        self.MAGIC_Entry.insert(0, 1)
        self.MAGIC_Entry.pack(side="left", padx=10, pady=5)
        
        # now GWM, DF, R and weapon checkbox options
        self.checksQ_frame = tk.Frame(self.DMG_frame, bg="dim grey")
        self.checksQ_frame.pack(expand=True, fill=tk.Y, padx=5, pady=5)
        tk.Label(self.checksQ_frame, text="Check for Great Weapon Master, Divine Fury & Rage: ").pack(side="left",pady=5)
        self.checks_frame = tk.Frame(self.DMG_frame, bg="dim grey")
        self.checks_frame.pack(expand=True, fill=tk.Y, padx=5, pady=5)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        R_check = tk.Checkbutton(self.checks_frame, text='R',variable=self.var3, onvalue=1, offvalue=0)
        R_check.pack(side="left", padx=10, pady=5)
        DF_check = tk.Checkbutton(self.checks_frame, text='DF',variable=self.var2, onvalue=1, offvalue=0)
        DF_check.pack(side="left", padx=10, pady=5)
        GWM_check = tk.Checkbutton(self.checks_frame, text='GWM',variable=self.var1, onvalue=1, offvalue=0)
        GWM_check.pack(side="left", padx=10, pady=5)
        
        # Button info
        self.DMG_Button = tk.Button(self.DMG_frame, text="• Roll Damage •", command = self.roll_dmg ,font=("Helvetica", 24, "bold"),
        bg="dim grey",
        fg="white",
        padx=20,
        pady=10,
        relief=tk.RAISED,
        bd=3)
        self.DMG_Button.pack(side=tk.BOTTOM,padx=5,pady=5)
        
        
        
        #----------------------------------------------------------------------------------------
        
        # Background Proficiency Selector
        self.BACK_frame = tk.Frame(self.top_frame, bg="dim grey", padx=10, pady=20)
        self.BACK_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=5,pady=10)
        
        # Main Title Label
        self.BACK_title_label = tk.Label(
            self.BACK_frame ,
            text="🎲 Background Search 🎲",
            font=("Helvetica", 20, "bold"),
            bg="black",
            fg="white")
        self.BACK_title_label.pack(side=tk.TOP, pady=0)

        # Subtitle Label
        self.BACK_subtitle_label = tk.Label(
            self.BACK_frame,
            text="Input desired Proficiences below:",
            font=("Helvetica", 14),
            bg="black",
            fg="white")
        self.BACK_subtitle_label.pack(pady=0)
        
        # label 1
        self.prof_list_frame_1 = tk.Frame(self.BACK_frame, bg="dim grey")
        self.prof_list_frame_1.pack(side="top",padx=5,pady=5)
        # switch
        self.prof_choice_1 = ttk.Combobox(
        self.prof_list_frame_1 ,
            values=["Any", "Acrobatics","Animal Handling","Athletics","Deception","History","Insight",
                    "Intimidation","Investigation","Medicine","Nature","Perception","Performance","Persuasion",
                    "Religion","Sleight of Hand","Stealth","Survival"],
            state="readonly",
            width=15,
            font=("Helvetica", 20),background="dim grey")
        self.prof_choice_1.current(0)  # Default: "all Classes"
        self.prof_choice_1.pack(pady=20)
        
        # label 2
        self.prof_list_frame_2 = tk.Frame(self.BACK_frame, bg="dim grey")
        self.prof_list_frame_2.pack(side="top",padx=5,pady=5)
        # switch
        self.prof_choice_2 = ttk.Combobox(
        self.prof_list_frame_2 ,
            values=["Any", "Acrobatics","Animal Handling","Athletics","Deception","History","Insight",
                    "Intimidation","Investigation","Medicine","Nature","Perception","Performance","Persuasion",
                    "Religion","Sleight of Hand","Stealth","Survival"],
            state="readonly",
            width=15,
            font=("Helvetica", 20),background="dim grey")
        self.prof_choice_2.current(0)  # Default: "all Classes"
        self.prof_choice_2.pack(pady=20)

        # CC Button
        self.find_btn = tk.Button(
            self.BACK_frame,
            text="• Find Background(s) • ",
            command=self.find_BACK,
            font=("Helvetica", 24, "bold"),
            bg="dim grey",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            bd=3)
        self.find_btn.pack(side=tk.BOTTOM, padx=5,pady=10)
        
        #----------------------------------------------------------------
        
        
        
        # AS roller
        self.AS_frame = tk.Frame(self.top_frame, bg="dim grey", padx=10, pady=20)
        self.AS_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH,padx=5,pady=10)
        self.AS_title_label = tk.Label(
            self.AS_frame ,
            text="🎲 Ability Score Roller🎲",
            font=("Helvetica", 20, "bold"),
            bg="black",
            fg="white")
        self.AS_title_label.pack(side=tk.TOP, pady=0)
        
        self.A15_frame = tk.Frame(self.AS_frame, bg="dim grey")
        self.A15_frame.pack(expand=True, fill=tk.Y,padx=5,pady=0)
        tk.Label(self.A15_frame, text="Enter minimum no. rolls above 15: ").pack(side="left",padx=5,pady=5)
        self.A15_Entry = tk.Entry(self.A15_frame, width=5)
        self.A15_Entry.insert(0, 2)
        self.A15_Entry.pack(side="right",padx=5,pady=5)
        
        self.S10_frame = tk.Frame(self.AS_frame, bg="dim grey")
        self.S10_frame.pack(expand=True, fill=tk.Y,padx=5,pady=0)
        tk.Label(self.S10_frame, text="Enter minimum no. rolls below 10: ").pack(side="left",padx=5,pady=5)
        self.S10_Entry = tk.Entry(self.S10_frame, width=5)
        #self.S10_Entry.insert(0,0)
        self.S10_Entry.pack(side="right",padx=5,pady=5)
        
        self.MT_frame = tk.Frame(self.AS_frame, bg="dim grey")
        self.MT_frame.pack(expand=True, fill=tk.Y,padx=5,pady=0)
        tk.Label(self.MT_frame, text="Enter minimum sum total of Rolls: ").pack(side="left",padx=5,pady=5)
        self.MT_Entry = tk.Entry(self.MT_frame, width=5)
        self.MT_Entry.insert(0,75)
        self.MT_Entry.pack(side="right",padx=5,pady=5)
        
        self.Roll_Button = tk.Button(self.AS_frame, text="• Roll Ability Scores •", command = self.roll_AS, font=("Helvetica", 24, "bold"),
        bg="dim grey",
        fg="white",
        padx=0,
        pady=10,
        relief=tk.RAISED,
        bd=3)
        self.Roll_Button.pack(side=tk.BOTTOM,padx=5,pady=0)
        
        
        
        
        # CC
        self.CC_frame = tk.Frame(self.top_frame , bg="dim grey", padx=10, pady=20)
        self.CC_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH,padx=5,pady=10)
        
        # Main Title Label
        self.CC_title_label = tk.Label(
            self.CC_frame ,
            text="🎲 Random Character Creator 🎲",
            font=("Helvetica", 20, "bold"),
            bg="black",
            fg="white")
        self.CC_title_label.pack(side=tk.TOP, pady=0)

        # Subtitle Label
        self.CC_subtitle_label = tk.Label(
            self.CC_frame,
            text="Click below to generate a fully randomized D&D character!",
            font=("Helvetica", 14),
            bg="black",
            fg="white")
        self.CC_subtitle_label.pack(pady=0)
        
        # label
        self.class_list_frame = tk.Frame(self.CC_frame, bg="dim grey")
        self.class_list_frame.pack(side="top",padx=5,pady=5)
        # switch
        self.class_list_switch = ttk.Combobox(
        self.class_list_frame ,
            values=["All Subclasses", "Better Subclasses"],
            state="readonly",
            width=15,
            font=("Helvetica", 20),background="dim grey")
        self.class_list_switch.current(0)  # Default: "all Classes"
        self.class_list_switch.pack(pady=20)

        # CC Button
        self.generate_btn = tk.Button(
            self.CC_frame,
            text="• Generate Character • ",
            command=self.generate_character,
            font=("Helvetica", 24, "bold"),
            bg="dim grey",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            bd=3)
        self.generate_btn.pack(side=tk.BOTTOM, padx=5,pady=10)

        

        # Output Frame
        self.output_frame = tk.Frame(self.root, bg="dim grey")
        self.output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        tk.Label(self.AS_frame,background="dim grey").pack(expand =True, fill="both")
        tk.Label(self.output_frame,background="dim grey").pack(expand =True, fill="both")
        
        # Both functions
        self.all_frame = tk.Frame(self.output_frame , bg="dim grey")
        self.all_frame.pack(expand=True, fill=tk.BOTH,padx=5,side=tk.TOP)
        self.all_Button = tk.Button(self.output_frame , text="Roll for Random Character & Ability Scores", command = self.roll_both ,font=("Helvetica", 20, "bold"),
        bg="dim grey",
        fg="white",
        padx=20,
        pady=5,
        relief=tk.RAISED,
        bd=3)
        self.all_Button.pack(fill=tk.BOTH,padx=5,side=tk.TOP)

        # Output Text Area
        self.output_text = scrolledtext.ScrolledText(
            self.output_frame,
            wrap=tk.WORD,
            width=85,
            height=25,
            font=("Helvetica", 9),
            bg="white",
            fg="#2c3e50",
            padx=10,
            pady=10,
            relief=tk.SUNKEN,
            bd=3)
        self.output_text.pack(padx=10,pady=5)
        
        # Clear Button
        self.clear_btn = tk.Button(
            self.output_frame,
            text="! Clear Output !",
            command=self.clear_output,
            font=("Helvetica", 12),
            bg="dim grey",
            fg="white",
            padx=15,
            pady=5,
            relief=tk.RAISED,
            bd=2)
        self.clear_btn.pack(side=tk.BOTTOM, pady=10,padx=10)

        # Footer Label
        self.footer = tk.Label(
            self.root,
            text="Character Creator v1.0 | Uses CC() from CC_new.py",
            font=("Helvetica", 8),
            bg="#2c3e50",
            fg="#7f8c8d")
        self.footer.pack(side=tk.BOTTOM,pady=0)
        
        
        
        
        
    def generate_character(self):
        # Generate and display a random character
        try:
            if self.class_list_switch.get() == "All Subclasses":
                class_list = "all"
            else:
                class_list = "better"
            # Get the character string from CC()
            character_sheet = CC(class_list=class_list)
            
            # Clear previous output and display new character
            # self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, character_sheet)
            self.output_text.see(tk.END)  # Scroll to bottom
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate character:\n{str(e)}")


    def toggle_method(self):
        current = self.roll_AS2.get()
        self.use_3d6.set(not current)
        new_text = "Method: 3d6" if not current else "Method: 4d6-min"
        self.toggle_di_button.config(text=new_text)
    
    def roll_AS(self):
        try:
            above15 = int(self.A15_Entry.get()) if self.A15_Entry.get() else 0
            sub10 = int(self.S10_Entry.get()) if self.S10_Entry.get() else 0
            mintot = int(self.MT_Entry.get()) if self.MT_Entry.get() else 0

            
            rolls = AS(above15, sub10, mintot)
                
            # self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, rolls)
            self.output_text.see(tk.END)  # Scroll to bottom
        except ValueError:
            messagebox.showerror("Invalid input")
            
   
            
    def find_BACK(self):
        try:
            prof1 = self.prof_choice_1.get()
            prof2 = self.prof_choice_2.get()
            # Get the character string from CC()
            BACK_choices = present_BACK(prof1,prof2)
            
            # Clear previous output and display new character
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, str(BACK_choices))
            self.output_text.see(tk.END)  # Scroll to bottom
        except Exception as e:
            messagebox.showerror("Error", f"Failed to complete operation:\n{str(e)}")
    
        
            
            
            
    def roll_dmg(self):
        try:
            NoHD = int(self.NoHD_Entry.get()) if self.NoHD_Entry.get() else 0
            HD = int(self.HD_Entry.get()) if self.HD_Entry.get() else 0
            STR = int(self.STR_Entry.get()) if self.STR_Entry.get() else 0
            
            MAGIC = int(self.MAGIC_Entry.get()) if self.MAGIC_Entry.get() else 0
            GWM_tick = int(self.var1.get()) if self.var1.get() else 0
            DF_tick = int(self.var2.get()) if self.var2.get() else 0
            R_tick = int(self.var3.get()) if self.var3.get() else 0
            DMG_done = dmg(NoHD,HD,STR,MAGIC,GWM_tick, DF_tick, R_tick)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, DMG_done)
            self.output_text.see(tk.END)
            
            
            # Weapon
            
        except ValueError:
            messagebox.showerror("Invalid input")
            
        
    def roll_both(self):
        self.generate_character()
        self.roll_AS()
        


    def clear_output(self):
        """Clear the output text widget"""
        self.output_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CC_app(root)
    root.mainloop()