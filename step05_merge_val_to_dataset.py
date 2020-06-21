import os
import cv2

from tqdm import tqdm
from shutil import move

SOURCE_PATH = 'merge'

def process_filename(base_path, name, append, ext):
    return os.path.join(base_path, '{0}_{1}{2}'.format(name, append, ext))

def process(pathname, target_name):
    cur_path = os.path.join(SOURCE_PATH, pathname)
    new_path = os.path.join(SOURCE_PATH, target_name)

    for filename in tqdm(os.listdir(cur_path)):
        file_path = os.path.join(cur_path, filename)
        move(file_path, os.path.join(new_path, 'val_{0}'.format(filename)))

process('val/covid', 'train/covid')
process('val/normal', 'train/normal')
process('val/pneumonia', 'train/pneumonia')