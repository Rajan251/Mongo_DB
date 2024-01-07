import pymongo

#Provide the Mongodb localhots url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/")

#Database Name
dataBase = client["test"]

#collection Name 
collection = dataBase['Products']

# sample Data 
d = {'companyName':'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment '
}

# Insert above records in the collection
rec = collection.insert_one(d)

#Lets Verify  all the record at once Present  in the recorder with all the fields
all_record = collection.find()

# Printing all records Present in the collection
for idx, record in enumerate(all_record):
    print(f"{idx}:{record}")


# Second_Lab

import pymongo

dbconn = pymongo.MongoClient("mongodb://localhost:27017/")

dbname = 'ineuron'

db=dbconn[dbname]


# to find all the database name.
dbconn.list_database_names()