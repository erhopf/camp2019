---
title: Setup your environment
nav_order: 3
permalink: /setup
---
# Let's setup your dev environment

Before we can build our Flask-based web app, we need to clone the project and install a few Python packages.

## Clone the project from GitHub

This repository is a skeleton for the project. The Python files are empty -- we'll be adding code throughout this tutorial. However, the `index.html` and `main.js` are ready for you from the start.

1. Open command line (Windows) or terminal (macOS/Linux). In your home directory, clone the project from GitHub:
   ```
   git clone https://github.com/erhopf/camp2019.git
   ```
2. Navigate to the project directory:
   ```
   cd camp2019
   ```

## Install virtualenv and enable your dev environment

1. Now that we've cloned the project, we need to install some dependencies. First, let's install `virtualenv`. This is an isolated development environment that allows you to install packages for testing without impacting the entire system. Run:
   ```
   pip install virtualenv
   ```
   Now, let's make sure everything is working. Run:
   ```
   virtualenv --version
   ```
   The version should be printed to terminal. Anything else means that something went wrong. Let us know, we're here to help!

2. Next, let's create a virtual environment for our project. Run:

   **macOS/Linux:**
   ```
   virtualenv venv --python=python3
   ```
   We've explicitly declared that the virtual environment should use Python 3. This ensures that users with multiple Python installations are using the correct version.

   **Windows CMD / Windows Bash:**
   ```
   virtualenv venv
   ```
   Make sure that your virtualenv is using Python 3x. If you're virtualenv was created with Python 2.7.x, please see [Troubleshooting](troubleshooting).

3. The commands to activate your virtual environment will vary depending on if you are a Windows or macOS/Linux user.  

   **macOS/Linux:**
   ```
   source venv/bin/activate
   ```

   **Windows CMD:**
   ```
   venv\Scripts\activate
   ```

   **Windows Bash:**

   ```
   source venv/Scripts/activate
   ```

   After running this command, your command line or terminal session should be prefaced with `venv`.

   ![](./images/venv.png)

   You can deactivate the session at any time by typing this into the command line or terminal `deactivate`.

## Install requests

Requests is a popular module that is used to send HTTP 1.1 requests. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. If you'd like to know more, I encourage you to [check out their site](http://docs.python-requests.org/en/master/).

```
pip install requests
```

## Install and configure Flask

1. Next we need to install Flask. Flask is the micro framework that we'll use to build our web app. It handles the routing, and allows us to make server-to-server calls that hide our subscription keys from the end user. To install Flask, run:
   ```
   pip install Flask
   ```
   Let's make sure Flask was installed. Run:
   ```
   flask --version
   ```
   The version should be printed to terminal. Anything else means that something went wrong. Let us know, we're here to help!

2. To run the flask app you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal which app to work with by exporting the `FLASK_APP` environment variable:

   **macOS/Linux**:
   ```
   export FLASK_APP=app.py
   ```

   **Windows**:
   ```
   set FLASK_APP=app.py
   ```

## Next

[Create a Flask app](flask-app){: .btn .btn-green }
