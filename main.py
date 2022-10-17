from PIL import Image
import itertools

combo_num = 2
layer_num = 2
gen_dir = input(r'Enter Filepath to layers to combine: ')

final_paths = []
for a in range(layer_num):
    layer_paths = []
    layer_path = gen_dir + '\layer_' + str(a+1)
    for b in range(combo_num):
        layer_paths.append(layer_path + '\layer_' + str(a+1) + '_' + str(b+1) + '.png')
    final_paths.append(layer_paths)

combos = (list(itertools.product(range(combo_num), range(combo_num))))


for x in range(len(combos)):
    # create all combo file path lists
    combo = list(combos[x])
    path_combos = []
    for y in range(len(combo)):
        part_num = combo[y]
        path_list = final_paths[y]
        path_combos.append(path_list[part_num])

    final = Image.open(path_combos[0])
    for z in range(len(path_combos)):
        if z >> 0:
            overlay = Image.open(path_combos[z])
            final.paste(overlay,(0,0),overlay)
    final.show()





