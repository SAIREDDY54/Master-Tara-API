# lst= [["usb","ble", "hello"], "TARA*5a7ls03o622ocjaneo3g"]
# lst=str(lst)
# lst2=[]
# stri=""
# for i in range(len(lst)):
#     if lst[i].isalpha() or lst[i] == '*' or lst[i].isnumeric():
#         stri=stri+lst[i]
#     elif lst[i]=="," or lst[i]=="]":
#         lst2.append(stri)
#         stri=""

# while("" in lst2):
#     lst2.remove("")

# print(lst2)
import pymongo

job_queue = []
conn_url = "mongodb://localhost:27017/" # your connection string
client = pymongo.MongoClient(conn_url)

change_streams = client.master_tara.Interfaces.watch([{
    '$match': {
        'operationType': { '$in': ['insert'] }
        }
    }])

for change in change_streams:
    job_queue.append(change['fullDocument']['interfaces'])
    
    job_queue.insert(0, change['fullDocument']['sessionId'])
    
    tmp_queue = []
    string = ""
    for i in range(len(str(job_queue))):
        if str(job_queue)[i].isalpha() or str(job_queue)[i] == '*' or str(job_queue)[i].isnumeric():
            string=string+str(job_queue)[i]
        elif str(job_queue)[i]=="," or str(job_queue)[i]=="]":
            tmp_queue.append(string)
            string=""

    while("" in tmp_queue):
        tmp_queue.remove("")
    print(tmp_queue)
    job_queue.clear()