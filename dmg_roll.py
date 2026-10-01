#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def dmg(NoHD,HD,STR,MAGIC,GWM,DF,R):
    
    wlist = []
    list_print = ""   
    dmg_mod = STR + MAGIC
    list_print += f"Damage Mod: {dmg_mod}"
    
    if R == 1:
        rage_damage = 2
        list_print += f"\nRage Damage: {rage_damage}"
    else:
        rage_damage = 0
        
    if GWM == 1:
        GWM_damage = 10
        list_print += f"\nGreat Weapon Master Damage: {GWM_damage}"
    else:
        GWM_damage = 0
        
    list_print += "\n" 
    flat_dmg = dmg_mod + rage_damage + GWM_damage
    list_print += f"\nFLAT DAMAGE BONUS = {flat_dmg}"
    list_print += "\n\n"
        
    for r in range(0,NoHD):
         wlist.append(random.randint(1, HD))
    weapon_damage = sum(wlist)
    list_print += f"\nWeapon Damage: {wlist} = {weapon_damage}"
    
        
    if DF == 1:
        df_damage = sum(random.randint(1, 6) for _ in range(1)) + 3
        list_print += f"\nDivine Fury Damage [roll + 3]:  {df_damage}"
    else:
        df_damage = 0
    
    list_print += "\n" 
    Roll_dmg = weapon_damage + df_damage
    list_print += f"\nROLL DAMAGE = {Roll_dmg}"
    list_print += "\n\n"
    
    
    tot_damage = flat_dmg + Roll_dmg
    tot_print = f"{list_print}\n\nTOTAL DAMAGE: {tot_damage}\n\n"
    return tot_print
        
    

    
