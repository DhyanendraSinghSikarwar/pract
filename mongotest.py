import pymongo

client = pymongo.MongoClient("mongodb+srv://dhyanendra:dhyanendra@cluster0.ghllth2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"Dhyanendra",
    "surname": "Singh",
    "email": "dhyanendra@gmail.com"
}
db1= client['mongotest']
coll = db1['test1']
coll.insert_one(d)