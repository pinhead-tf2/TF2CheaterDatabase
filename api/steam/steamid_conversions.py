# All of this code is credited to bcahue of GitHub
# https://gist.github.com/bcahue/4eae86ae1d10364bb66d

baseSID64 = 76561197960265728

def steam3id_to_steamid32(steam3id):
    for ch in ['[', ']']:
        if ch in steam3id:
            steam3id = steam3id.replace(ch, '')
    steam3id_split = steam3id.split(':')
    steamid32 = ['STEAM_0:']
    z = int(steam3id_split[2])
    if z % 2 == 0:
        steamid32.append('0:')
    else:
        steamid32.append('1:')
    steamAccount = z // 2
    steamid32.append(str(steamAccount))
    return ''.join(steamid32)


def steam3id_to_steamid64(steam3id):
    for ch in ['[', ']']:
        if ch in steam3id:
            steam3id = steam3id.replace(ch, '')
    steam3id_split = steam3id.split(':')
    steamid64 = int(steam3id_split[2]) + baseSID64
    return str(steamid64)


def steamid64_to_steam3id(steamid64):
    steam3id = ['[U:1:']
    steamIDAccount = int(steamid64) - baseSID64

    steam3id.append(str(steamIDAccount) + ']')

    return ''.join(steam3id)
