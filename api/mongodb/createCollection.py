from connection_handler import createConnection


def create_collection(collection_name):
    client = createConnection()
    db = client.cheaterDatabase
    result = db.create_collection(collection_name, validator={
        "title": "userList",
        "description": "Holds the data for each user in the cheater database",
        "required": [
            "_id",
            "date",
            "username",
            "cheatData"
        ],
        "properties": {
            "_id": {
                "bsonType": "long",
                "title": "User ID",
                "description": "Holds the SteamID64 of an entered user. Is a primary key. Required."
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
                    "bsonType": "long"
                }
            },
            "cheatData": {
                "bsonType": "object",
                "title": "Cheat Data",
                "description": "An object that contains what the user is logged as, reasons why if they're not innocent, and optional evidence links to prove they cheat. Required entries: flag, isBot.",
                "required": [
                    "flag, isBot"
                ],
                "properties": {
                    "flag": {
                        "bsonType": "string",
                        "title": "Flag",
                        "description": "What level of suspicion the user is at. Required.",
                        "enum": [
                            "innocent",
                            "watched",
                            "suspicious",
                            "cheater"
                        ]
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

    print(result)
