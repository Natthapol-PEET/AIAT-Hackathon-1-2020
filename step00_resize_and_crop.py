import os

from PIL import Image
from tqdm import tqdm
from resizeimage import resizeimage

def convert(raw_path):
    path = os.path.join('original', raw_path)
    new_path = os.path.join('cropped', raw_path)

    os.makedirs(new_path, exist_ok=True)
    files = os.listdir(path)

    for file in tqdm(files):
        with open(os.path.join(path, file), 'r+b') as f:
            with Image.open(f) as image:

                filename = file
        
                if '.png' in file:
                    image = image.convert('RGB')
                    filename = file.replace('.png', '.jpg')
                elif '.jpeg' in file:
                    filename = file.replace('.jpeg', '.jpg')

                try:
                    cover = resizeimage.resize_cover(image, [310, 310])
                    cover.save(os.path.join(new_path, filename), image.format)
                except:
                    width, height = image.size
                    image = image.resize((width+200,height+200), Image.LANCZOS)
                    cover = resizeimage.resize_cover(image, [310, 310])
                    cover.save(os.path.join(new_path, filename), image.format)

convert('train/covid')
convert('train/normal')
convert('train/pneumonia')
convert('val/covid')
convert('val/normal')
convert('val/pneumonia')