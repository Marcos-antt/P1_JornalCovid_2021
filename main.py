##from application import app
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> helllowwww </h1>'







