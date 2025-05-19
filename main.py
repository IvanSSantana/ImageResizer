import os
from pathlib import Path
from PIL import Image
from argparse import ArgumentParser

parser = ArgumentParser(
    prog='Image Resizer',
    description='Changes the size of an any image (%)',)

parser.add_argument(
    'percent',
    help='Sizes\' percent of the new image.',
    type=int,
    action='store'
)

arg = parser.parse_args()

if arg.percent is None:
    print('Please, type a percent of the new image.')

ROOT = Path(__file__).parent
img_extensions = ['.jpg', '.jpeg', '.png', '.webp']
try:
    reducer_percent = int(arg.percent)
except ValueError:
    print('Valor inválido, por favor tente novamente.')

ratio = reducer_percent / 100

for root, dirs, files in os.walk(ROOT):
    for file_ in files:
        file_route = Path(root) / file_
        extension = file_route.suffix.lower()

        if extension in img_extensions:
            pil_img = Image.open(file_route)
            width, height = pil_img.size

            new_width = round(width * ratio)
            new_height = round(height * ratio)
            
            new_img = pil_img.resize(size=(new_width, new_height))
            try:
                new_file = file_route.parent / f'{file_route.name.replace(extension, '')}_new{extension}'
                new_img.save(new_file, optimize=True, quality=70)
                file_route.unlink()
            except Exception as error:
                raise error
            finally:
                pil_img.close()
                new_img.close() # Por garantia
        else: pass