---
title: Create a Flask app
nav_order: 4
permalink: /flask-app
---

# Create a Flask app

In this section we're going to create a barebones Flask app that returns an HTML file when users hit the root of our web app. Don't spend too much time trying to pick apart the code, we'll come back to update this file later in the workshop.

## What is a Flask route?

Before we continue, let's take a minute to talk about "[routes](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.route)". Routing is used to bind a URL to a specific function. Flask uses route decorators to register functions to specific URLs. For example, when a user navigates to the root (`/`) of our web app, `index.html` is rendered.  

```python
@app.route('/')
def index():
    return render_template('index.html')
```

Let's take a look at one more example to hammer this home.

```python
@app.route('/about')
def about():
    return render_template('about.html')
```

This code ensures that when a user navigates to `http://your-web-app.com/about` that the `about.html` file is rendered.

While these samples illustrate how to render html pages for a user, routes can also be used to call APIs when a button is pressed, or take any number of actions without having to navigate from the homepage. You'll see this in action when we create routes for translation, sentiment, and speech synthesis.

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

You should see a print out for a local server. Open a browser and navigate to that URL. You should see our single page app. However, none of the buttons work. That's because we haven't build routes for our API calls yet.

Press **Ctrl + c** to kill the application.

## Next

[Translate text](translate-text){: .btn .btn-green }
