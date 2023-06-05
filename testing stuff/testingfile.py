import asyncio
import time
import json
from api.mongodb.connection_handler import insert_user, insert_multiple_users, create_user_collection, \
    create_user_collection_noschemarequirements


async def main():
    # await create_user_collection()
    # await create_user_collection_noschemarequirements()
    with open('testdata2.json') as json_file:
        await insert_user(json.load(json_file))


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.2f} seconds.")
