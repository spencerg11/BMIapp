from flask import Flask

app = flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

