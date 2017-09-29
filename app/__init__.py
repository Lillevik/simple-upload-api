import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object("config")
CORS(app)

if not os.path.isdir("uploads"):
    os.makedirs("uploads")

from . import views
