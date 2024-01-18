from pymongo import MongoClient

client = MongoClient("localhost",27017)

db = client["google"]
employees = db["employees"]

employees.insert_one({
    "id": "0",
    "name":"XYZ"

})