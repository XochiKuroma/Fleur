# botconfig.json

owners_uids: A list of users who are "bot owners." Bot owners have full control of the bot.
botid: The running bot's user ID.

# serverID.json

verified: Verification roles, for gated servers. If not used, leave empty. Provide as role names, caps sensitive. If no role name is passed as an argument to .verify, slot 0 will be granted by default.

lockdown: Role for .lockdown command, which essentially jails a user. Should be high in role heirarchy and restrictive at channel level permissions.

-- Fleur will reference these channels in automated messages and actions. All values should be channel IDs, or 0 if unused. --

ruleschan: Channel ID for rules channel. Fleur will direct users here to read the rules.
general: Channel ID for general chat channel. Fleur will announce verified arrivals here.
greetchan (COG: greet.py): Channel ID for landing channel. Fleur will greet users with the greeting preamble and await verification. 

colorchan (COG: customcolor.py): Primary channel ID where members should use the customcolor command. Fleur will direct users to this channel, but the command will be restricted to channels listed below, in colorchannels.
roleschan (COG: roles.py): Channel ID where members should apply roles to themselves.

chanlog: Channel ID where channel parameter edits should be logged.
msglog: Channel ID where message edits/deletions should be logged.
rolelog: Channel ID where role additions/removals from members should be logged.
usrlog: Channel ID where user (global profile) changes should be logged.
cmdlog: Channel ID where ran commands should be logged.

noimagechannels: Channels where no attachments are permitted. All attachments will be immediately deleted.
nologchannels: Channels omitted from all logging.
colorchannels: Channels to restrict the color command to.

emojikeys: Keyword/Emoji pairs
Adds emoji reactions to messages if the contents match a regex.
Ex: "aw+oo": 123456789012345678
