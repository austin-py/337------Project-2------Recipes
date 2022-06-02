from bs4 import BeautifulSoup
kitchen_utensils_list = '''<ul>
<li>Apron</li>
<li>Butter knife</li>
<li>Butter dish</li>
<li>Breadbox</li>
<li>Bread basket</li>
<li>Bowl</li>
<li>Bottle opener</li>
<li>Bottle</li>
<li>Blender</li>
<li>Bin</li>
<li>Baking tray</li>
<li>Cutting board</li>
<li>Cutlery</li>
<li>Cup (mug)</li>
<li>Cup</li>
<li>Corkscrew</li>
<li>Cookware</li>
<li>Cooker</li>
<li>Colander</li>
<li>Cleaver</li>
<li>Chopsticks</li>
<li>Chopping board</li>
<li>Casserole dish</li>
<li>Can opener</li>
<li>Cake slicer</li>
<li>Dishwasher</li>
<li>Dish rack</li>
<li>Deep fryer</li>
<li>Egg slicer</li>
<li>Funnel</li>
<li>Frying pan (stainless steel or nonstick)</li>
<li>Frying pan</li>
<li>Fork</li>
<li>Grater</li>
<li>Glass</li>
<li>Gas stove</li>
<li>Garlic crusher</li>
<li>Hot pot</li>
<li>Juicer</li>
<li>Jug</li>
<li>Jar</li>
<li>Knife</li>
<li>Kitchen towel</li>
<li>Scissors</li>
<li>Kitchen Shears</li>
<li>Kitchen paper</li>
<li>Kettle</li>
<li>Butter knife</li>
<li>Paring knife</li>
<li>Steak knife</li>
<li>Ladle</li>
<li>Lemon squeezer</li>
<li>Mortar</li>
<li>Mixing bowl</li>
<li>Mixer</li>
<li>Microwave oven</li>
<li>Mesh skimmer</li>
<li>Meat mallet</li>
<li>Measuring spoons</li>
<li>Measuring cup</li>
<li>Matchbox</li>
<li>Pressure cooker</li>
<li>Potato peeler</li>
<li>Potato masher</li>
<li>Plate</li>
<li>Pizza cutter</li>
<li>Pitcher (or jug)</li>
<li>Pie plate</li>
<li>Pestle</li>
<li>Perforated spoon</li>
<li>Peppermill</li>
<li>Peeler</li>
<li>Pan</li>
<li>Oven gloves</li>
<li>Oven</li>
<li>Napkin</li>
<li>Refrigerator</li>
<li>Regular spoon</li>
<li>Rolling pin</li>
<li>Strainer</li>
<li>Steak hammer</li>
<li>Spoon</li>
<li>Spice container</li>
<li>Spice box</li>
<li>Spatula</li>
<li>Slotted spoon</li>
<li>Sieve</li>
<li>Serving bowl</li>
<li>Saucepan</li>
<li>Salad spinner</li>
<li>Tureen (or bowl)</li>
<li>Tray</li>
<li>Tongs</li>
<li>Toaster</li>
<li>Timer</li>
<li>Thermos</li>
<li>Teaspoon</li>
<li>Teapot</li>
<li>Wooden spoon</li>
<li>Wok</li>
<li>Whisk</li>
<li>Washbasin</li>
</ul>'''

