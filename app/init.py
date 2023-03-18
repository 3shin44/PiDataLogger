from flask import Flask
from app.controller.api import api
app = Flask(__name__)
app.register_blueprint(api)
