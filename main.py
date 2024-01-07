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

collection_name ='mongo_demo'

collection=db[collection_name]

collection

my_row = {'Serial No': '9998',
          'GRE Score':'337',
          'TOEFL Score': '118',
          'University Rating':'4',
          'SOP':'4.5',
          'LOR':'4.5',
          'CGPA':'9.65',
          'Research':'1',
          'Chance of Admit': '0.92'

}

col=collection.insert_one(my_row)

col.inserted_id

res =collection.find()

# Extract Data From DB
for i in res:
    print(i)

#List of the Doc
my_rows=[{'Serial No': '9999',
          'GRE Score':'337',
          'TOEFL Score': '118',
          'University Rating':'4',
          'SOP':'4.5',
          'LOR':'4.5',
          'CGPA':'9.66',
          'Research':'1',
          'Chance of Admit': '0.92'

},{'Serial No': '10000',
          'GRE Score':'337',
          'TOEFL Score': '118',
          'University Rating':'4',
          'SOP':'4.5',
          'LOR':'4.5',
          'CGPA':'9.67',
          'Research':'1',
          'Chance of Admit': '0.92'

}]  

# insert many row data using list
res =collection.insert_many(my_rows)

res =collection.find # Fetch Data From DB