import tkinter as tk
import logging, sys
import bisect
import math
from tkinter import ttk
from utilfunctions import *
from weapon_archetype import *

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class D2Rangefinder:
    def __init__(self) -> None:
        self.range_stat_value = 0
        self.RESILIENCE_VALUES = [185, 186, 187, 188, 189, 190, 192, 194, 196, 198, 200]
    
    def calcTTK(self, weapon):
        body_dam = weapon.body_damage
        prec_dam = weapon.precision_damage
        damage_diff = prec_dam - body_dam

        resilience_crit_body_ratios = []
        
        health_count = 0
        crit_count = 0
        body_count = 0
        step = 0
        tier_reached = 0
        while (health_count < self.RESILIENCE_VALUES[0]):
            if (step == 0):
                health_count += body_dam
                body_count += 1
                step = 1
            elif (step == 1):
                health_count += damage_diff
                body_count -= 1
                crit_count += 1
                step = 0
             

        # starting at tiers_reached, determine how many tiers the next body or crit increment will cover,
        #     and then increment to tiers_reached to that tier + 1. Use bisect_right-1 for binary search on the RESILIENCE_VALUES. 
        #     Store each result in a Tuple(tier_start, tier_end, crit, body)
        tier_end = bisect.bisect_right(self.RESILIENCE_VALUES, health_count, lo=tier_reached) - 1
        resilience_crit_body_ratios.append((tier_reached, tier_end, crit_count, body_count))
        tier_reached=tier_end + 1
        logging.debug(health_count)
        while (tier_reached < 11):
            if (step == 0):
                health_count += body_dam
                body_count += 1
                tier_end = bisect.bisect(self.RESILIENCE_VALUES, health_count, lo=tier_reached) - 1
                if(tier_end >= tier_reached):
                    resilience_crit_body_ratios.append((tier_reached, tier_end, crit_count, body_count))
                    tier_reached=tier_end + 1
                step = 1
            elif (step == 1):
                health_count += damage_diff
                body_count -= 1
                crit_count += 1
                tier_end = bisect.bisect(self.RESILIENCE_VALUES, health_count, lo=tier_reached) - 1
                if(tier_end >= tier_reached):
                    resilience_crit_body_ratios.append((tier_reached, tier_end, crit_count, body_count))
                    tier_reached=tier_end + 1
                step = 0


        return resilience_crit_body_ratios

    def run(self) -> None:
        grid_pad_x = 10
        grid_pad_y = 15

        place_row_gap = 75
        
        root = tk.Tk()  
        root.title("Destiny 2 Rangefinder")
        root.geometry ('450x450')
        root.grid_columnconfigure(0, minsize= 130)
        root.grid_columnconfigure(1, minsize= 130)
        

        # Range Stat Display Field
        range_stat_display_text = tk.StringVar()
        range_stat_display_text.set("Range Stat: " + str(self.range_stat_value))
        range_stat_label = tk.Label(root, textvariable=range_stat_display_text)

        # adding Entry Field
        range_input_text = tk.Entry(root, width=10)

        range_input_validiation = root.register(rangeCallback)
        range_input_text.config(validate="key", validatecommand=(range_input_validiation, '%P'))


        def setRangeStat():
            entry = range_input_text.get()
            if(entry == ''):
                return
            self.range_stat_value = clamp(int(entry), 0, 100)
            s = "Range Stat: " + str(self.range_stat_value)
            range_stat_display_text.set(s)
            range_input_text.delete(0, tk.END)

        range_set_button = tk.Button(root, text = "Set Range", command= setRangeStat)

        #Archetype Display Text
        archetype_display_text = tk.StringVar()
        archetype_display_text.set("Archetype: ")
        archetype_label = tk.Label(root, textvariable=archetype_display_text)

        #Archetype Dropdown Text 
        WEAPON_ARCHETYPES = [
            "Auto Rifle",
            "SMG",
            "Hand Cannon",
            "Pulse Rifle",
            "Scout Rifle",
            "Sidearm"
        ]

        archetype_dictionary = {
            "Auto Rifle": AutoRifle(),
            "SMG": SMG(),
            "Hand Cannon": HandCannon(),
            "Pulse Rifle": PulseRifle(),
            "Scout Rifle": ScoutRifle(),
            "Sidearm": Sidearm()
        }

        autorifle_archetype_dictionary = {
            'Adapative (600 RPM)': Autorifle_Adapative(),
            'Precision (450 RPM)': Autorifle_Precision(),
            'Rapid-Fire (720 RPM)': Autorifle_RapidFire(),
            'High-Impact (360 RPM)': Autorifle_HighImpact()
        }

        handcannon_archetype_dictionary = {
            'Adapative (140 RPM)': HandCannon_Adapative(),
            'Lightweight (140 RPM)': HandCannon_Adapative(),
            'Precision (180 RPM)': HandCannon_Precision(),
            'Aggressive (120 RPM)': HandCannon_Aggressive(),
        }

        smg_archetype_dictionary = {
            'Adapative (900 RPM)': SMG_Adapative(),
            'Lightweight (900 RPM)': SMG_Lightweight(),
            'Precision (600 RPM)': SMG_Precision(),
            'Aggressive (750 RPM)': SMG_Aggressive()
        }
        pulserifle_archetype_dictionary = {
            'Adapative (390 RPM)': PulseRifle_Adaptive(),
            'Lightweight (450 RPM)': PulseRifle_Lightweight(),
            'Rapid-Fire (540 RPM)': PulseRifle_RapidFire(),
            'High-Impact (340 RPM)': PulseRifle_HighImpact(),
            'Aggressive (450 RPM)': PulseRifle_Aggressive()
        }

        scoutrifle_archetype_dictionary = {
            'Lightweight (200 RPM)': ScoutRifle_Lightweight(),
            'Precision (180 RPM)': ScoutRifle_Precision(),
            'Rapid-Fire (260 RPM)': ScoutRifle_RapidFire(),
            'High-Impact (150 RPM)': ScoutRifle_HighImpact(),
            'Aggressive (120 RPM)': ScoutRifle_Aggressive()
        }

        sidearm_archetype_dictionary = {
            'Omolon Adapative Frame (491)': Sidearm_OmolonAdapative(),
            'Adapative Frame (300)': Sidearm_Adaptive(),
            'Precision (260 RPM)': Sidearm_Precision(),
            'Lightweight (360 RPM)': Sidearm_Lightweight(),
            'Rapid-Fire (450 RPM)': Sidearm_RapidFire(),
            'Aggressive (325 RPM)': Sidearm_Aggressive()
        }

        sub_archetype_dictionaries = {
            "Auto Rifle": autorifle_archetype_dictionary,
            "SMG": smg_archetype_dictionary,
            "Hand Cannon": handcannon_archetype_dictionary,
            "Pulse Rifle": pulserifle_archetype_dictionary,
            "Scout Rifle": scoutrifle_archetype_dictionary,
            "Sidearm": sidearm_archetype_dictionary
        }

        selected_archetype = tk.StringVar(root)
        selected_archetype.set("Select an Archetype")

        def pickSubArchetype(e):
            logging.debug(archetype_menu_new.get())
            archetype = archetype_menu_new.get()
            selected_archetype.set(archetype)
            sub_archetype_menu.config(value= archetype_dictionary[archetype].subfamilies)
            sub_archetype_menu.current(0)
            
        archetype_menu_new = ttk.Combobox(root, width=15, values=(WEAPON_ARCHETYPES))
        archetype_menu_new.bind("<<ComboboxSelected>>", pickSubArchetype)
        sub_archetype_menu = ttk.Combobox(root, width=20, values=[""])


        # Archetype Display Field
        selected_archetype_display_text = tk.StringVar()
        selected_archetype_display_text.set("Archetype Unselected")
        selected_archetype_label = tk.Label(root, textvariable=selected_archetype_display_text)

        # Damage Dropoff Display Field
        damage_dropoff_display_text = tk.StringVar()
        damage_dropoff_display_text.set("Damage Dropoff: ")
        damage_dropoff_label = tk.Label(root, textvariable=damage_dropoff_display_text)


        # TTK Display Field
        TTK_display_text = tk.StringVar()
        TTK_display_text.set("Tier 0: \nTier 1: \nTier 2: \nTier 3: \nTier 4: \nTier 5: \nTier 6: \nTier 7: \nTier 8: \nTier 9: \nTier 10:")
        TTK_label = tk.Label(root, textvariable=TTK_display_text)

        def calculateRange():
            setRangeStat()
            selected = selected_archetype.get()
            selected_archetype_display_text.set(selected)
            weapon = sub_archetype_dictionaries[selected][sub_archetype_menu.get()]
            if(weapon != None):
                damage_dropoff_display_text.set("Damage Dropoff: " + str(weapon.calculateRange(self.range_stat_value)) + " Meters")
                ttk_info = self.calcTTK(weapon)
                ttk_string = "Optimal TTK\n"
                for tuple in ttk_info:
                    start = tuple[0]
                    end = tuple[1]
                    crits = tuple[2]
                    bodies = tuple[3]
                    if(start == end):
                        ttk_string += ("Tier " + str(start) + ": " + str(crits) + " Criticals & " + str(bodies) + " Bodies \n")
                    else: 
                        ttk_string += "Tiers " + str(start) + " to " + str(end)+ ": " + str(crits) + " Criticals & " + str(bodies) + " Bodies \n"
                TTK_display_text.set(ttk_string)




        calculate_button = tk.Button(root, text = "Calculate Range", command= calculateRange)

        #Widget Placement 
        range_stat_label.grid(column=0, row=0, padx=0, pady=grid_pad_y,)
        range_input_text.grid(column=1, row=0, padx=5, pady=grid_pad_y)
        range_set_button.grid(column=2, row=0, padx=0, pady=grid_pad_y)
        archetype_label.grid(column=0, row=1, padx=0, pady=grid_pad_y)
        archetype_menu_new.grid(column=1, row=1, padx=20, pady=grid_pad_y, columnspan=2, sticky= tk.W)
        sub_archetype_menu.grid(column=2, row=1, padx=20, pady=grid_pad_y, columnspan=2, sticky= tk.W)
        selected_archetype_label.grid(column=0, row=3, padx=0, pady=grid_pad_y,)
        damage_dropoff_label.grid(column=0, row=4, padx=20, pady=grid_pad_y, columnspan=2, sticky= tk.W)
        calculate_button.grid(column=1, row=3, padx=20, pady=0, )
        TTK_label.grid(column=0, row=5, padx=20, pady=grid_pad_y, columnspan=4, sticky= tk.W)

        #Run
        root.mainloop()
        return
