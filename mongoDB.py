import pymongo

conn_url = "mongodb://localhost:27017/master_tara" # your connection string
client = pymongo.MongoClient(conn_url)

Database = client.get_database('master_tara')

sampleTable = Database.Interfaces