# The Main Goal:
To make a database that houses a master cheater list that:
- Interacts with Steam's API
- Is easily accessible
- Can be edited smoothly
- Is able to be visualized via web browser
- Can interface with pazer's bot detector
- Can interface with discord bots for ease of access

# References
https://megascatterbomb.com/mcd
![[MCDgraphpreview.png]]

# Database
Uses: MongoDB
- Can be converted to JSON for website displaying
	- Allows for easy downloading

## Stores
Permissions List
- id `INTEGER: Discord UID`

Cheater Data
- id `TEXT: Steam3ID`
- flag `TEXT CHECK(flag IN ("innocent", "watched", "suspicious", "cheater", "bot"))`
- cheatTypes `TEXT`
- evidenceLinks `TEXT: json_array("url1", "url2")`

User List
- id `TEXT: Steam3ID` 
- dateAdded `INTEGER`
- dateUpdated `INTEGER`
- updatee `Relational: Permissions List`
- overrideName `TEXT`
- username `TEXT`
- aliases `TEXT: json_array()`
- friends `TEXT: json_array()`
- cheaterData `Relational: Cheater Data`

Stores:
- User Data
	- Username `String`
	- Aliases `String[]`
	- SteamID64 `int`
	- Friends' SteamID64 `int[]`
- Cheater Data
	- Flag `String[Innocent, Watched, Suspicious, Cheater]`
		- Suspicious, Cheater
			- Infractions/cheat types `String[]`
			- Optional evidence URL `String[]`
- Custom Data
	- Override username `String`

# Steam API
https://partner.steamgames.com/doc/webapi/ISteamUser#GetPlayerSummaries
https://partner.steamgames.com/doc/webapi/ISteamUser#GetFriendList
Interface to get:
- User data
	- Current username
	- Profile picture `(Discord bot)`
	- Aliases
	- VAC Status
	- Friends

# Discord
Uses: Primary interface for actions on the database

## Features
#### Searches
- Find user by name
- Find user by Steam3ID
- Find all users with current username or past aliases 
- Mass search users by pasting `status` output into channel
- Select user from search if multiple

#### Selections
![[MCDbotpreview.png]]
- Show profile info 
	- Username (Should be refreshed)
	- Aliases (Should be refreshed)
	- Hacks
	- Evidence URLs
	- VAC Status
	- Friends (Should be refreshed)
	- Database Update Info
	- SteamIDs (Converted before creation using steam3id_converter.py)
- Controls
	- Marks
		- Cheater
		- Suspicious
		- Remove mark
		- Innocent
	- Modify 
		- Cheats
		- Evidence