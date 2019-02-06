---
title: Translate text
nav_order: 5
permalink: /translate-text
---

# Translate text

The [Translator Text API](https://docs.microsoft.com/azure/cognitive-services/translator/translator-info-overview) is a neural machine translation service that developers can easily integrate into their applications websites, tools, or any solution requiring multi-language support such as website localization, e-commerce, customer support, messaging applications, internal communication, and more.

In this section we're going to do a few things:

1. Write some Python code to call the Translator Text API.
2. Create a Flask route that accepts `POST` requests. When users hit the translate button in your web app, it will send data, like the text you want to translate and the selected language to this route.
3. Test the translate button. Don't worry, for this workshop we've taken care of the Javascript code that listens for button presses. We're not going to cover this code in the workshop, but if you're interested, see `main.js`.

## Build a request to translate text

Open `translate.py` in your IDE or text editor and copy in this code.

Make sure to add your **Cognitive Services** subscription key and save. Don't forget, if you're using our keys, they're available on the [prerequisites](prerequisites) page.

```python
import os, requests, uuid, json

# Don't forget to replace with your Cog Services subscription key!
# If you prefer to use environment variables, see Extra Credit for more info.
subscription_key = "YOUR_COG_SERVICES_SUBSCRIPTION_KEY_GOES_HERE"

# Our Flask route will supply two arguments: text_input and language_output.
# When the translate text button is pressed in our Flask app, the Ajax request
# will grab these values from our web app, and use them in the request.
# See main.js for Ajax calls.
def get_translation(text_input, language_output):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=' + language_output
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        #If your Cog Services key is another region, change this!!
        'Ocp-Apim-Subscription-Region': 'westus',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        "text" : text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()
```

The function that we've created only requires two arguments: `text_input` and `language_output`. The `text_input` is provided by the text area in our HTML, and the `language_output` is from the language selector drop-down in our HTML.

## Add a Flask route

Let's create a route in our Flask app that accepts `POST` requests. We're going to call this route when a user presses the translate button in your web app.

First, locate the import statement at the top of `app.py` and add the following line:

```python
import translate
```

Now our Flask app can use the method available via `translate.py`.

Then, copy this code to the end of `app.py`:


```python
@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    response = translate.get_translation(text_input, translation_output)
    return jsonify(response)
```

There are a few things in this code snippet I'd like to call out before we continue, since you'll see similar things in the following sections.

1. We're restricting this route to only accept `POST` requests. This is because we need data from our web application to complete the request.
2. We're using `request.get_json()` to manage the request object. For translation, the request will include two JSON key/value pairs: `text` and `to`. The text to translate and the output language respectively.
3. We're assigning data from the request to variables. Then passing these variables to the `get_translation()` method we just created.
4. Finally, we're handling the response. In this case the translation output. When our web app calls this route, this is the datat that will be used to populate the translation text area, and provide the value of the identified language.

## Test your web app

Let's test translation in our web app. Go ahead and run:
```
flask run
```

Navigate to the provided server address. Type text into the input area, select a language, and press translate. You should get a translation. If it doesn't work, let us know. Otherwise, press **CTRL + c** to kill the app, then head to the next step.

## Next

[Analyze sentiment](analyze-sentiment){: .btn .btn-green }
