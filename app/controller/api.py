# flask setting
from flask import Blueprint, request, render_template
api = Blueprint('api', __name__)
# allow CORS
from flask_cors import CORS
CORS(api)
# set response mimetype
from flask import Response

@api.route('/')
def catch_all():
    return render_template('index.html')

@api.route('/hello')
def hello():
    return 'Hello, World!'

@api.route('/version')
def version():
    # define response content-type
    return Response('v1.0', mimetype='text/plain')

@api.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return f'The sum of {a} and {b} is {a+b}.'

@api.route('/dbtest')
def dbtest():
    from app.service.service import test_query_myTable
    return test_query_myTable()

@api.route('/queryByName', methods=['POST'])
def queryByName():
    data = request.get_json()
    name = data.get('name')
    from app.service.service import query_myTable
    return query_myTable(name)