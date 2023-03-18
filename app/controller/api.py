from flask import Blueprint, request, render_template

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return render_template('index.html')

@api.route('/hello')
def hello():
    return 'Hello, World!'

@api.route('/version')
def version():
    return 'v1.0'

@api.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return f'The sum of {a} and {b} is {a+b}.'