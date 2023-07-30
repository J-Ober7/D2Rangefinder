import tkinter as tk
from utilfunctions import *
from weapon_archetype import *

grid_pad_x = 10
grid_pad_y = 15

place_row_gap = 75

range_stat_value = 0

root = tk.Tk()

root.title("Destiny 2 Range Calculator")
root.geometry ('400x400')
root.grid_columnconfigure(0, minsize= 130)
root.grid_columnconfigure(1, minsize= 130)

# Range Stat Display Field
range_stat_display_text = tk.StringVar()
range_stat_display_text.set("Range Stat: " + str(range_stat_value))
range_stat_label = tk.Label(root, textvariable=range_stat_display_text)

# adding Entry Field
range_input_text = tk.Entry(root, width=10)

range_input_validiation = root.register(rangeCallback)
range_input_text.config(validate="key", validatecommand=(range_input_validiation, '%P'))

def setRangeStat():
    entry = range_input_text.get()
    if(entry == ''):
        return
    global range_stat_value
    range_stat_value = clamp(int(entry), 0, 100)
    s = "Range Stat: " + str(range_stat_value)
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



selected_archetype = tk.StringVar(root)
selected_archetype.set("Select an Archetype")

archetype_menu = tk.OptionMenu(root, selected_archetype, *WEAPON_ARCHETYPES)

# Archetype Display Field
selected_archetype_display_text = tk.StringVar()
selected_archetype_display_text.set("Archetype Unselected")
selected_archetype_label = tk.Label(root, textvariable=selected_archetype_display_text)

# Damage Dropoff Display Field
damage_dropoff_display_text = tk.StringVar()
damage_dropoff_display_text.set("Damage Dropoff: ")
damage_dropoff_label = tk.Label(root, textvariable=damage_dropoff_display_text)

def calculateRange():
    setRangeStat()
    selected = selected_archetype.get()
    selected_archetype_display_text.set(selected)
    damage_dropoff_display_text.set("Damage Dropoff: " + str(archetype_dictionary[selected].calculateRange(range_stat_value)) + " Meters")



calculate_button = tk.Button(root, text = "Calculate Range", command= calculateRange)






#Widget Placement 
range_stat_label.grid(column=0, row=0, padx=0, pady=grid_pad_y,)
range_input_text.grid(column=1, row=0, padx=5, pady=grid_pad_y)
range_set_button.grid(column=2, row=0, padx=0, pady=grid_pad_y)
archetype_label.grid(column=0, row=1, padx=0, pady=grid_pad_y)
archetype_menu.grid(column=1, row=1, padx=20, pady=grid_pad_y, columnspan=2, sticky= tk.W)
selected_archetype_label.grid(column=0, row=3, padx=0, pady=grid_pad_y,)
damage_dropoff_label.grid(column=0, row=4, padx=0, pady=grid_pad_y, columnspan=2, sticky= tk.W)
calculate_button.grid(column=1, row=3, padx=20, pady=0, )



root.mainloop()