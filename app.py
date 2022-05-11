from flask import Flask, url_for, jsonify, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/test')
def test():
    return f"Index is at: {url_for('index')}"

@app.route('/json')
def json():
    return jsonify({
        'index': url_for('index', _external=True),
        "self": url_for('json', _external=True)
    })

@app.route('/redirect')
def redir():
    return redirect(url_for('index'))
