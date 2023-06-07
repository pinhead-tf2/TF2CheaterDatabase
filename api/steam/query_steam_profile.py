import aiohttp
import asyncio
from os import getenv
from dotenv import load_dotenv
from steamid_conversions import steam3id_to_steamid64

load_dotenv()
STEAM_API_KEY = str(getenv("STEAM_API_KEY"))


async def api_call_generic(session: aiohttp.ClientSession, call_type: str, steam3ids: list[str]):
    match call_type:
        case "GetFriendList" | "GetPlayerBans":
            version = "v1"
        case "GetPlayerSummaries":
            version = "v2"
        case _:
            return "you fucked up, son"

    steamid64s = []
    for s3id in steam3ids:
        steamid64s.append(steam3id_to_steamid64(s3id))

    if call_type == "GetFriendList":
        players = []

        for query in steamid64s:
            response_friend = await session.get(f'https://api.steampowered.com/ISteamUser/GetFriendList/{version}/',
                                                params={
                                                    'key': STEAM_API_KEY,
                                                    'steamid': query
                                                })
            print(await response_friend.text())
            responseJSON = await response_friend.json()
            players.append(responseJSON["friendslist"]["friends"])

        return players
    else:
        async with session.get(f'https://api.steampowered.com/ISteamUser/{call_type}/{version}/',
                               params={
                                   'key': STEAM_API_KEY,
                                   'steamids': ','.join(steamid64s)
                               }) as response:
            responseJSON = await response.json()
            return responseJSON['response']['players']


async def get_user_aliases(session: aiohttp.ClientSession, steam3ids: list[str]):
    # hey, i don't have to convert ids this time!
    players = []

    for s3id in steam3ids:
        async with session.get(f'https://steamcommunity.com/profiles/{s3id}/ajaxaliases') as response:
            responseJSON = await response.json()
            players.append(responseJSON)

    return players


async def main():
    async with aiohttp.ClientSession() as session:
        arr = ["[U:1:858409410]"]
        # print(await get_user_aliases(session, arr))
        print(await api_call_generic(session, "GetPlayerSummaries", arr))


if __name__ == '__main__':
    asyncio.run(main())
