from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# protects login + database
uri = f"mongodb+srv://{getenv('MONGODB_USERNAME')}:{getenv('MONGODB_PASSWORD')}" \
      f"@{getenv('MONGODB_DATABASE')}.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

cheaterDatabase = client["cheaterDatabase"]
userList = cheaterDatabase["userList"]

schema = {
    '_id': {
        'type': '$numberLong',
        'minlength': 17,
        'maxlength': 17,
        'required': True
    }
}

testdata = {
    "_id": {"$numberLong": "76561198818675138"},
    "username": "pinhead",
    "aliases": [
        "pinhead",
        "pinhead the sherpa"
    ],
    "friends": [
        {"$numberLong": "76561199007223827"}
    ],
    "cheatData": {
        "flag": "innocent",
        "infractions": [],
        "evidence": []
    },
    "overrideName": "pinhead"
}
