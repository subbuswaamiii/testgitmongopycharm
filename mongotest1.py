import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb:ineuron2020@cluster0.gnseh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


### example dictionary ##

d = {   "name": "subodh", "email": "subodh@gmail.com", "surname":"mhatre"   }
# create varible db1 #
db1 = client['mongotest']
# create another variable #
coll = db1['test']
coll.insert_one(d)