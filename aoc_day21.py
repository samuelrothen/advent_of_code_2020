# Advent of Code Day 21


data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""




food_list = []
for line in data.split('\n'):
    ingr, allerg = line.split(' (contains ')
    ingr = ingr.split()
    allerg = allerg[:-1].split(', ')
    food_list.append((ingr, allerg))




