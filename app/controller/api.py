# flask setting
from flask import Blueprint, request, render_template
api = Blueprint('api', __name__)
# allow CORS
from flask_cors import CORS
CORS(api)
# set response mimetype
from flask import Response

from app.service.service import *

@api.route('/')
def catch_all():
    return render_template('index.html')

@api.route('/version')
def version():
    # define response content-type
    return Response('v1.0', mimetype='text/plain')

@api.route('/startRecord', methods=['get'])
def startRecord():
    serviceStartRecord()
    return Response("start success", mimetype='text/plain')

@api.route('/stopRecord', methods=['get'])
def stopRecord():
    serviceStopRecord()
    return "record stop"

@api.route('/getRecordData', methods=['get'])
def getRecordData():
    return serviceGetRecordData()