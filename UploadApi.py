from flask import Flask
import os

app = Flask(__name__)
app.config.from_object("config")

import views

if not os.path.isdir("uploads"):
    os.makedirs("uploads")

