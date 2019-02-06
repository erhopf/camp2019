---
title: Synthesize speech
nav_order: 7
permalink: /text-to-speech
---

# Synthesize speech (text-to-speech)

The [Text-to-Speech API](https://docs.microsoft.com/azure/cognitive-services/speech-service/text-to-speech) allows an app or service to convert text into human-sounding speech. Today, this service supports 75+ voices in more than 45 languages/locales.

Our Flask app is going to use the Text-to-Speech API to convert our translation output into audio for playback in the browser.

You may feel like you've read this spiel before...you have. Just in case you skipped ahead, here's what we're going to do in this section:

1. Write some Python code to convert text-to-speech using Speech Services.
2. Create a Flask route that accepts `POST` requests. When users hit the button to convert text-to-speech in your web app, it will send data, in this case text and the selected voice for synthesized speech.
3. Test the convert text-to-speech button. Don't worry, for this workshop we've taken care of the Javascript code that listens for button presses. We're not going to cover this code in the workshop, but if you're interested, see `main.js`.

## Build a request to synthesize speech

Open `synthesize.py` in your IDE or text editor and copy in this code.

Make sure to add your **Speech Services** subscription key and save. Don't forget, if you're using our keys, they're available on the [prerequisites](prerequisites) page.

```python
import os, requests, time
from xml.etree import ElementTree

# Don't forget to replace with your Speech Services subscription key!
# If you prefer to use environment variables, see Extra Credit for more info.
subscription_key = "YOUR_SPEECH_SERV_SUBSCRIPTION_KEY_GOES_HERE"

# Our Flask route will supply two arguments: input_text and voice_font.
# When the convert text-to-speech button is pressed in our Flask app,
# the XHR request will grab these values from our web app, and use them in
# to construct the SSML body of the request. See main.js to review the
# XHR request.
class TextToSpeech(object):
    def __init__(self, input_text, voice_font):
        self.subscription_key = subscription_key
        self.input_text = input_text
        self.voice_font = voice_font
        self.timestr = time.strftime('%Y%m%d-%H%M')
        self.access_token = None

    # This method exchanges a subscription key for an access token. Access
    # tokens for Speech Services REST endpoints are valid for 10 minutes.
    # Our app is currently setup to exchange on each request.
    def get_token(self):
        fetch_token_url = 'https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken'
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    # This method calls the text-to-speech endpoint. The body of the request is
    # SSML and contains the input_text and the voice used for speech synthesis.
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
        return response.content
```

There's a lot going on in this code block compared to translation and sentiment. Since the text-to-speech endpoint requires an access token, the subscription key must be exchanged for a token before we can synthesize speech. So, we've created a class with two methods.

* `get_token()` - Performs the token exchange. Once called, this token is valid for 10 minutes.
* `save_audio()` - Calls the text-to-speech endpoint using the access token.

Unlike translation and sentiment, which have JSON message bodies, speech synthesis uses [Speech Synthesis Markup Language (SSML)](https://docs.microsoft.com/azure/cognitive-services/speech-service/speech-synthesis-markup). SSML is an XML-based markup language that allows you to choose a voice, and control volume, pronunciation and prosody of text-to-speech.

In this sample, we've used `ElementTree` to construct the SSML. The `input_text` and `voice_font` are provided by the web app; and the body is encoded as UTF-8.

## Add a Flask route

Let's create another route in our Flask app that accepts `POST` requests. We're going to call this route when a user presses the convert text-to-speech button in your web app.

Locate the import statements at the top of `app.py` and update the line that reads `import translate, sentiment` to:

```python
import translate, sentiment, synthesize
```

Now our Flask app can use the method available via `synthesize.py`.

Then, copy this code to the end of `app.py`:

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

Unlike the first two routes that return JSON data, this call will return binary audio data. If you take a look at the `main.js` file (included in the repository), you'll notice that the response is written to a blob, then loaded for playback. It also uses [XMLHttpRequest (XHR)](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) instead of [Ajax](http://api.jquery.com/jquery.ajax/), due to limitations handling binary data.

## Test speech synthesis

Let's test speech synthesis in our web app.

1. Go ahead and run:
   ```
   flask run
   ```
2. Navigate to the provided server address.
3. Type text into the input area, select a language, and press translate. You should get a translation. If it doesn't work, let us know.
4. A voice should be auto selected based on your previous selection, however, feel free to experiment with different voices. Then click convert text-to-speech.
5. When the audio file is ready, you should be able to press play and listen to the synthesized text.

That's it. You've got a working Flask app that translates text, analyzes sentiment, and converts text-to-speech.

Press **Ctrl + c** to kill the application.

## Next

[Extra credit and helpful links](extra-credit){: .btn .btn-green }
