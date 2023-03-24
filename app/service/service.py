# get sensor measure data
def getTemperature():
    import random
    value = round(random.uniform(10, 100), 2)
    return value

import threading
execFlag = True
def insertRecord(flag):
    if(not flag):
       return
    # fetch data from sensor
    from datetime import datetime
    # get current date and time
    now = datetime.now()
    time_mark = now.strftime("%Y-%m-%d %H:%M:%S")
    value = getTemperature()
    print(f"insert data: Date:{time_mark}, Value: {value}")
    loopSelf()

# 再度執行 insertRecord(寫入紀錄)
def loopSelf():
    global execFlag
    timer = threading.Timer(1, insertRecord, (execFlag,))
    timer.start()

# 啟動記錄服務
def serviceStartRecord():
    global execFlag
    execFlag = True
    loopSelf()
    return "start success"

# 停止記錄服務
def serviceStopRecord():
    global execFlag
    execFlag = False
    return "record stop"

# 獲取現存紀錄值
def serviceGetRecordData():
    
    return json_data

import csv
def writeToCSV():
    
    with open('DataLogger', 'a', newline='') as file:
        writer = csv.writer(file)
        from datetime import datetime
        now = datetime.now()
        time_mark = now.strftime("%Y-%m-%d %H:%M:%S")
        value = getTemperature()
        print(f"insert data: Date:{time_mark}, Value: {value}")
        writer.writerow([time_mark, value])

# check DataLogger.csv is exist
def checkCSVFile():
    from os.path import exists
    file_exists = exists("DataLogger.csv")
    if(not file_exists):
        print("create file")
        open("DataLogger.csv", "x").close()
checkCSVFile()