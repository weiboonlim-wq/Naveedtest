from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return app.send_static_file("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
