from __future__ import print_function, division

from flask import Flask, request
from flask_restful import Resource, Api

import os
import torch
import torchvision
import torch.nn as nn

from PIL import Image
from torchvision import models, transforms

print(torch.__version__)
print(torchvision.__version__)

MODEL_FILE_NAME = 'model_resNet18_v3.pth'

device = torch.device("cpu")

model_ft = models.resnet18()

for param in model_ft.parameters():
    param.requires_grad = False

num_features = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_features, 3)

model_ft = model_ft.to(device)
model_ft.load_state_dict(torch.load(MODEL_FILE_NAME, map_location=device))
model_ft.eval()

data_transforms_pre = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])


def predict(image_path):
    image = Image.open(image_path).convert('RGB')
    image = data_transforms_pre(image)
    image = image.to(device)
    image = image.unsqueeze(0)
    return model_ft(image)


class IndexPage(Resource):
    def get(self):
        return MODEL_FILE_NAME


class PredictAPI(Resource):
    def post(self):
        image = request.files['image']
        output = predict(image)
        _, preds = torch.max(output, 1)
        return {'Predicted': '{}'.format(preds.item())}


app = Flask(__name__)
api = Api(app)

api.add_resource(IndexPage, '/')
api.add_resource(PredictAPI, '/predict')

app.run(debug=True, host='0.0.0.0', port='8000')
