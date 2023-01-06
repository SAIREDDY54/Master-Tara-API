import os
import pymongo
from bson.json_util import dumps

session_id = ""

client = pymongo.MongoClient("mongodb://localhost:27017/master_tara")
change_streams = client.master_tara.Interfaces.watch([{
    '$match': {
        'operationType': { '$in': ['update'] }
    }
}])

def printSession():
    print("session id is",session_id)
    return session_id

for change in change_streams:
    # print(change['fullDocument']['interfaces'], change['fullDocument']['sessionId'], change['fullDocument']['status'])
    # print('') # for readability only
    # global session_id
    # session_id = change['fullDocument']['sessionId']
    # printSession()
    session_id = change
    printSession()
    break
