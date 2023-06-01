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
