---
title: Challenge: Computer Vision
nav_order: 4
parent: Extra credit
permalink: /deploy
---

# Learn how to deploy your app to Azure

Now that you've built and app and have access to the code, how would you leverage the Computer Vision API to get the text from an image and translate it?

## Resources

* [Recognize printed and handwritten text](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/concept-recognizing-text#ocr-optical-character-recognition-api)
* [Quickstart: OCR](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-print-text)

## Some code to get you started

Here's a Flask route to get you started.

```python
@app.route('/ocr')
def ocr_image():
    image_url = request.args.get('image', default='', type=str)
    response = ocr.get_ocr(image_url)
    return jsonify(response)
```

And here's some python to hit the OCR service.

```python
import os, requests, uuid, json

## You'll need a key for the computer vision service.
if 'COMPUTER_VISION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_KEY']
else:
    print('Environment variable for COMPUTER_VISION_KEY is not set.')
    exit()

## An image URL is passed to this function and a JSON response is returned.
def get_ocr(url):
    image_url = url
    base_url = 'https://westus.api.cognitive.microsoft.com/'
    path = 'vision/v2.0/ocr'
    params = {
        'language': 'unk',
        'detectOrientation': 'true',
    }
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = {
        "url" : image_url
    }
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response
```

## Next steps

* How will you provide the image URL through your app?
* How will you parse the JSON response?
* What information returned is important to your user?

Good luck!
