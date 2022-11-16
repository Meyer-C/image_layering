from PIL import Image
import itertools

def get_paths():
    with open(r'C:\Users\Camden\PycharmProject\nft_layering\paths.txt', 'r') as a:
        b = a.readlines()
        project_name = ((b[0].split('=')[1]).replace(' ', '')).replace('\n', '')
        in_gen_path = ((b[1].split('=')[1]).replace(' ', '')).replace('\n', '')
        out_path = ((b[2].split('=')[1]).replace(' ', '')).replace('\n', '')
        layers = int(((b[3].split('=')[1]).replace(' ', '')).replace('\n', ''))
        combos = int(((b[4].split('=')[1]).replace(' ', '')).replace('\n', ''))

        input_strs = []
        for x in range(layers):
            layer_strs = []
            for y in range(combos):
                layer_strs.append(str(f'{in_gen_path}\\layer_{x+1}\\layer_{x+1}_{y+1}.png'))
            input_strs.append(layer_strs)

    return (input_strs, project_name, out_path)

def layer(paths_data, show=False, save=False):
    input_strs = paths_data[0]
    project_name = paths_data[1]
    out_path = paths_data[2]
    combos = list(itertools.product(*input_strs))
    for x, combo in enumerate(combos):
        image = Image.open(combo[0])
        out_filepath = str(f'{out_path}\\{project_name}_{x}.png')
        for path in combo[1::]:
            overlay = Image.open(path)
            image.paste(overlay, (0, 0), overlay)
        if show == True and save == True:
            image.show()
            image.save(out_filepath)
        elif show == True:
            image.show()
        elif save == True:
            image.save(out_filepath)

layer(get_paths(), show=True, save=True)