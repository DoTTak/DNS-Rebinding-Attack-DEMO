import json
from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>localhost(127.0.0.1)</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)