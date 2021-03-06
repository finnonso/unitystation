List_of_plants = []
class ambrosia():
	name = 'ambrosia'
	plantname = 'Ambrosia Vulgaris'
	Description = "These seeds grow into common ambrosia, a plant grown by and from medicine."
	icon_state = 'seed-ambrosiavulgaris'
	lifespan = 60
	endurance = 25
	production = 6
	plant_yield = 6
	potency = 5
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'ambrosia-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["ambrosia_deus"]
	reagents_add = {'space_drugs':0.15, 'bicaridine':0.1, 'kelotane':0.1, 'vitamin':0.04, 'nutriment':0.05, 'toxin':0.1}
	species = 'ambrosiavulgaris'

List_of_plants.append(ambrosia)

class ambrosia_deus():
	name = 'ambrosia_deus'
	plantname = 'Ambrosia Deus'
	Description = "These seeds grow into ambrosia deus. Could it be the food of the gods..?"
	icon_state = 'seed-ambrosiadeus'
	lifespan = 60
	endurance = 25
	production = 6
	plant_yield = 6
	potency = 5
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'ambrosia-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["ambrosia_gaia"]
	reagents_add = {'omnizine':0.15, 'synaptizine':0.15, 'space_drugs':0.1, 'vitamin':0.04, 'nutriment':0.05}
	species = 'ambrosiadeus'

List_of_plants.append(ambrosia_deus)

class ambrosia_gaia():
	name = 'ambrosia_gaia'
	plantname = 'Ambrosia Gaia'
	Description = "These seeds grow into ambrosia gaia, filled with infinite potential."
	icon_state = 'seed-ambrosia_gaia'
	lifespan = 60
	endurance = 25
	production = 6
	plant_yield = 6
	potency = 5
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'ambrosia-dead'
	genes = []
	mutates_into = ["ambrosia_deus"]
	reagents_add = {'earthsblood':0.05, 'nutriment':0.06, 'vitamin':0.05}
	species = 'ambrosia_gaia'

List_of_plants.append(ambrosia_gaia)

class apple():
	name = 'apple'
	plantname = 'Apple Tree'
	Description = "These seeds grow into apple trees."
	icon_state = 'seed-apple'
	lifespan = 55
	endurance = 35
	production = 6
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'apple-grow'
	dead_Sprite = 'apple-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["apple_gold"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1}
	species = 'apple'

List_of_plants.append(apple)

class apple_poisoned():
	name = 'apple_poisoned'
	plantname = 'Apple Tree'
	Description = "These seeds grow into apple trees."
	icon_state = 'seed-apple'
	lifespan = 55
	endurance = 35
	production = 6
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'apple-grow'
	dead_Sprite = 'apple-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'zombiepowder':0.5, 'vitamin':0.04, 'nutriment':0.1}

List_of_plants.append(apple_poisoned)

class apple_gold():
	name = 'apple_gold'
	plantname = 'Golden Apple Tree'
	Description = "These seeds grow into golden apple trees. Good thing there are no firebirds in space."
	icon_state = 'seed-goldapple'
	lifespan = 55
	endurance = 35
	production = 10
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'apple-grow'
	dead_Sprite = 'apple-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'gold':0.2, 'vitamin':0.04, 'nutriment':0.1}
	species = 'goldapple'

List_of_plants.append(apple_gold)

class banana():
	name = 'banana'
	plantname = 'Banana Tree'
	Description = "They're seeds that grow into banana trees. When grown, keep away from clown."
	icon_state = 'seed-banana'
	lifespan = 50
	endurance = 30
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	dead_Sprite = 'banana-dead'
	genes = ["Slippery Skin", "Perennial_Growth"]
	mutates_into = ["banana_mime","banana_bluespace"]
	reagents_add = {'banana':0.1, 'potassium':0.1, 'vitamin':0.04, 'nutriment':0.02}
	species = 'banana'

List_of_plants.append(banana)

