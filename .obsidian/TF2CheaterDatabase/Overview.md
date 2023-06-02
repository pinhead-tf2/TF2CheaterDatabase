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
![[MCDbotpreview.png]]
![[MCDgraphpreview.png]]

# Database
Uses: MongoDB
- Can be converted to JSON for website displaying
	- Allows for easy downloading

Stores:
- User Data
	- Username `String`
	- Aliases `String[]`
	- SteamID64 `int`
	- Friends' SteamID64 `int[]`
- Cheater Data
	- Suspicion level `String[Innocent, Watched, Suspicious, Cheater]`
		- Suspicious, Cheater
			- Infractions/cheat types `String[]`
			- Optional evidence URL `String[]`
- Custom Data
	- Override username `String`

# Steam API
Interface to get:
- User data
	- Current username
	- Profile picture `(Discord bot)`
	- Aliases
	- VAC Status
	- Friends