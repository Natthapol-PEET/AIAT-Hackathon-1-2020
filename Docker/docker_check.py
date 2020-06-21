import os
import pathlib
import requests

from tqdm import tqdm

basepath = pathlib.Path(__file__).parent.absolute()

files = os.listdir('test_release')
files.sort()

outputs = []

for file in tqdm(files):
    with open(os.path.join('test_release', file), 'rb') as f:
        r = requests.post('http://localhost:8000/predict', files={'image': f})
        outputs.append('{},{}'.format(os.path.splitext(file)[0], r.json().get('Predicted')))

with open('test.csv', 'w') as f:
    f.write('Id,Predicted\n')
    f.write('\n'.join(outputs))
