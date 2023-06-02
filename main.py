import asyncio
import time
import json

from api.mongodb.connection_handler import insert_user, insert_multiple_users


async def main():
    with open('testdata.json') as json_file:
        print(await insert_user(json.load(json_file)))


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.2f} seconds.")
