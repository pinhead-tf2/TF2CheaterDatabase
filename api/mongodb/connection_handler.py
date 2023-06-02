from os import getenv
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

load_dotenv()

# protects login + database
uri = f"mongodb+srv://{getenv('MONGODB_USERNAME')}:{getenv('MONGODB_PASSWORD')}" \
      f"@{getenv('MONGODB_DATABASE')}.mongodb.net/?retryWrites=true&w=majority"


async def create_connection():
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)


async def get_user_collection(client):
    cheaterDatabase = client.cheaterDatabase
    userList = cheaterDatabase.userList
    return userList


async def insert_user(data: dict):
    userList = await get_user_collection(await create_connection())
    try:
        result = userList.insert_one(data)
        return result
    except Exception as e:
        print(e)


async def insert_multiple_users(data: [dict]):
    userList = await get_user_collection(await create_connection())
    try:
        result = userList.insert_many(data)
        return result
    except Exception as e:
        print(e)
