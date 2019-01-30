---
layout: default
title: Synthesize speech
nav_order: 7
permalink: /text-to-speech
---

# Synthesize speech (text-to-speech)

You may feel like you've read this spiel before...you have. Just in case you skipped ahead, here's what we're going to do in this section:

1. Write some Python code to convert text-to-speech using Speech Services.
2. Create a Flask route that accepts `POST` requests. When users hit the button to convert text-to-speech in your web app, it will send data, in this case text and the selected voice for synthesized speech.
3. Test the convert text-to-speech button. Don't worry, for this workshop we've taken care of the Javascript code that listens for button presses. We're not going to cover this code in the workshop, but if you're interested, see `main.js`.

## Build a request to synthesize speech

```python
import os, requests, time
from xml.etree import ElementTree

# The Cognitive Services key won't work here.
subscription_key = "YOUR_SPEECH_SERV_SUBSCRIPTION_KEY_GOES_HERE"

class TextToSpeech(object):
    def __init__(self, input_text, voice_font):
        self.subscription_key = subscription_key
        self.input_text = input_text
        self.voice_font = voice_font
        self.timestr = time.strftime('%Y%m%d-%H%M')
        self.access_token = None

    # This function performs the token exchange.
    # The TTS endpoint requires an access token. Access tokens expire
    # in 10 minutes.
    def get_token(self):
        fetch_token_url = 'https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken'
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    # This function calls the TTS endpoint with the access token.
    def save_audio(self):
        base_url = 'https://westus.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'YOUR_RESOURCE_NAME',
        }
        # Here, ElementTree is used to build the SSML request.
        # This request is populated with data from a dropdown in the HTML.
        # Specifically, the voice selected for speech output.
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
        voice.set('name', 'Microsoft Server Speech Text to Speech Voice {}'.format(self.voice_font))
        voice.text = self.input_text
        # The body must be encoded as UTF-8 to handle non-ascii characters.
        body = ElementTree.tostring(xml_body, encoding="utf-8")

        response = requests.post(constructed_url, headers=headers, data=body)
        # Write the response as a wav file for playback. The file is located
        # in the same directory where this sample is run.
        print(response)
        return response.content
```

## Add a Flask route

Let's create another route in our Flask app that accepts `POST` requests. We're going to call this route when a user presses the convert text-to-speech button in your web app.

Locate the import statements at the top of `app.py` and update the line that reads `import translate, sentiment` to:

```python
import translate, sentiment, synthesize, sys
```

Now our Flask app can use the method available via `synthesize.py`.

Then copy this code into `app.py` below your translation route:

```python
@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text_input = data['text']
    voice_font = data['voice']
    tts = synthesize.TextToSpeech(text_input, voice_font)
    tts.get_token()
    audio_response = tts.save_audio()
    return audio_response
```

You'll notice that this route is very similar to what we've created for translation and sentiment. This request takes two arguments: `text_input` and `voice_font`. Here, `text_input` is the translation result, and `voice_font` is the voice selected from the drop-down menu in your web app.

Unlike the first two routes that return JSON data, this call will return binary audio data. If you take a look at the `main.js` file (included in the repository), you'll notice that the response is written to a blob, then loaded for playback. It also uses XMLHttpRequest instead of AJAX, due to limitations handling binary data.

## Test speech synthesis

Let's test speech synthesis in our web app. Go ahead and run:

```
flask run
```

Navigate to the provided server address. Type text into the input area, select a language, and press translate. You should get a translation. If it doesn't work, let us know. A voice should be auto selected based on your previous selection, however, feel free to experiment with different voices. Then click convert text-to-speech. When the audio file is ready, you should be able to press play and listen to the synthesized text.

That's it. You've got a working Flask app that translates text, analyzes sentiment, and converts text-to-speech.

Press **Ctrl + c** to kill the application.

## Next

[Extra credit and helpful links](extra-credit){: .btn .btn-green }
