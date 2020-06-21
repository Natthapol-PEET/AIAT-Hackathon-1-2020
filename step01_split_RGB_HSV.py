import os
import cv2

from tqdm import tqdm
from shutil import copyfile

SOURCE_PATH = 'cropped'
DESTINATION_PATH = 'step01'

def process_filename(base_path, name, append, ext):
    return os.path.join(base_path, '{0}_{1}{2}'.format(name, append, ext))

def process(pathname):
    cur_path = os.path.join(SOURCE_PATH, pathname)
    new_path = os.path.join(DESTINATION_PATH, pathname)

    os.makedirs(new_path, exist_ok=True)

    for filename in tqdm(os.listdir(cur_path)):
        file_path = os.path.join(cur_path, filename)
        copyfile(file_path, os.path.join(new_path, filename))

        realname, extension = os.path.splitext(filename)

        image = cv2.imread(file_path)
        image2 = image.copy()

        B, G, R = cv2.split(image)
        cv2.imwrite(process_filename(new_path, realname, 'R', extension), R)
        # cv2.imwrite(process_filename(new_path, realname, 'G', extension), G)
        cv2.imwrite(process_filename(new_path, realname, 'B', extension), B)

        image = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
        H,S,V = cv2.split(image)
        # cv2.imwrite(process_filename(new_path, realname, 'H', extension), H)
        # cv2.imwrite(process_filename(new_path, realname, 'S', extension), S)
        cv2.imwrite(process_filename(new_path, realname, 'V', extension), V)

process('train/covid')
process('train/normal')
process('train/pneumonia')
process('val/covid')
process('val/normal')
process('val/pneumonia')