from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import json

credentials = json.load(open('credential.json'))

subscription_key = credentials['API_KEY']
endpoint = credentials['ENDPOINT']

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


# Get an image with text
def recognize(FILE_PATH):
    read_image_path = FILE_PATH
    read_image = open(read_image_path, 'rb')
    # Call API with URL and raw response (allows you to get the operation location)

    read_response = computervision_client.read_in_stream(read_image, raw=True)

    # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Print the detected text, line by line
    correct_answer = ""
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                correct_answer += line.text + "\n"

    return correct_answer

if __name__ == '__main__':
    recognize('correct_answer.png')