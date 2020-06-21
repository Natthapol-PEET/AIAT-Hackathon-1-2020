import os
import cv2

from tqdm import tqdm
from shutil import copyfile
from scipy import ndimage, misc

SOURCE_PATH = 'step01'
DESTINATION_PATH = 'step02'

def process_filename(base_path, name, append, ext):
    return os.path.join(base_path, '{0}_{1}{2}'.format(name, append, ext))

def process(pathname):
    cur_path = os.path.join(SOURCE_PATH, pathname)
    new_path = os.path.join(DESTINATION_PATH, pathname)

    os.makedirs(new_path, exist_ok=True)

    for filename in tqdm(os.listdir(cur_path)):
        file_path = os.path.join(cur_path, filename)

        realname, extension = os.path.splitext(filename)

        image = cv2.imread(file_path)
        image2 = image.copy()

        rotate_p5 = ndimage.rotate(image, -5, reshape=False)
        cv2.imwrite(process_filename(new_path, realname, 'rotate_p5', extension), rotate_p5)

        rotate_m5 = ndimage.rotate(image2, 5, reshape=False)
        cv2.imwrite(process_filename(new_path, realname, 'rotate_m5', extension), rotate_m5)

process('train/covid')
process('train/normal')
process('train/pneumonia')
process('val/covid')
process('val/normal')
process('val/pneumonia')
