from sqlalchemy import create_engine
from sqlalchemy import text
import json

url = "mysql+pymysql://root:root@localhost/AZAG_DB"
engine = create_engine(url)
connection = engine.connect()

def test_query_myTable():
    sql = text("SELECT * FROM MYTABLE")
    row = connection.execute(sql)
    results = row.fetchall()
    response = ""
    for row in results:
        response = response + str(row)
    return response

def query_myTable(name):
    sql = text(f"SELECT * FROM MYTABLE WHERE name='{name}'")
    row = connection.execute(sql)
    results = row.fetchall()
    response = ""
    for row in results:
        response = response + str(row)
    return response
