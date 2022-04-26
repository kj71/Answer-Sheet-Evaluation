import os, io

import cv2
from google.cloud import vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision.ImageAnnotatorClient()


# Get an image with text
def recognize(FILE_PATH):
    with io.open(FILE_PATH, 'rb') as file:
        content = file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    docText = response.full_text_annotation.text

    return docText
