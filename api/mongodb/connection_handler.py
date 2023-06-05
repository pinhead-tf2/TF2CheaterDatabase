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


async def create_user_collection():
    client = await create_connection()
    cheaterDatabase = client.cheaterDatabase
    await cheaterDatabase.create_collection("userList", validator={
        "title": "userList",
        "required": [
            "_id",
            "date",
            "username",
            "cheatData"
        ],
        "properties": {
            "_id": {
                "bsonType": "string",
                "title": "User ID",
                "description": "Holds the Steam3 ID of an entered user. Is a primary key. Required."
            },
            "date": {
                "bsonType": "date",
                "title": "Addition Date",
                "description": "Holds a MongoDB Date that represents the date and time that the data was added. Required."
            },
            "username": {
                "bsonType": "string",
                "title": "Username",
                "description": "The current username of a given user, obtained via Steam API. Required."
            },
            "aliases": {
                "bsonType": "array",
                "title": "Aliases",
                "description": "All past aliases of the user, obtained via Steam API.",
                "items": {
                    "bsonType": "string"
                }
            },
            "friends": {
                "bsonType": "array",
                "title": "Friends",
                "description": "The current friends of the user, obtained via Steam API.",
                "items": {
                    "bsonType": "string"
                }
            },
            "cheatData": {
                "bsonType": "object",
                "title": "Cheat Data",
                "description": "An object that contains what the user is logged as, reasons why if they're not innocent, and optional evidence links to prove they cheat. Required entries: flag, isBot.",
                "required": [
                    "flag",
                    "isBot"
                ],
                "properties": {
                    "flag": {
                        "bsonType": "string",
                        "title": "Flag",
                        "description": "What level of suspicion the user is at. Required."
                    },
                    "isBot": {
                        "bsonType": "bool",
                        "title": "Is Bot",
                        "description": "A simple boolean to say if the user is a bot. Required."
                    },
                    "infractions": {
                        "bsonType": "array",
                        "title": "Infractions",
                        "description": "All possible or confirmed infractions/cheats the user has demonstrated employing. Should only be filled out if the flag is suspicious or cheater.",
                        "items": {
                            "bsonType": "string"
                        }
                    },
                    "evidence": {
                        "bsonType": "array",
                        "title": "Evidence",
                        "description": "All evidence that is used to prove the user is a cheater. Not required, heavily encouraged.",
                        "items": {
                            "bsonType": "string"
                        }
                    }
                }
            },
            "overrideName": {
                "bsonType": "string",
                "title": "Custom Name",
                "description": "Overrides the username when displayed on any data visualizer or displayer. Should be used if a cheater changes their name often."
            }
        }
    })


async def create_user_collection_noschemarequirements():
    client = await create_connection()
    cheaterDatabase = client.cheaterDatabase
    await cheaterDatabase.create_collection("agony", validator={
        "title": "agony",
        "properties": {
            "_id": {
                "bsonType": "string",
                "title": "User ID",
                "description": "Holds the Steam3 ID of an entered user. Is a primary key. Required."
            },
            "date": {
                "bsonType": "date",
                "title": "Addition Date",
                "description": "Holds a MongoDB Date that represents the date and time that the data was added. Required."
            },
            "username": {
                "bsonType": "string",
                "title": "Username",
                "description": "The current username of a given user, obtained via Steam API. Required."
            },
            "aliases": {
                "bsonType": "array",
                "title": "Aliases",
                "description": "All past aliases of the user, obtained via Steam API.",
                "items": {
                    "bsonType": "string"
                }
            },
            "friends": {
                "bsonType": "array",
                "title": "Friends",
                "description": "The current friends of the user, obtained via Steam API.",
                "items": {
                    "bsonType": "string"
                }
            },
            "cheatData": {
                "bsonType": "object",
                "title": "Cheat Data",
                "description": "An object that contains what the user is logged as, reasons why if they're not innocent, and optional evidence links to prove they cheat. Required entries: flag, isBot.",
                "properties": {
                    "flag": {
                        "bsonType": "string",
                        "title": "Flag",
                        "description": "What level of suspicion the user is at. Required."
                    },
                    "isBot": {
                        "bsonType": "bool",
                        "title": "Is Bot",
                        "description": "A simple boolean to say if the user is a bot. Required."
                    },
                    "infractions": {
                        "bsonType": "array",
                        "title": "Infractions",
                        "description": "All possible or confirmed infractions/cheats the user has demonstrated employing. Should only be filled out if the flag is suspicious or cheater.",
                        "items": {
                            "bsonType": "string"
                        }
                    },
                    "evidence": {
                        "bsonType": "array",
                        "title": "Evidence",
                        "description": "All evidence that is used to prove the user is a cheater. Not required, heavily encouraged.",
                        "items": {
                            "bsonType": "string"
                        }
                    }
                }
            },
            "overrideName": {
                "bsonType": "string",
                "title": "Custom Name",
                "description": "Overrides the username when displayed on any data visualizer or displayer. Should be used if a cheater changes their name often."
            }
        }
    })


async def insert_user(data: dict):
    userList = await get_user_collection(await create_connection())
    try:
        userList.insert_one(data)
    except Exception as e:
        print(e)


async def insert_multiple_users(data: [dict]):
    userList = await get_user_collection(await create_connection())
    try:
        userList.insert_many(data)
    except Exception as e:
        print(e)
