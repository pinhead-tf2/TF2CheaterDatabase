import asyncio


async def clean_aliases(unclean_list: list):
    filtered_list = []

    for user in unclean_list:
        names_only = []
        for name in user:
            names_only.append(name["newname"])

        filtered_list.append(names_only)
    return filtered_list


async def main():
    test = [[{'newname': 'pinhead', 'timechanged': 'Jun 6 @ 11:50am'},
             {'newname': 'xX_c0ck_l0ver_Xx', 'timechanged': 'Jun 6 @ 11:50am'},
             {'newname': 'pinhead the sherpa', 'timechanged': 'Jun 6 @ 11:49am'},
             {'newname': 'pinheadtf2', 'timechanged': 'Jun 6 @ 11:49am'}]
            ]
    cleaned = await clean_aliases(test)
    print(cleaned[0])


if __name__ == '__main__':
    asyncio.run(main())
