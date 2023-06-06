import aiohttp
import aiosqlite

from api.steam.query_steam_profile import get_user_aliases
from api.general.cleaners import clean_aliases


async def mark_innocent(db: aiosqlite.Connection, session: aiohttp.ClientSession, user: str, accuser: int):
    aliases = await clean_aliases(await get_user_aliases(session, [user]))
    cursor = await db.execute(f'''
            INSERT INTO user_list
            (id, accuser, username, aliases, friends)
            VALUES (
                {user},
                {accuser},
                {"steamusernamequery"},
                {aliases[0]},
                {"steamfriendsquery"}
            )
        ''')
    return True if cursor.lastrowid == 1 else False


async def mark_cheater(db, user: str, accuser: int, cheat_types: list[str] | None, evidence_links: list[str] | None):
    cursor = await db.execute(f'''
                INSERT INTO user_list
                (id, accuser, username, aliases, friends, flag, cheat_types, evidence_links)
                VALUES (
                    {user},
                    {accuser},
                    {"steamusernamequery"},
                    {"steamaliasesquery"},
                    {"steamfriendsquery"},
                    {"cheater"},
                    {cheat_types},
                    {evidence_links}
                )
            ''')
    return True if cursor.lastrowid == 1 else False


async def mark_bot(db, user: str, accuser: int, bot_owner: str):
    cursor = await db.execute(f'''
            INSERT INTO user_list
            (id, accuser, username, aliases, friends, flag, cheat_types, bot_owner)
            VALUES (
                {user},
                {accuser},
                {"steamusernamequery"},
                {"steamaliasesquery"},
                {"steamfriendsquery"},
                {"bot"},
                {["aimbot", "cathook", "walls", "spam"]},
                {bot_owner}
            )
        ''')
    return True if cursor.lastrowid == 1 else False


async def manual_mark(db, user: str, accuser: int, mark: str,
                         cheat_types: list[str] | None, evidence_links: list[str] | None,
                         bot_owner: str | None):
    cursor = await db.execute(f'''
                INSERT INTO user_list
                (id, accuser, username, aliases, friends, flag, cheat_types, evidence_links, bot_owner)
                VALUES (
                    {user},
                    {accuser},
                    {"steamusernamequery"},
                    {"steamaliasesquery"},
                    {"steamfriendsquery"},
                    {mark},
                    {cheat_types},
                    {evidence_links},
                    {bot_owner}
                )
            ''')
    return True if cursor.lastrowid == 1 else False