class banana_mime():
	name = 'banana_mime'
	plantname = 'Mimana Tree'
	Description = "They're seeds that grow into mimana trees. When grown, keep away from mime."
	icon_state = 'seed-mimana'
	lifespan = 50
	endurance = 30
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	dead_Sprite = 'banana-dead'
	genes = ["Slippery Skin", "Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'nothing':0.1, 'mutetoxin':0.1, 'nutriment':0.02}
	species = 'mimana'

List_of_plants.append(banana_mime)

class banana_bluespace():
	name = 'banana_bluespace'
	plantname = 'Bluespace Banana Tree'
	Description = "They're seeds that grow into bluespace banana trees. When grown, keep away from bluespace clown."
	icon_state = 'seed-banana-blue'
	lifespan = 50
	endurance = 30
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'banana-grow'
	dead_Sprite = 'banana-dead'
	genes = ["Slippery Skin", "Bluespace Activity", "Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'bluespace':0.2, 'banana':0.1, 'vitamin':0.04, 'nutriment':0.02}
	species = 'bluespacebanana'

List_of_plants.append(banana_bluespace)

class soya():
	name = 'soya'
	plantname = 'Soybean Plants'
	Description = "These seeds grow into soybean plants."
	icon_state = 'seed-soybean'
	lifespan = 25
	endurance = 15
	production = 4
	plant_yield = 3
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'soybean-grow'
	dead_Sprite = 'soybean-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["soya_koi"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.05}
	species = 'soybean'

List_of_plants.append(soya)

class soya_koi():
	name = 'soya_koi'
	plantname = 'Koibean Plants'
	Description = "These seeds grow into koibean plants."
	icon_state = 'seed-koibean'
	lifespan = 25
	endurance = 15
	production = 4
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'soybean-grow'
	dead_Sprite = 'soybean-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'carpotoxin':0.1, 'vitamin':0.04, 'nutriment':0.05}
	species = 'koibean'

List_of_plants.append(soya_koi)

class berry():
	name = 'berry'
	plantname = 'Berry Bush'
	Description = "These seeds grow into berry bushes."
	icon_state = 'seed-berry'
	lifespan = 20
	endurance = 15
	production = 5
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'berry-grow' 
	dead_Sprite = 'berry-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = ["berry_glow","berry_poison"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1}
	species = 'berry'

List_of_plants.append(berry)

class berry_poison():
	name = 'berry_poison'
	plantname = 'Poison-Berry Bush'
	Description = "These seeds grow into poison-berry bushes."
	icon_state = 'seed-poisonberry'
	lifespan = 20
	endurance = 15
	production = 5
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'berry-grow' 
	dead_Sprite = 'berry-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = ["berry_death"]
	reagents_add = {'cyanide':0.15, 'tirizene':0.2, 'vitamin':0.04, 'nutriment':0.1}
	species = 'poisonberry'

List_of_plants.append(berry_poison)

class berry_death():
	name = 'berry_death'
	plantname = 'Death Berry Bush'
	Description = "These seeds grow into death berries."
	icon_state = 'seed-deathberry'
	lifespan = 30
	endurance = 15
	production = 5
	plant_yield = 2
	potency = 50
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'berry-grow' 
	dead_Sprite = 'berry-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'coniine':0.08, 'tirizene':0.1, 'vitamin':0.04, 'nutriment':0.1}
	species = 'deathberry'

List_of_plants.append(berry_death)

class berry_glow():
	name = 'berry_glow'
	plantname = 'Glow-Berry Bush'
	Description = "These seeds grow into glow-berry bushes."
	icon_state = 'seed-glowberry'
	lifespan = 30
	endurance = 25
	production = 5
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'berry-grow' 
	dead_Sprite = 'berry-dead' 
	genes = ["Strong Bioluminescence" , "Separated Chemicals", "Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'uranium':0.25, 'iodine':0.2, 'vitamin':0.04, 'nutriment':0.1}
	species = 'glowberry'

List_of_plants.append(berry_glow)

class cherry():
	name = 'cherry'
	plantname = 'Cherry Tree'
	Description = "Careful not to crack a tooth on one... That'd be the pits."
	icon_state = 'seed-cherry'
	lifespan = 35
	endurance = 35
	production = 5
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'cherry-grow'
	dead_Sprite = 'cherry-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["cherry_blue"]
	reagents_add = {'nutriment':0.07, 'sugar':0.07}
	species = 'cherry'

List_of_plants.append(cherry)

class cherry_blue():
	name = 'cherry_blue'
	plantname = 'Blue Cherry Tree'
	Description = "The blue kind of cherries."
	icon_state = 'seed-bluecherry'
	lifespan = 35
	endurance = 35
	production = 5
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'cherry-grow'
	dead_Sprite = 'cherry-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'nutriment':0.07, 'sugar':0.07}
	species = 'bluecherry'

List_of_plants.append(cherry_blue)

class grape():
	name = 'grape'
	plantname = 'Grape Vine'
	Description = "These seeds grow into grape vines."
	icon_state = 'seed-grapes'
	lifespan = 50
	endurance = 25
	production = 5
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'grape-grow'
	dead_Sprite = 'grape-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["grape_green"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1, 'sugar':0.1}
	species = 'grape'

List_of_plants.append(grape)

class grape_green():
	name = 'grape_green'
	plantname = 'Green-Grape Vine'
	Description = "These seeds grow into green-grape vines."
	icon_state = 'seed-greengrapes'
	lifespan = 50
	endurance = 25
	production = 5
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'grape-grow'
	dead_Sprite = 'grape-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'kelotane':0.2, 'vitamin':0.04, 'nutriment':0.1, 'sugar':0.1}
	species = 'greengrape'

List_of_plants.append(grape_green)

class cannabis():
	name = 'cannabis'
	plantname = 'Cannabis Plant'
	Description = "Taxable."
	icon_state = 'seed-cannabis'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'goon/icons/obj/hydroponics'
	Grown_Sprite = 'cannabis-grow' 
	dead_Sprite = 'cannabis-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = ["cannabis_rainbow","cannabis_death","cannabis_white","cannabis_ultimate"]
	reagents_add = {'space_drugs':0.15, 'lipolicide':0.35} 
	species = 'cannabis'

List_of_plants.append(cannabis)

class cannabis_rainbow():
	name = 'cannabis_rainbow'
	plantname = 'Rainbow Weed'
	Description = "These seeds grow into rainbow weed. Groovy."
	icon_state = 'seed-megacannabis'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'goon/icons/obj/hydroponics'
	Grown_Sprite = 'cannabis-grow' 
	dead_Sprite = 'cannabis-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'mindbreaker':0.15, 'lipolicide':0.35}
	species = 'megacannabis'

List_of_plants.append(cannabis_rainbow)

class cannabis_death():
	name = 'cannabis_death'
	plantname = 'Deathweed'
	Description = "These seeds grow into deathweed. Not groovy."
	icon_state = 'seed-blackcannabis'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'goon/icons/obj/hydroponics'
	Grown_Sprite = 'cannabis-grow' 
	dead_Sprite = 'cannabis-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'cyanide':0.35, 'space_drugs':0.15, 'lipolicide':0.15}
	species = 'blackcannabis'

List_of_plants.append(cannabis_death)

class cannabis_white():
	name = 'cannabis_white'
	plantname = 'Lifeweed'
	Description = "I will give unto him that is munchies of the fountain of the cravings of life, freely."
	icon_state = 'seed-whitecannabis'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'goon/icons/obj/hydroponics'
	Grown_Sprite = 'cannabis-grow' 
	dead_Sprite = 'cannabis-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'omnizine':0.35, 'space_drugs':0.15, 'lipolicide':0.15}
	species = 'whitecannabis'

List_of_plants.append(cannabis_white)

class cannabis_ultimate():
	name = 'cannabis_ultimate'
	plantname = 'Omega Weed'
	Description = "These seeds grow into omega weed."
	icon_state = 'seed-ocannabis'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'goon/icons/obj/hydroponics'
	Grown_Sprite = 'cannabis-grow' 
	dead_Sprite = 'cannabis-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'space_drugs':0.3,'mindbreaker':0.3,'mercury':0.15,'lithium':0.15,'atropine':0.15,'haloperidol':0.15,'methamphetamine':0.15,'capsaicin':0.15,'barbers_aid':0.15,'bath_salts':0.15,'itching_powder':0.15,'crank':0.15,'krokodil':0.15,'histamine':0.15,'lipolicide':0.15}
	species = 'ocannabis'

List_of_plants.append(cannabis_ultimate)

class wheat():
	name = 'wheat'
	plantname = 'Wheat Stalks'
	Description = "These may, or may not, grow into wheat."
	icon_state = 'seed-wheat'
	lifespan = 25
	endurance = 15
	production = 1
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'wheat-dead'
	mutates_into = ["wheat_oat","wheat_meat"]
	reagents_add = {'nutriment':0.04}
	species = 'wheat'

List_of_plants.append(wheat)

class wheat_oat():
	name = 'wheat_oat'
	plantname = 'Oat Stalks'
	Description = "These may, or may not, grow into oat."
	icon_state = 'seed-oat'
	lifespan = 25
	endurance = 15
	production = 1
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'wheat-dead'
	mutates_into = [""]
	reagents_add = {'nutriment':0.04}
	species = 'oat'

List_of_plants.append(wheat_oat)

class wheat_rice():
	name = 'wheat_rice'
	plantname = 'Rice Stalks'
	Description = "These may, or may not, grow into rice."
	icon_state = 'seed-rice'
	lifespan = 25
	endurance = 15
	production = 1
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'wheat-dead'
	mutates_into = [""]
	reagents_add = {'nutriment':0.04}
	species = 'rice'

List_of_plants.append(wheat_rice)

class wheat_meat():
	name = 'wheat_meat'
	plantname = 'Meatwheat'
	Description = "If you ever wanted to drive a vegetarian to insanity, here's how."
	icon_state = 'seed-meatwheat'
	lifespan = 25
	endurance = 15
	production = 1
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'wheat-dead'
	mutates_into = [""]
	reagents_add = {'nutriment':0.04}
	species = 'meatwheat'

List_of_plants.append(wheat_meat)

class chili():
	name = 'chili'
	plantname = 'Chili Plants'
	Description = "These seeds grow into chili plants. HOT! HOT! HOT!"
	icon_state = 'seed-chili'
	lifespan = 20
	endurance = 15
	production = 5
	plant_yield = 4
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'chili-grow' 
	dead_Sprite = 'chili-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = ["chili_ice","chili_ghost"]
	reagents_add = {'capsaicin':0.25, 'vitamin':0.04, 'nutriment':0.04}
	species = 'chili'

List_of_plants.append(chili)

class chili_ice():
	name = 'chili_ice'
	plantname = 'Ice Pepper Plants'
	Description = "These seeds grow into ice pepper plants."
	icon_state = 'seed-icepepper'
	lifespan = 25
	endurance = 15
	production = 4
	plant_yield = 4
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'chili-grow' 
	dead_Sprite = 'chili-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'frostoil':0.25, 'vitamin':0.02, 'nutriment':0.02}
	species = 'chiliice'

List_of_plants.append(chili_ice)

class chili_ghost():
	name = 'chili_ghost'
	plantname = 'Ghost Chili Plants'
	Description = "These seeds grow into a chili said to be the hottest in the galaxy."
	icon_state = 'seed-chilighost'
	lifespan = 20
	endurance = 10
	production = 10
	plant_yield = 3
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'chili-grow' 
	dead_Sprite = 'chili-dead' 
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'condensedcapsaicin':0.3, 'capsaicin':0.55, 'nutriment':0.04}
	species = 'chilighost'

List_of_plants.append(chili_ghost)

class lime():
	name = 'lime'
	plantname = 'Lime Tree'
	Description = "These are very sour seeds."
	icon_state = 'seed-lime'
	lifespan = 55
	endurance = 50
	production = 6
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	genes = ["Perennial_Growth"]
	mutates_into = ["orange"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.05}
	species = 'lime'

List_of_plants.append(lime)

class orange():
	name = 'orange'
	plantname = 'Orange Tree'
	Description = "Sour seeds."
	icon_state = 'seed-orange'
	lifespan = 60
	endurance = 50
	production = 6
	plant_yield = 5
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'lime-grow'
	dead_Sprite = 'lime-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["lime"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.05}
	species = 'orange'

List_of_plants.append(orange)

class lemon():
	name = 'lemon'
	plantname = 'Lemon Tree'
	Description = "These are sour seeds."
	icon_state = 'seed-lemon'
	lifespan = 55
	endurance = 45
	production = 6
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'lime-grow'
	dead_Sprite = 'lime-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["firelemon"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.05}
	species = 'lemon'

List_of_plants.append(lemon)

class firelemon():
	name = 'firelemon '
	plantname = 'Combustible Lemon Tree'
	Description = "When life gives you lemons, don't make lemonade. Make life take the lemons back! Get mad! I don't want your damn lemons!"
	icon_state = 'seed-firelemon'
	lifespan = 55
	endurance = 45
	production = 6
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'lime-grow'
	dead_Sprite = 'lime-dead'
	genes = ["Perennial_Growth"]
	reagents_add = {'nutriment':0.05}
	species = 'firelemon'

List_of_plants.append(firelemon)

class cocoapod():
	name = 'cocoapod'
	plantname = 'Cocao Tree'
	Description = "These seeds grow into cacao trees. They look fattening." 
	icon_state = 'seed-cocoapod'
	lifespan = 20
	endurance = 15
	production = 5
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'cocoapod-grow'
	dead_Sprite = 'cocoapod-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["cocoapod_vanillapod"]
	reagents_add = {'cocoa':0.25, 'nutriment':0.1}
	species = 'cocoapod'

List_of_plants.append(cocoapod)

class cocoapod_vanillapod():
	name = 'cocoapod_vanillapod'
	plantname = 'Vanilla Tree'
	Description = "These seeds grow into vanilla trees. They look fattening."
	icon_state = 'seed-vanillapod'
	lifespan = 20
	endurance = 15
	production = 5
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'cocoapod-grow'
	dead_Sprite = 'cocoapod-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'vanilla':0.25, 'nutriment':0.1}
	species = 'vanillapod'

List_of_plants.append(cocoapod_vanillapod)

class corn():
	name = 'corn'
	plantname = 'Corn Stalks'
	Description = "I don't mean to sound corny..."
	icon_state = 'seed-corn'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'corn-grow' 
	dead_Sprite = 'corn-dead' 
	mutates_into = ["corn_snapcorn"]
	reagents_add = {'cornoil':0.2, 'vitamin':0.04, 'nutriment':0.1}
	species = 'corn'

List_of_plants.append(corn)

class corn_snapcorn():
	name = 'corn_snapcorn'
	plantname = 'Snapcorn Stalks'
	Description = "Oh snap!"
	icon_state = 'seed-snapcorn'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'corn-grow' 
	dead_Sprite = 'corn-dead' 
	mutates_into = [""]
	reagents_add = {'cornoil':0.2, 'vitamin':0.04, 'nutriment':0.1}
	species = 'snapcorn'

List_of_plants.append(corn_snapcorn)

class eggplant():
	name = 'eggplant'
	plantname = 'Eggplants'
	Description = "These seeds grow to produce berries that look nothing like eggs."
	icon_state = 'seed-eggplant'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 2
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'eggplant-grow'
	dead_Sprite = 'eggplant-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["eggplant_eggy"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1}
	species = 'eggplant'

List_of_plants.append(eggplant)

class eggplant_eggy():
	name = 'eggplant_eggy'
	plantname = 'Eggplants'
	Description = "These seeds grow to produce berries that look a lot like eggs."
	icon_state = 'seed-eggy'
	lifespan = 75
	endurance = 15
	production = 12
	plant_yield = 2
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'eggplant-grow'
	dead_Sprite = 'eggplant-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'nutriment':0.1}
	species = 'eggy'

List_of_plants.append(eggplant_eggy)

class poppy():
	name = 'poppy'
	plantname = 'Poppy Plants'
	Description = "These seeds grow into poppies."
	icon_state = 'seed-poppy'
	lifespan = 25
	endurance = 10
	production = 6
	plant_yield = 6
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_flowers'
	Grown_Sprite = 'poppy-grow'
	dead_Sprite = 'poppy-dead'
	mutates_into = ["poppy_geranium","poppy_lily"]
	reagents_add = {'bicaridine':0.2, 'nutriment':0.05}
	species = 'poppy'

List_of_plants.append(poppy)

class poppy_lily():
	name = 'poppy_lily'
	plantname = 'Lily Plants'
	Description = "These seeds grow into lilies."
	icon_state = 'seed-lily'
	lifespan = 25
	endurance = 10
	production = 6
	plant_yield = 6
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_flowers'
	Grown_Sprite = 'poppy-grow'
	dead_Sprite = 'poppy-dead'
	mutates_into = [""]
	reagents_add = {'bicaridine':0.2, 'nutriment':0.05}
	species = 'lily'

List_of_plants.append(poppy_lily)

class poppy_geranium():
	name = 'poppy_geranium'
	plantname = 'Geranium Plants'
	Description = "These seeds grow into geranium."
	icon_state = 'seed-geranium'
	lifespan = 25
	endurance = 10
	production = 6
	plant_yield = 6
	potency = 20
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_flowers'
	Grown_Sprite = 'poppy-grow'
	dead_Sprite = 'poppy-dead'
	mutates_into = [""]
	reagents_add = {'bicaridine':0.2, 'nutriment':0.05}
	species = 'geranium'

List_of_plants.append(poppy_geranium)

class harebell():
	name = 'harebell'
	plantname = 'Harebells'
	Description = "These seeds grow into pretty little flowers."
	icon_state = 'seed-harebell'
	lifespan = 100
	endurance = 20
	production = 1
	plant_yield = 2
	potency = 30
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_flowers'
	genes = ["Weed Adaptation"]
	reagents_add = {'nutriment':0.04}
	species = 'harebell'

List_of_plants.append(harebell)

class sunflower():
	name = 'sunflower'
	plantname = 'Sunflowers'
	Description = "These seeds grow into sunflowers."
	icon_state = 'seed-sunflower'
	lifespan = 25
	endurance = 20
	production = 2
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_flowers'
	Grown_Sprite = 'sunflower-grow'
	dead_Sprite = 'sunflower-dead'
	mutates_into = ["sunflower_moonflower","sunflower_novaflower"]
	reagents_add = {'cornoil':0.08, 'nutriment':0.04}
	species = 'sunflower'

List_of_plants.append(sunflower)

class sunflower_moonflower():
	name = 'sunflower_moonflower'
	plantname = 'Moonflowers'
	Description = "These seeds grow into moonflowers."
	icon_state = 'seed-moonflower'
	lifespan = 25
	endurance = 20
	production = 2
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_flowers'
	Grown_Sprite = 'moonflower-grow'
	dead_Sprite = 'sunflower-dead'
	mutates_into = [""]
	reagents_add = {'moonshine':0.2, 'vitamin':0.02, 'nutriment':0.02}
	species = 'moonflower'

List_of_plants.append(sunflower_moonflower)

class sunflower_novaflower():
	name = 'sunflower_novaflower'
	plantname = 'Novaflowers'
	Description = "These seeds grow into novaflowers."
	icon_state = 'seed-novaflower'
	lifespan = 25
	endurance = 20
	production = 2
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_flowers'
	Grown_Sprite = 'novaflower-grow'
	dead_Sprite = 'sunflower-dead'
	mutates_into = [""]
	reagents_add = {'condensedcapsaicin':0.25, 'capsaicin':0.3, 'nutriment':0}
	species = 'novaflower'

List_of_plants.append(sunflower_novaflower)

class grass():
	name = 'grass'
	plantname = 'Grass'
	Description = "These seeds grow into grass. Yummy!"
	icon_state = 'seed-grass'
	lifespan = 40
	endurance = 40
	production = 5
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	Grown_Sprite = 'grass-grow'
	dead_Sprite = 'grass-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["grass_carpet"]
	reagents_add = {'nutriment':0.02, 'hydrogen':0.05}
	species = 'grass'

List_of_plants.append(grass)

class grass_carpet():
	name = 'grass_carpet'
	plantname = 'Carpet'
	Description = "These seeds grow into stylish carpet samples."
	icon_state = 'seed-carpet'
	lifespan = 40
	endurance = 40
	production = 5
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	Grown_Sprite = 'grass-grow'
	dead_Sprite = 'grass-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'nutriment':0.02, 'hydrogen':0.05}
	species = 'carpet'

List_of_plants.append(grass_carpet)

class kudzu():
	name = 'kudzu'
	plantname = 'Kudzu'
	Description = "These seeds grow into a weed that grows incredibly fast."
	icon_state = 'seed-kudzu'
	lifespan = 20
	endurance = 10
	production = 6
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	genes = ["Perennial_Growth", "Weed Adaptation"]
	reagents_add = {'charcoal':0.04, 'nutriment':0.02}
	species = 'kudzu'

List_of_plants.append(kudzu)

class watermelon():
	name = 'watermelon'
	plantname = 'Watermelon Vines'
	Description = "These seeds grow into watermelon plants."
	icon_state = 'seed-watermelon'
	lifespan = 50
	endurance = 40
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	dead_Sprite = 'watermelon-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["watermelon_holy"]
	reagents_add = {'water':0.2, 'vitamin':0.04, 'nutriment':0.2}
	species = 'watermelon'

List_of_plants.append(watermelon)

class watermelon_holy():
	name = 'watermelon_holy'
	plantname = 'Holy Melon Vines'
	Description = "These seeds grow into holymelon plants."
	icon_state = 'seed-holymelon'
	lifespan = 50
	endurance = 40
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	dead_Sprite = 'watermelon-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'holywater':0.2, 'vitamin':0.04, 'nutriment':0.1}
	species = 'holymelon'

List_of_plants.append(watermelon_holy)

class starthistle():
	name = 'starthistle'
	plantname = 'Starthistle'
	Description = "A robust species of weed that often springs up in-between the cracks of spaceship parking lots."
	icon_state = 'seed-starthistle'
	lifespan = 70
	endurance = 50 
	production = 1
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_flowers'
	genes = ["Weed Adaptation"]
	mutates_into = ["harebell"]
	species = 'starthistle'

List_of_plants.append(starthistle)

class cabbage():
	name = 'cabbage'
	plantname = 'Cabbages'
	Description = "These seeds grow into cabbages."
	icon_state = 'seed-cabbage'
	lifespan = 50
	endurance = 25
	production = 5
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	genes = ["Perennial_Growth"]
	mutates_into = ["replicapod"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1}
	species = 'cabbage'

List_of_plants.append(cabbage)

class sugarcane():
	name = 'sugarcane'
	plantname = 'Sugarcane'
	Description = "These seeds grow into sugarcane."
	icon_state = 'seed-sugarcane'
	lifespan = 60
	endurance = 50
	production = 6
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	genes = ["Perennial_Growth"]
	reagents_add = {'sugar':0.25}
	species = 'sugarcane'

List_of_plants.append(sugarcane)

class gatfruit():
	name = 'gatfruit'
	plantname = 'Gatfruit Tree'
	Description = "These seeds grow into .357 revolvers."
	icon_state = 'seed-gatfruit'
	lifespan = 20
	endurance = 20
	production = 10
	plant_yield = 2
	potency = 60
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	genes = ["Perennial_Growth"]
	reagents_add = {'sulfur':0.1, 'carbon':0.1, 'nitrogen':0.07, 'potassium':0.05}
	species = 'gatfruit'

List_of_plants.append(gatfruit)

class cherry_bomb():
	name = 'cherry_bomb'
	plantname = 'Cherry Bomb Tree'
	Description = "They give you vibes of dread and frustration."
	icon_state = 'seed-cherry_bomb'
	lifespan = 35
	endurance = 35
	production = 5
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'cherry-grow'
	dead_Sprite = 'cherry-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'nutriment':0.1, 'sugar':0.1, 'blackpowder':0.7}
	species = 'cherry_bomb'

List_of_plants.append(cherry_bomb)

class reishi():
	name = 'reishi'
	plantname = 'Reishi'
	Description = "This mycelium grows into something medicinal and relaxing."
	icon_state = 'mycelium-reishi'
	lifespan = 35
	endurance = 35
	production = 5
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	reagents_add = {'morphine':0.35, 'charcoal':0.35, 'nutriment':0}
	species = 'reishi'

List_of_plants.append(reishi)

class amanita():
	name = 'amanita'
	plantname = 'Fly Amanitas'
	Description = "This mycelium grows into something horrible."
	icon_state = 'mycelium-amanita'
	lifespan = 50
	endurance = 35
	production = 5
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	mutates_into = ["angel"]
	reagents_add = {'mushroomhallucinogen':0.04, 'amatoxin':0.35, 'nutriment':0, 'growthserum':0.1}
	species = 'amanita'

List_of_plants.append(amanita)

class angel():
	name = 'angel'
	plantname = 'Destroying Angels'
	Description = "This mycelium grows into something devastating."
	icon_state = 'mycelium-angel'
	lifespan = 50
	endurance = 35
	production = 5
	plant_yield = 2
	potency = 35
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	reagents_add = {'mushroomhallucinogen':0.04, 'amatoxin':0.1, 'nutriment':0, 'amanitin':0.2}
	species = 'angel'

List_of_plants.append(angel)

class liberty():
	name = 'liberty'
	plantname = 'Liberty-Caps'
	Description = "This mycelium grows into liberty-cap mushrooms."
	icon_state = 'mycelium-liberty'
	lifespan = 25
	endurance = 15
	production = 1
	plant_yield = 5
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	reagents_add = {'mushroomhallucinogen':0.25, 'nutriment':0.02}
	species = 'liberty'

List_of_plants.append(liberty)

class plump():
	name = 'plump'
	plantname = 'Plump-Helmet Mushrooms'
	Description = "This mycelium grows into helmets... maybe."
	icon_state = 'mycelium-plump'
	lifespan = 25
	endurance = 15
	production = 1
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	mutates_into = ["plump_walkingmushroom"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1}
	species = 'plump'

List_of_plants.append(plump)

class plump_walkingmushroom():
	name = 'plump_walkingmushroom'
	plantname = 'Walking Mushrooms'
	Description = "This mycelium will grow into huge stuff!"
	icon_state = 'mycelium-walkingmushroom'
	lifespan = 30
	endurance = 30
	production = 1
	plant_yield = 1
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	mutates_into = [""]
	reagents_add = {'vitamin':0.05, 'nutriment':0.15}
	species = 'walkingmushroom'

List_of_plants.append(plump_walkingmushroom)

class chanter():
	name = 'chanter'
	plantname = 'Chanterelle Mushrooms'
	Description = "This mycelium grows into chanterelle mushrooms."
	icon_state = 'mycelium-chanter'
	lifespan = 35
	endurance = 20
	production = 1
	plant_yield = 5
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	reagents_add = {'nutriment':0.1}
	species = 'chanter'

List_of_plants.append(chanter)

class glowshroom():
	name = 'glowshroom'
	plantname = 'Glowshrooms'
	Description = "This mycelium -glows- into mushrooms!"
	icon_state = 'mycelium-glowshroom'
	lifespan = 100 
	endurance = 30
	production = 1
	plant_yield = 3 
	potency = 30 
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Bioluminescence", "Fungal Vitality"]
	mutates_into = ["glowshroom_glowcap","glowshroom_shadowshroom"]
	reagents_add = {'radium':0.1, 'phosphorus':0.1, 'nutriment':0.04}
	species = 'glowshroom'

List_of_plants.append(glowshroom)

class glowshroom_glowcap():
	name = 'glowshroom_glowcap'
	plantname = 'Glowcaps'
	Description = "This mycelium -powers- into mushrooms!"
	icon_state = 'mycelium-glowcap'
	lifespan = 100 
	endurance = 30
	production = 1
	plant_yield = 3 
	potency = 30 
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	Grown_Sprite = 'glowshroom-grow'
	dead_Sprite = 'glowshroom-dead'
	genes = ["Red Electrical Glow", "Electrical Activity", "Fungal Vitality"]
	mutates_into = [""]
	reagents_add = {'teslium':0.1, 'nutriment':0.04}
	species = 'glowcap'

List_of_plants.append(glowshroom_glowcap)

class glowshroom_shadowshroom():
	name = 'glowshroom_shadowshroom'
	plantname = 'Shadowshrooms'
	Description = "This mycelium will grow into something shadowy."
	icon_state = 'mycelium-shadowshroom'
	lifespan = 100 
	endurance = 30
	production = 1
	plant_yield = 3 
	potency = 30 
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	Grown_Sprite = 'shadowshroom-grow'
	dead_Sprite = 'shadowshroom-dead'
	genes = ["Shadow Emission", "Fungal Vitality"]
	mutates_into = [""]
	reagents_add = {'radium':0.2, 'nutriment':0.04}
	species = 'shadowshroom'

List_of_plants.append(glowshroom_shadowshroom)

class lavaland():
	name = 'lavaland'
	Description = "You should never see this."
	lifespan = 50
	endurance = 25
	production = 4
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	reagents_add = {'nutriment':0.1}

List_of_plants.append(lavaland)

class lavaland_polypore():
	name = 'lavaland_polypore'
	plantname = 'Polypore Mushrooms'
	Description = "This mycelium grows into bracket mushrooms, also known as polypores. Woody and firm, shaft miners often use them for makeshift crafts."
	icon_state = 'mycelium-polypore'
	lifespan = 50
	endurance = 25
	production = 4
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	reagents_add = {'nutriment':0.1}
	species = 'polypore'

List_of_plants.append(lavaland_polypore)

class lavaland_porcini():
	name = 'lavaland_porcini'
	plantname = 'Porcini Mushrooms'
	Description = "This mycelium grows into Boletus edulus, also known as porcini. Native to the late Earth, but discovered on Lavaland. Has culinary, medicinal and relaxant effects."
	icon_state = 'mycelium-porcini'
	lifespan = 50
	endurance = 25
	production = 4
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	reagents_add = {'nutriment':0.1}
	species = 'porcini'

List_of_plants.append(lavaland_porcini)

class lavaland_inocybe():
	name = 'lavaland_inocybe'
	plantname = 'Inocybe Mushrooms'
	Description = "This mycelium grows into an inocybe mushroom, a species of Lavaland origin with hallucinatory and toxic effects."
	icon_state = 'mycelium-inocybe'
	lifespan = 50
	endurance = 25
	production = 4
	plant_yield = 4
	potency = 15
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	genes = ["Fungal Vitality"]
	reagents_add = {'nutriment':0.1}
	species = 'inocybe'

List_of_plants.append(lavaland_inocybe)

class nettle():
	name = 'nettle'
	plantname = 'Nettles'
	Description = "These seeds grow into nettles."
	icon_state = 'seed-nettle'
	lifespan = 30
	endurance = 40 
	production = 6
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	genes = ["Perennial_Growth", "Weed Adaptation"]
	mutates_into = ["nettle_death"]
	reagents_add = {'sacid':0.5}
	species = 'nettle'

List_of_plants.append(nettle)

class nettle_death():
	name = 'nettle_death'
	plantname = 'Death Nettles'
	Description = "These seeds grow into death-nettles."
	icon_state = 'seed-deathnettle'
	lifespan = 30
	endurance = 25
	production = 6
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	genes = ["Perennial_Growth", "Weed Adaptation", "Hypodermic Prickles"]
	mutates_into = [""]
	reagents_add = {'facid':0.5, 'sacid':0.5}
	species = 'deathnettle'

List_of_plants.append(nettle_death)

class onion():
	name = 'onion'
	plantname = 'Onion Sprouts'
	Description = "These seeds grow into onions."
	icon_state = 'seed-onion'
	lifespan = 20
	endurance = 25
	production = 4
	plant_yield = 6
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	mutates_into = ["onion_red"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1}
	species = 'onion'

List_of_plants.append(onion)

class onion_red():
	name = 'onion_red'
	plantname = 'Red Onion Sprouts'
	Description = "For growing exceptionally potent onions."
	icon_state = 'seed-onionred'
	lifespan = 20
	endurance = 25
	production = 4
	plant_yield = 6
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	reagents_add = {'vitamin':0.04, 'nutriment':0.1, 'tearjuice':0.05}
	species = 'onion_red'

List_of_plants.append(onion_red)

class potato():
	name = 'potato'
	plantname = 'Potato Plants'
	Description = "Boil 'em! Mash 'em! Stick 'em in a stew!"
	icon_state = 'seed-potato'
	lifespan = 30
	endurance = 15
	production = 1
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'potato-grow'
	dead_Sprite = 'potato-dead'
	genes = ["Capacitive Cell Production"]
	mutates_into = ["potato_sweet"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1}
	species = 'potato'

List_of_plants.append(potato)

class potato_sweet():
	name = 'potato_sweet'
	plantname = 'Sweet Potato Plants'
	Description = "These seeds grow into sweet potato plants."
	icon_state = 'seed-sweetpotato'
	lifespan = 30
	endurance = 15
	production = 1
	plant_yield = 4
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	Grown_Sprite = 'potato-grow'
	dead_Sprite = 'potato-dead'
	genes = ["Capacitive Cell Production"]
	mutates_into = [""]
	reagents_add = {'vitamin':0.1, 'sugar':0.1, 'nutriment':0.1}
	species = 'sweetpotato'

List_of_plants.append(potato_sweet)

class pumpkin():
	name = 'pumpkin'
	plantname = 'Pumpkin Vines'
	Description = "These seeds grow into pumpkin vines."
	icon_state = 'seed-pumpkin'
	lifespan = 50
	endurance = 40
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'pumpkin-grow'
	dead_Sprite = 'pumpkin-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["pumpkin_blumpkin"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.2}
	species = 'pumpkin'

List_of_plants.append(pumpkin)

class pumpkin_blumpkin():
	name = 'pumpkin_blumpkin'
	plantname = 'Blumpkin Vines'
	Description = "These seeds grow into blumpkin vines."
	icon_state = 'seed-blumpkin'
	lifespan = 50
	endurance = 40
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'pumpkin-grow'
	dead_Sprite = 'pumpkin-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'ammonia':0.2, 'chlorine':0.1, 'nutriment':0.2}
	species = 'blumpkin'

List_of_plants.append(pumpkin_blumpkin)

class random():
	name = 'random'
	plantname = 'strange plant'
	Description = "Mysterious seeds as strange as their name implies. Spooky."
	icon_state = 'seed-x'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	Grown_Sprite = 'xpod-grow'
	dead_Sprite = 'xpod-dead'
	species = '?????'

List_of_plants.append(random)

class replicapod():
	name = 'replicapod'
	plantname = 'Replica Pod'
	Description = "These seeds grow into replica pods. They say these are used to harvest humans."
	icon_state = 'seed-replicapod'
	lifespan = 50
	endurance = 8
	production = 1
	plant_yield = 1 
	potency = 30
	weed_growth_rate = 1
	weed_resistance = 5
	species = 'replicapod'

List_of_plants.append(replicapod)

class carrot():
	name = 'carrot'
	plantname = 'Carrots'
	Description = "These seeds grow into carrots."
	icon_state = 'seed-carrot'
	lifespan = 25
	endurance = 15
	production = 1
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	mutates_into = ["carrot_parsnip"]
	reagents_add = {'oculine':0.25, 'vitamin':0.04, 'nutriment':0.05}
	species = 'carrot'

List_of_plants.append(carrot)

class carrot_parsnip():
	name = 'carrot_parsnip'
	plantname = 'Parsnip'
	Description = "These seeds grow into parsnips."
	icon_state = 'seed-parsnip'
	lifespan = 25
	endurance = 15
	production = 1
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	dead_Sprite = 'carrot-dead'
	mutates_into = [""]
	reagents_add = {'vitamin':0.05, 'nutriment':0.05}
	species = 'parsnip'

List_of_plants.append(carrot_parsnip)

class whitebeet():
	name = 'whitebeet'
	plantname = 'White-Beet Plants'
	Description = "These seeds grow into sugary beet producing plants."
	icon_state = 'seed-whitebeet'
	lifespan = 60
	endurance = 50
	production = 6
	plant_yield = 6
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	dead_Sprite = 'whitebeet-dead'
	mutates_into = ["redbeet"]
	reagents_add = {'vitamin':0.04, 'sugar':0.2, 'nutriment':0.05}
	species = 'whitebeet'

List_of_plants.append(whitebeet)

class redbeet():
	name = 'redbeet'
	plantname = 'Red-Beet Plants'
	Description = "These seeds grow into red beet producing plants."
	icon_state = 'seed-redbeet'
	lifespan = 60
	endurance = 50
	production = 6
	plant_yield = 6
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_vegetables'
	dead_Sprite = 'whitebeet-dead'
	genes = ["Densified Chemicals"]
	reagents_add = {'vitamin':0.05, 'nutriment':0.05}
	species = 'redbeet'

List_of_plants.append(redbeet)

class tea():
	name = 'tea'
	plantname = 'Tea Aspera Plant'
	Description = "These seeds grow into tea plants."
	icon_state = 'seed-teaaspera'
	lifespan = 20
	endurance = 15
	production = 5
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'tea-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["tea_astra"]
	reagents_add = {'vitamin':0.04, 'teapowder':0.1}
	species = 'teaaspera'

List_of_plants.append(tea)

class tea_astra():
	name = 'tea_astra'
	plantname = 'Tea Astra Plant'
	Description = "These seeds grow into tea plants."
	icon_state = 'seed-teaastra'
	lifespan = 20
	endurance = 15
	production = 5
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'tea-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'synaptizine':0.1, 'vitamin':0.04, 'teapowder':0.1}
	species = 'teaastra'

List_of_plants.append(tea_astra)

class coffee():
	name = 'coffee'
	plantname = 'Coffee Arabica Bush'
	Description = "These seeds grow into coffee arabica bushes."
	icon_state = 'seed-coffeea'
	lifespan = 30
	endurance = 20
	production = 5
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'coffee-dead'
	genes = ["Perennial_Growth"]
	mutates_into = ["coffee_robusta"]
	reagents_add = {'vitamin':0.04, 'coffeepowder':0.1}
	species = 'coffeea'

List_of_plants.append(coffee)

class coffee_robusta():
	name = 'coffee_robusta'
	plantname = 'Coffee Robusta Bush'
	Description = "These seeds grow into coffee robusta bushes."
	icon_state = 'seed-coffeer'
	lifespan = 30
	endurance = 20
	production = 5
	plant_yield = 5
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'coffee-dead'
	genes = ["Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'ephedrine':0.1, 'vitamin':0.04, 'coffeepowder':0.1}
	species = 'coffeer'

List_of_plants.append(coffee_robusta)

class tobacco():
	name = 'tobacco'
	plantname = 'Tobacco Plant'
	Description = "These seeds grow into tobacco plants."
	icon_state = 'seed-tobacco'
	lifespan = 20
	endurance = 15
	production = 5
	plant_yield = 10
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'tobacco-dead'
	mutates_into = ["tobacco_space"]
	reagents_add = {'nicotine':0.03, 'nutriment':0.03}
	species = 'tobacco'

List_of_plants.append(tobacco)

class tobacco_space():
	name = 'tobacco_space'
	plantname = 'Space Tobacco Plant'
	Description = "These seeds grow into space tobacco plants."
	icon_state = 'seed-stobacco'
	lifespan = 20
	endurance = 15
	production = 5
	plant_yield = 10
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	dead_Sprite = 'tobacco-dead'
	mutates_into = [""]
	reagents_add = {'salbutamol':0.05, 'nicotine':0.08, 'nutriment':0.03}
	species = 'stobacco'

List_of_plants.append(tobacco_space)

class tomato():
	name = 'tomato'
	plantname = 'Tomato Plants'
	Description = "These seeds grow into tomato plants."
	icon_state = 'seed-tomato'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'tomato-grow'
	dead_Sprite = 'tomato-dead'
	genes = ["Liquid Contents", "Perennial_Growth"]
	mutates_into = ["tomato_blue","tomato_blood","tomato_killer"]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1}
	species = 'tomato'

List_of_plants.append(tomato)

class tomato_blood():
	name = 'tomato_blood'
	plantname = 'Blood-Tomato Plants'
	Description = "These seeds grow into blood-tomato plants."
	icon_state = 'seed-bloodtomato'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 3
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'tomato-grow'
	dead_Sprite = 'tomato-dead'
	genes = ["Liquid Contents", "Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'blood':0.2, 'vitamin':0.04, 'nutriment':0.1}
	species = 'bloodtomato'

List_of_plants.append(tomato_blood)

class tomato_blue():
	name = 'tomato_blue'
	plantname = 'Blue-Tomato Plants'
	Description = "These seeds grow into blue-tomato plants."
	icon_state = 'seed-bluetomato'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'bluetomato-grow'
	dead_Sprite = 'tomato-dead'
	genes = ["Slippery Skin", "Perennial_Growth"]
	mutates_into = ["tomato_blue_bluespace"]
	reagents_add = {'lube':0.2, 'vitamin':0.04, 'nutriment':0.1}
	species = 'bluetomato'

List_of_plants.append(tomato_blue)

class tomato_blue_bluespace():
	name = 'tomato_blue_bluespace'
	plantname = 'Bluespace Tomato Plants'
	Description = "These seeds grow into bluespace tomato plants."
	icon_state = 'seed-bluespacetomato'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'tomato-grow'
	dead_Sprite = 'tomato-dead'
	genes = ["Liquid Contents", "Slippery Skin", "Bluespace Activity", "Perennial_Growth"]
	mutates_into = [""]
	reagents_add = {'lube':0.2, 'bluespace':0.2, 'vitamin':0.04, 'nutriment':0.1}
	species = 'bluespacetomato'

List_of_plants.append(tomato_blue_bluespace)

class tomato_killer():
	name = 'tomato_killer'
	plantname = 'Killer-Tomato Plants'
	Description = "These seeds grow into killer-tomato plants."
	icon_state = 'seed-killertomato'
	lifespan = 25
	endurance = 15
	production = 6
	plant_yield = 2
	potency = 10
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_fruits'
	Grown_Sprite = 'killertomato-grow'
	dead_Sprite = 'killertomato-dead'
	genes = ["Liquid Contents"]
	mutates_into = [""]
	reagents_add = {'vitamin':0.04, 'nutriment':0.1}
	species = 'killertomato'

List_of_plants.append(tomato_killer)

class tower():
	name = 'tower'
	plantname = 'Tower Caps'
	Description = "This mycelium grows into tower-cap mushrooms."
	icon_state = 'mycelium-tower'
	lifespan = 80
	endurance = 50
	production = 1
	plant_yield = 5
	potency = 50
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	dead_Sprite = 'towercap-dead'
	genes = ["Fungal Vitality"]
	mutates_into = ["tower_steel"]
	species = 'towercap'

List_of_plants.append(tower)

class tower_steel():
	name = 'tower_steel'
	plantname = 'Steel Caps'
	Description = "This mycelium grows into steel logs."
	icon_state = 'mycelium-steelcap'
	lifespan = 80
	endurance = 50
	production = 1
	plant_yield = 5
	potency = 50
	weed_growth_rate = 1
	weed_resistance = 5
	growing_icon = 'growing_mushrooms'
	dead_Sprite = 'towercap-dead'
	genes = ["Fungal Vitality"]
	mutates_into = [""]
	species = 'steelcap'

List_of_plants.append(tower_steel)
