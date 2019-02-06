---
title: Analyze sentiment
nav_order: 6
permalink: /analyze-sentiment
---

# Analyze sentiment

Sentiment Analysis is a function of the [Text Analytics API](https://docs.microsoft.com/azure/cognitive-services/Text-Analytics/overview). Provide raw text to the API, and it is analyzed for clues about positive or negative sentiment. The closer a score is to `1` indicates positive sentiment, while scores closer to `0` indicate negative sentiment. A score of `0.5` is considered neutral.

In our Flask app, we're going to analyze the sentiment scores for the source text and translation output. Who knows, maybe we'll see some results where source text is positive and the translation is negative.

Just like the last section, we're going to:

1. Write some Python code to call the Sentiment Analysis API.
2. Create a Flask route that accepts `POST` requests. When users hit the button to analyze sentiment in your web app, it will send data, in this case the input and translated text to this route.
3. Test the analyze sentiment button. Don't worry, for this workshop we've taken care of the Javascript code that listens for button presses. We're not going to cover this code in the workshop, but if you're interested, see `main.js`.

## Build a request to analyze sentiment

Open `sentiment.py` in your IDE or text editor. Then copy in this code block. Make sure to add your **Cognitive Services** subscription key and save.

```python
import os, requests, uuid, json

# Don't forget to replace with your Cog Services subscription key!
# If you prefer to use environment variables, see Extra Credit for more info.
subscription_key = "YOUR_COG_SERVICES_SUBSCRIPTION_KEY_GOES_HERE"

# Our Flask route will supply four arguments: input_language,
# input_text, output_language, and output_text. When the analyze sentiment
# button is pressed in our Flask app, the Ajax request will grab these
# values from our web app, and use them in the request. See main.js
# for Ajax calls.
def get_sentiment(input_text, input_language, output_text, output_language):
    base_url = 'https://westus.api.cognitive.microsoft.com/text/analytics'
    path = '/v2.0/sentiment'
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    # Each object must have a unique identifier.
    body = {
        "documents": [
            {
                "language": input_language,
                "id": "1",
                "text": input_text
            },
            {
                "language": output_language,
                "id": "2",
                "text": output_text
            }
        ]
    }
    response = requests.post(constructed_url, headers=headers, json=body)
    # Convert the response to JSON and make it available to our web app.
    return response.json()
```

Let's take a look at the code. For our web app, we're passing two sets of data to the Sentiment Analysis API. The first for the input text, the second for the translated text. The data is sent as an array of objects, each requiring the language code, a unique identifier, and the actual text. You'll notice that we've hard coded the unique identifier, however, the other data is pulled from our app.

The response is a simple JSON object, which our web app will parse and display for the user with some nifty Javascript. As mentioned earlier, we're not going to discuss the Javascript in this workshop, but feel free to take a look at `main.js` to see how the data is used.

## Add a Flask route

Now that you have some code to call the Sentiment Analysis API using data from the translation request, we need to create another route in our Flask app that accepts `POST` requests. We're going to call this route when a user presses the analyze sentiment button in your web app.

Locate the import statements at the top of `app.py` and update the line that reads `import translate` to:

```python
import translate, sentiment
```

Now our Flask app can use the method available via `sentiment.py`.

Next, copy this code to the end of `app.py`:

```python
@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    input_text = data['inputText']
    input_lang = data['inputLanguage']
    output_text = data['outputText']
    output_lang =  data['outputLanguage']
    response = sentiment.get_sentiment(input_text, input_lang, output_text, output_lang)
    return jsonify(response)
```

You'll notice that this route is very similar to what we created for translation. The key callout is that these four values are passed to the `get_sentiment()` method: `input_text`, `input_lang`, `output_text`, and `output_lang`.

`input_lang` and `output_text` are values returned by the translation request.

## Test sentiment analysis

Let's test sentiment analysis in our web app.

1. Go ahead and run:
   ```
   flask run
   ```
2. Navigate to the provided server address.
3. Type text into the input area, select a language, and press translate. You should get a translation.
4. Next, press **Run sentiment analysis**. If it works, you should see sentiment scores for the input and output language.

If you have any trouble, let us know. Otherwise, press **CTRL + c** to kill the application and head to the next step.

## Next

[Synthesize speech](text-to-speech){: .btn .btn-green }
