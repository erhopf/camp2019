from flask import Flask, render_template, url_for, jsonify, request
import translate, synthesize, sentiment, sys

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')
