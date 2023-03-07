from flask import Flask, jsonify, request
import pymongo

from flask_cors import CORS
import time
import threading
import bcrypt

app = Flask(__name__)
app.secret_key = "000d88cd9d90036ebdd237eb6b0db000"
CORS(app)

conn_url = "mongodb://localhost:27017/"  # your connection string

# conn_url = "mongodb+srv://saikumar:saikumar@master-tara.2u3a4r1.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn_url)

interfaces = []
awsCloud = []
azureCloud = []
DBAssets = []
filePath = []
absPath = []
abs = []

db_password = ""
userSession = ""
status = " "


def updateStatus():
    updateQuery = client.master_tara.Interfaces.find_one_and_update(
        {'sessionId': userSession}, {'$set': {"status": "processing"}})
    time.sleep(5)
    updateQuery = client.master_tara.Interfaces.find_one_and_update(
        {'sessionId': userSession}, {'$set': {"status": "Completed"}})
    # triggers.stop_tail()


def getStatus():

    # print("status is", cd.printSession())
    change_stream = client.master_tara.Interfaces.watch([{
        '$match': {
            'operationType': {'$in': ['update']}
        }
    }])

    for change in change_stream:
        global status
        # print(change['updateDescription']['updatedFields']['status'])
        status = change['updateDescription']['updatedFields']['status']

        print("Called from interfaces", status)
        # break
        time.sleep(1)
        break
    return status

# @app.route('/upload', methods=['PUT'])
# def upload(file_name):
#     with grid_fs.new_file(filename = file_name) as fp:
#         fp.write(request.data)
#         file_id = fp._id

#     if grid_fs.find_one(file_id) is not None:
#         return json.dumps({'state': 'File Saved successfully'}), 200
#     else:
#         return json.dumps({'state': 'Error while saving'}), 500


@app.route('/addData', methods=['POST'])
# @cross_origin(origin=['https://flask-two.vercel.app'])
def getInterfaces():
    global interfaces
    global userSession
    global awsCloud
    global azureCloud
    global DBAssets

    interfaces = request.json["interfaces"]
    awsAssets = request.json["awsAssets"]
    azureAssets = request.json["azureAssets"]
    DBAssets = request.json["DBAssets"]
    userSession = request.json["sessionId"]
    email = request.json["email"]

    queryObject = {
        'interfaces': interfaces if len(interfaces) > 0 else "",
        'awsAssets': awsAssets if len(awsAssets) > 0 else "",
        'azureAssets': azureAssets if len(azureAssets) > 0 else "",
        'DBAssets': DBAssets if len(DBAssets) > 0 else "",
        'sessionId': userSession,
        'status': "NEW"
    }
    thread = threading.Thread(target=getStatus)
    thread.daemon = True
    thread.start()
    query = client.master_tara.Interfaces.insert_one(queryObject)

    updateStatus()

    return interfaces


def hash_password(password):
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password.decode('utf-8')


@app.route('/registerUser', methods=['POST'])
def uploadUserData():
    mail = request.json['mail']
    password = request.json['password']
    pass_hash = hash_password(password)

    if client.master_tara.UserData.find_one({"email": mail}):
        return jsonify({'error': 'Email already exists'}), 400
    else:
        query = {
            'email': mail,
            'password': pass_hash
        }

        client.master_tara.UserData.insert_one(query)

        return jsonify({"message": "Data has been successfully uploaded"}), 201


@app.route('/loginUser', methods=['POST'])
def loginUser():
    email = request.json['mail']
    password = request.json['password'].encode('utf-8')

    user = client.master_tara.UserData.find_one({'email': email})

    if user is None:
        return jsonify({"message": "Email not found"}), 404
    else:
        db_password = user.get('password')
        
        if bcrypt.hashpw(password, db_password.encode('utf-8')) == db_password.encode('utf-8'):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Incorrect password"}), 401

# <--- LINUX FILE UPLOAD FIFO --->
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


def getInput():
    if (len(interfaces) > 0):
        return "YES"
    else:
        return "NO"


@app.route('/checkStatus', methods=['GET'])
# @cross_origin(origin=['https://flask-two.vercel.app'])
def checkStatus():
    getStatus()
    return status


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=8080, threaded=True)
    # Thread(target=app.run).start()