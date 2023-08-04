import pymongo

#Connect to database
conn = "mongobd://localhost:27017"
client = pymongo.MongoClient(conn)

#connect to collection (if using MongoDB)
db = client.DBNAME
user_defined_variable = db.COLLECTIONNAME
#API call - get the data needed

#Insert data into database

COLLECTIONNAME.insert_many(
    [
        {

        }
    ]
    
)

#Print to terminal to check working
print("Data Uploaded")