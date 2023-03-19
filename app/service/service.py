# 這個多次呼叫時會爆掉 stack資料顯示可能為BUG
# from apscheduler.schedulers.background import BackgroundScheduler

# import the module to create a database engine
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import text  # import the module to execute SQL statements
from sqlalchemy.orm import sessionmaker
import json  # import the module to handle JSON data

url = "mysql+pymysql://root:root@localhost/AZAG_DB"  # define the database URL
engine = create_engine(url)  # create a database engine
metadata = MetaData()
# start session
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()  # connect to the database


def test_query_myTable():  # define a function to test query all data from MYTABLE
    sql = text("SELECT * FROM MYTABLE")  # write the SQL statement
    # execute the SQL statement and get the result set
    row = connection.execute(sql)
    results = row.fetchall()  # fetch all rows from the result set
    response = ""  # initialize an empty string for response
    for row in results:  # loop through each row in results
        # append each row as a string to response
        response = response + str(row)
    return response  # return the response


def query_myTable(name):  # define a function to query data from MYTABLE by name
    # write the SQL statement with name parameter
    sql = text(f"SELECT * FROM MYTABLE WHERE name='{name}'")
    # execute the SQL statement and get the result set
    row = connection.execute(sql)
    results = row.fetchall()  # fetch all rows from the result set
    response = ""  # initialize an empty string for response
    for row in results:
        response = response + str(row)
    return response


def getTemperature():
    import random
    value = round(random.uniform(10, 100), 2)
    return value

import threading
execFlag = True
def insertRecord(flag):
    if(not flag):
       return
    # table model
    DATALOGGER_table = Table('DATALOGGER', metadata, autoload_with=engine)
    # fetch data from sensor
    from datetime import datetime
    # get current date and time
    now = datetime.now()
    time_mark = now.strftime("%Y-%m-%d %H:%M:%S")
    value = getTemperature()
    print(f"insert data: Date:{time_mark}, Value: {value}")
    # create insert object and define values, commit change
    ins = DATALOGGER_table.insert().values(DATE=time_mark, TEMP=value)
    session.execute(ins)
    session.commit()
    loopSelf()

def loopSelf():
    global execFlag
    timer = threading.Timer(2, insertRecord, (execFlag,))
    timer.start()

def serviceStartRecord():
    global execFlag
    execFlag = True
    loopSelf()
    return "start success"

def serviceStopRecord():
    global execFlag
    execFlag = False
    return "record stop"


def serviceGetRecordData():
    from app.models.mytable import DATALOGGER
    # query all data from User table and order by ID in descending order 
    query = session.query(DATALOGGER).order_by(DATALOGGER.DATE.desc()) 
    results = query.limit(20).all()

    def rowData_to_dict(rowData): # define a function to convert a User object to a dictionary
        return {"ID": rowData.ID, "DATE": str(rowData.DATE), "TEMP": rowData.TEMP} # return a dictionary with the attributes of the user

    json_data = [rowData_to_dict(d) for d in results]
    return json_data


