---
title: Setup your environment
nav_order: 3
permalink: /setup
---
# Let's setup your dev environment

Before we can build our Flask-based web app, we need to clone the project and install a few Python packages.

## Clone the project from GitHub

1. Open command line (Windows) or terminal (macOS/Linux). In your home directory, clone the project from GitHub:
   ```
   git clone https://github.com/erhopf/camp2019.git
   ```
2. Navigate to the project directory:
   ```
   cd camp2019
   ```

## Install virtualenv and enable your dev environment

**PyCharm Users:** Before you go any further, if you're using PyCharm, they've got great instructions for using a virtualenv within their IDE, [Configuring Virtualenv Environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html).

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
   ```
   virtualenv venv --python=Python3
   ```
   **Note**: We've explicitly declared that the virtual environment should use Python 3. This ensures that users with multiple Python installations are using the correct version.
3. The commands to activate your virtual environment will vary depending on if you are a Windows or macOS/Linux user.  

   **macOS/Linux:**
   ```
   source venv/bin/activate
   ```

   **Windows:**
   ```
   \venv\Scripts\activate
   ```
   After running this command, your command line or terminal session should be prefaced with `venv`.

   ![](./images/venv.png)

   You can deactivate the session at any time by typing this into the command line or terminal `deactivate`.

4. Install requests. This is a library used for HTTP requests.

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
   C:\path\to\app>set FLASK_APP=app.py
   ```

## Next

[Create a Flask app](flask-app){: .btn .btn-green }
