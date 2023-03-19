from flask import Flask
from app.controller.api import api
app = Flask(__name__, template_folder='../templates', static_folder='../templates')
app.register_blueprint(api)