kitchenware_list = '''
<ul><li><a href="/wiki/Baking_dish" class="mw-redirect" title="Baking dish">Baking dish</a></li>
<li><a href="/wiki/Baking_tray" class="mw-redirect" title="Baking tray">Baking tray</a></li>
<li><a href="/wiki/Cake_pan" class="mw-redirect" title="Cake pan">Cake pan</a></li>
<li><a href="/wiki/Can_opener" title="Can opener">Can opener</a></li>
<li><a href="/wiki/Chopping_board" class="mw-redirect" title="Chopping board">Chopping board</a></li>
<li><a href="/wiki/Coffee_press" class="mw-redirect" title="Coffee press">Coffee press</a></li>
<li><a href="/wiki/Colander" title="Colander">Colander</a></li>
<li><a href="/w/index.php?title=Cooling_rack&amp;action=edit&amp;redlink=1" class="new" title="Cooling rack (page does not exist)">Cooling rack</a></li>
<li><a href="/wiki/Corkscrew" title="Corkscrew">Corkscrew</a></li>
<li><a href="/wiki/Cutlery" title="Cutlery">Cutlery</a></li>
<li><a href="/wiki/Dinnerware" class="mw-redirect" title="Dinnerware">Dinnerware</a></li>
<li><a href="/wiki/Mixer_(cooking)" class="mw-redirect" title="Mixer (cooking)">Eggbeater</a></li>
<li><a href="/wiki/Egg_slicer" title="Egg slicer">Egg slicer</a></li>
<li><a href="/wiki/Electric_mixer" class="mw-redirect" title="Electric mixer">Electric mixer</a></li>
<li><a href="/wiki/Fork" title="Fork">Fork</a></li>
<li><a href="/wiki/Frying_pan" title="Frying pan">Frying pan</a></li>
<li><a href="/wiki/Garlic_press" title="Garlic press">Garlic press</a></li>
<li><a href="/wiki/Grater" title="Grater">Grater</a></li>
<li><a href="/wiki/Glassware" class="mw-redirect" title="Glassware">Glassware</a></li>
<li><a href="/wiki/Griddle" title="Griddle">Grill pan</a></li>
<li><a href="/wiki/Kitchen_scissors" class="mw-redirect" title="Kitchen scissors">Kitchen scissors</a></li>
<li><a href="/wiki/Knife" title="Knife">Knives</a></li>
<li><a href="/wiki/Mandolin_(cooking)" class="mw-redirect" title="Mandolin (cooking)">Mandolin</a></li>
<li><a href="/wiki/Measuring_cup" title="Measuring cup">Measuring cups and spoons</a></li>
<li><a href="/wiki/Measuring_spoon" title="Measuring spoon">Measuring spoon</a></li>
<li><a href="/wiki/Meat_slicer" title="Meat slicer">Meat slicer</a></li>
<li><a href="/wiki/Bowl" title="Bowl">Mixing bowls</a></li>
<li><a href="/wiki/Muffin_tin" title="Muffin tin">Muffin tin</a></li>
<li><a href="/wiki/Pressure_cooker" class="mw-redirect" title="Pressure cooker">Pressure cooker</a></li>
<li><a href="/w/index.php?title=Pasta_server&amp;action=edit&amp;redlink=1" class="new" title="Pasta server (page does not exist)">Pasta server</a></li>
<li><a href="/wiki/Peeler" title="Peeler">Peeler</a></li>
<li><a href="/wiki/Pepper_mill" class="mw-redirect" title="Pepper mill">Pepper mill</a></li>
<li><a href="/w/index.php?title=Pie_dish&amp;action=edit&amp;redlink=1" class="new" title="Pie dish (page does not exist)">Pie dish</a></li>
<li><a href="/wiki/Pizza_stone" class="mw-redirect" title="Pizza stone">Pizza stone</a></li>
<li><a href="/wiki/Plate_(dishware)" title="Plate (dishware)">Plates</a></li>
<li><a href="/wiki/Potato_masher" title="Potato masher">Potato masher</a></li>
<li><a href="/wiki/Potato_ricer" title="Potato ricer">Potato ricer</a></li>
<li><a href="/wiki/Rolling_pin" title="Rolling pin">Rolling pin</a></li>
<li><a href="/wiki/Saucepan" class="mw-redirect" title="Saucepan">Saucepan</a></li>
<li><a href="/w/index.php?title=Serving_fork&amp;action=edit&amp;redlink=1" class="new" title="Serving fork (page does not exist)">Serving fork</a></li>
<li><a href="/wiki/Serving_spoon" class="mw-redirect" title="Serving spoon">Serving spoon</a></li>
<li><a href="/wiki/Sheet_pan" title="Sheet pan">Sheet pan</a></li>
<li><a href="/wiki/Skillet" class="mw-redirect" title="Skillet">Skillet</a></li>
<li><a href="/wiki/Slotted_spoon" title="Slotted spoon">Slotted spoon</a></li>
<li><a href="/wiki/Soup_spoon" title="Soup spoon">Soup spoon</a></li>
<li><a href="/wiki/Spatula" title="Spatula">Spatula</a></li>
<li><a href="/wiki/Spiral_vegetable_slicer" title="Spiral vegetable slicer">Spiral vegetable slicer</a></li>
<li><a href="/wiki/Spoon" title="Spoon">Spoon</a></li>
<li><a href="/wiki/Stock_pot" title="Stock pot">Stock pot</a></li>
<li><a href="/wiki/Food_steamer" title="Food steamer">Steamers</a></li>
<li><a href="/wiki/Strainer" class="mw-redirect" title="Strainer">Strainer</a></li>
<li><a href="/wiki/Timer" title="Timer">Timer</a></li>
<li><a href="/wiki/Tomato_slicer" title="Tomato slicer">Tomato slicer</a></li>
<li><a href="/wiki/Tongs" title="Tongs">Tongs</a></li>
<li><a href="/wiki/Tray" title="Tray">Tray</a></li>
<li><a href="/wiki/Whisk" title="Whisk">Whisk</a></li>
<li><a href="/wiki/Wok" title="Wok">Wok</a></li>
<li><a href="/wiki/Wooden_spoon" title="Wooden spoon">Wooden spoon</a></li></ul>
'''

def get_kitchen_utensils_list():
    soup = BeautifulSoup(kitchen_utensils_list, 'html.parser')
    list_html = soup.find_all('li')
    list = []
    for li in list_html:
        list.append(li.text)
    #list.append('skillet')
    return list

def get_kitchenware_list():
    soup = BeautifulSoup(kitchenware_list, 'html.parser')
    list_html = soup.find_all('li')
    list = []
    for li in list_html:
        list.append(li.text)
    return list

#Combine all lists to one
def get_tool_list():
    tool_list = []
    tool_list.extend(get_kitchen_utensils_list())
    tool_list.extend(get_kitchenware_list())
    a = (map(lambda x: x.lower(), tool_list))
    #Conver elements to lower case
    tool_list = list(a)
    return tool_list

if __name__=='__main__':
    print(get_tool_list())