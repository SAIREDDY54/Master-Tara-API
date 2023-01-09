from flask import Flask, request
import pymongo

from flask_cors import CORS, cross_origin
import time
import threading
# from mongotriggers import MongoTrigger
# import change_stream as cd
from gridfs import GridFS
import json


app = Flask(__name__)
app.secret_key = "000d88cd9d90036ebdd237eb6b0db000"
cors = CORS(app, resources={r'*': {'origins':'*'}})

# conn_url = "mongodb://localhost:27017/" # your connection string

conn_url = "mongodb+srv://saikumar:saikumar@master-tara.2u3a4r1.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn_url)

# triggers = MongoTrigger(client)

grid_fs = GridFS(client.master_tara)

# print(client)
# Database = client.get_database('master_tara')

# sampleTable = Database.Interfaces
# print(client.changestream.sampleTable.insert_one)

# app.config['CORS_HEADERS'] = 'Content-Type', 'access-control-allow-origin'

interfaces = []
filePath = []
absPath = []
abs = []
userSession = ""
status = " "

def notify(op_document):
    print('added data to database')

def updateStatus():
    # Popen('python db_access.py')
    # triggers.register_update_trigger(notify, 'master_tara', 'Interfaces')
    # triggers.tail_oplog()
    updateQuery = client.master_tara.Interfaces.find_one_and_update({'sessionId': userSession}, {'$set': {"status":"processing"}})
    time.sleep(5)
    updateQuery = client.master_tara.Interfaces.find_one_and_update({'sessionId': userSession}, {'$set': {"status":"Completed"}})
    # triggers.stop_tail()
    


def getStatus():
    
    # print("status is", cd.printSession())
    change_stream = client.master_tara.Interfaces.watch([{
    '$match': {
        'operationType': { '$in': ['update'] }
        }
    }])

    for change in change_stream:
        global status
        # print(change['updateDescription']['updatedFields']['status'])
        status = change['updateDescription']['updatedFields']['status']
        
        print("Called from interfaces",status)
        # break
        time.sleep(1)
        break
    return status
    # return status
    


@app.route('/hello', methods=['GET'])
def home():
    return "Hello World"

@app.route('/upload', methods=['PUT'])
def upload(file_name):
    with grid_fs.new_file(filename = file_name) as fp:
        fp.write(request.data)
        file_id = fp._id
    
    if grid_fs.find_one(file_id) is not None:
        return json.dumps({'state': 'File Saved successfully'}), 200
    else:
        return json.dumps({'state': 'Error while saving'}), 500

# @app.route('/interfaces', methods=['POST'])
# # @cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type'])
# def getInterfaces():
#     global interfaces
#     interfaces = request.json["interfaces"]
#     print("pipe interfaces")
#     runAnotherFile()
#     pipe = win32pipe.CreateNamedPipe(
#         r'\\.\pipe\Foo',
#         win32pipe.PIPE_ACCESS_DUPLEX,
#         win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
#         1, 65536, 65536,
#         0,
#         None)
#     try:
#         print("waiting for client")
#         win32pipe.ConnectNamedPipe(pipe, None)
#         print("got client")

#         win32file.WriteFile(pipe, str.encode(f"{interfaces}"))
#         time.sleep(2)
#         win32file.WriteFile(pipe, str.encode(f"{sendFilePath()}"))
#         abs.clear()
#         # print(sendFilePath())
#         print("finished now")
#     finally:
#         win32file.CloseHandle(pipe)
#     return interfaces

@app.route('/interfaces', methods=['POST'])
@cross_origin(origin=['https://tara-api.onrender.com'])
def getInterfaces():
    print(client)
    global interfaces
    global userSession
    interfaces = request.json["interfaces"]
    userSession = request.json["sessionId"]
    # ls = json.loads(interfaces)
    # print(ls[0])

    queryObject = {
        'interfaces': interfaces,
        'sessionId': userSession,
        'status': "NEW"
    }
    # print("from global", getStatus())
    thread = threading.Thread(target=getStatus)
    thread.daemon = True
    thread.start()
    # print(client.master_tara.sampleTable.insert_one(queryObject).inserted_id)
    query = client.master_tara.Interfaces.insert_one(queryObject)
    
    updateStatus()
    
    
    # change_streams.close()
    print("pipe interfaces")
    
    
    
    # getStatus()
    

    # pipe = win32pipe.CreateNamedPipe(
    #     r'\\.\pipe\Foo',    
    #     win32pipe.PIPE_ACCESS_DUPLEX,
    #     win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
    #     1, 65536, 65536,
    #     0,
    #     None)
    # try:
    #     print("waiting for client")
    #     win32pipe.ConnectNamedPipe(pipe, None)
    #     print("got client")

    #     win32file.WriteFile(pipe, str.encode(f"{interfaces}"))
    #     abs.clear()
    #     # print(sendFilePath())
    #     print("finished now")
    # finally:
    #     win32file.CloseHandle(pipe)
    return interfaces



## <--- LINUX FILE UPLOAD FIFO --->
    # FIFO = '\mypipe'
    # os.mkfifo(FIFO)
    # # with open(FIFO) as fifo:
    # #     while True:
    # #         line = fifo.read()
    # # try:
    
    # # except OSError as e:
    # #     print("faile :%s" % e)
    # # else:
    # #     fifo = open(FIFO, 'w')
    # print("path created")
    # return interfaces
        


# @app.route('/filePath', methods=['POST'])
# # @cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type'])
# def getFilePath():
#     global filePath
#     global abs
#     filePath = request.json["filePath"]
#     abs.append(os.path.abspath(filePath))
#     return os.path.abspath(filePath)


# def sendFilePath():

#     return abs


def getInput():
    if (len(interfaces) > 0):
        return "YES"
    else:
        return "NO"

# def getStatus():
#     change_stream = client.master_tara.Interfaces.watch([{
#     '$match': {
#         'operationType': { '$in': ['update'] }
#         }
#     }])

#     for change in change_stream:
#         # print(change['updateDescription']['updatedFields']['status'])
#         status = change['updateDescription']['updatedFields']['status']
#         print(status)
#     return status

@app.route('/checkStatus', methods=['GET'])
@cross_origin(origin=['https://tara-api.onrender.com'])
def checkStatus():
    getStatus()
    return status
# # @cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type'])
# def checkStatus():
#     # change_stream = client.master_tara.Interfaces.watch([{
#     # '$match': {
#     #     'operationType': { '$in': ['update'] }
#     #     }
#     # }])

#     # for change in change_stream:
#     #     # print(change['updateDescription']['updatedFields']['status'])
#     #     global status
#     #     status = change['updateDescription']['updatedFields']['status']
#     if getStatus() == "processing":
#         return "YES"
#     else:
#         return "FALSE"


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=8080, threaded=True)
    # Thread(target=app.run).start()
