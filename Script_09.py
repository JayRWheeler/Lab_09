from tkinter import *
from tkinter import ttk
from poke_doki_api import get_pokemon_info
from tkinter import messagebox

# Create the window
root = Tk()
root.title("Pokedex")
root.resizable(False, False)

# TODO: Additional window configuration
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2)

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, padx=15, pady=15)

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=15, pady=15)

lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0, padx=5)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, pady=10)

def handle_get_info():
    # Get the Pokemon name from Info
    poke_name = ent_name.get()
    if len(poke_name) == 0:
        return

    # Get the Poke Info from the PokeAPI
    poke_info = get_pokemon_info(poke_name)
    if poke_info is None:
        err_msg = f'Unable to fetch info for {poke_name.capitalize()} from the Pokedex.'
        messagebox.showerror(title='Error', message=err_msg, icon='error')

    lbl_height_val['text'] = f"{poke_info['height']} dm"
    lbl_weight_val['text'] =f"{poke_info['weight']} hg"
    types_list = [t['type']['name'] for t in poke_info['types']]
    types = ', '.join(types_list).title()
    lbl_type_val['text'] = types

    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_atk['value'] = poke_info['stats'][1]['base_stat']
    bar_dfn['value'] = poke_info['stats'][2]['base_stat']
    bar_spc_atk['value'] = poke_info['stats'][3]['base_stat']
    bar_spc_dfn['value'] = poke_info['stats'][4]['base_stat']
    bar_spd['value'] = poke_info['stats'][5]['base_stat']

    return

btn_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_info.grid(padx=5, pady=10, row=0, column=2)


# Populate widget in the Info Frame
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx=2, pady=2, sticky=W)

lbl_height_val = ttk.Label(frm_btm_left, text='TBD')
lbl_height_val.grid(row=0, column=1, padx=2, pady=2, sticky=W)

lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, padx=2, pady=2, sticky=W)

lbl_weight_val = ttk.Label(frm_btm_left, text='TBD')
lbl_weight_val.grid(row=1, column=1, padx=2, pady=2, sticky=W)

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, padx=2, pady=2, sticky=E)

lbl_type_val = ttk.Label(frm_btm_left, text='TBD')
lbl_type_val.grid(row=2, column=1,padx=2, pady=2, sticky=W)

# TODO: Add widgets to window
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, sticky=E)

bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0, column=1)

lbl_atk = ttk.Label(frm_btm_right, text='ATK:')
lbl_atk.grid(row=1, column=0, sticky=E)

bar_atk = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_atk.grid(row=1, column=1)

lbl_dfn = ttk.Label(frm_btm_right, text='DFN:')
lbl_dfn.grid(row=2, column=0, sticky=E)

bar_dfn = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_dfn.grid(row=2, column=1)

lbl_spc_atk = ttk.Label(frm_btm_right, text='SPC-ATK:')
lbl_spc_atk.grid(row=3, column=0, sticky=E)

bar_spc_atk = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spc_atk.grid(row=3, column=1)

lbl_spc_dfn = ttk.Label(frm_btm_right, text='SPC-DFN:')
lbl_spc_dfn.grid(row=4, column=0, sticky=E)

bar_spc_dfn = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spc_dfn.grid(row=4, column=1)

lbl_spd = ttk.Label(frm_btm_right, text='SPD:')
lbl_spd.grid(row=5, column=0, sticky=E)

bar_spd = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spd.grid(row=5, column=1)

# Loop until window is closed
root.mainloop()