---
title: Create a Flask app
nav_order: 4
permalink: /flask-app
---

# Create a Flask app

In this section we're going to create a barebones Flask app that returns an HTML file when users hit the root of our web app. Don't spend too much time trying to pick apart the code, we'll come back to update this file later in the workshop.

## Get started

First, open `app.py` in your IDE or text editor. This file is included in the repository you cloned during setup. Then copy and paste this code block and save.

```python
from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')
```

This code block tells my app to display `index.html` whenever a user navigates to the root. Let's try it out. Run:

```
flask run
```

You should see a print out for a local server. Open a browser and navigate to that URL. You should see our single page app. However, none of the buttons work. That's because we need to build the requests to each of the Cognitive Services.

Press **Ctrl + c** to kill the application.

## Next

[Translate text](translate-text){: .btn .btn-green }
