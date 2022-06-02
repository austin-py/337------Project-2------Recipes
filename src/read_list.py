from bs4 import BeautifulSoup
kichen_utensils_list = '''<ul>
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

def get_kichen_utensils_list():
    soup = BeautifulSoup(kichen_utensils_list, 'html.parser')
    list_html = soup.find_all('li')
    list = []
    for li in list_html:
        list.append(li.text)
    return list