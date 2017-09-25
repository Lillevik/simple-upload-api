from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
app.config.from_object("config")
CORS(app)

import views

if not os.path.isdir("uploads"):
    os.makedirs("uploads")

