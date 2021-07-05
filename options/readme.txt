debug: Whether the bot should print full stacktraces for normal exceptions: `True`, or be nice and only print small messages: `False` (the default).

owners_uids: A list of users who are "bot owners." Bot owners have full control of the bot.

staff: Guild staff roles in order of lowest to highest authority.
Slot 1: A role all staff members have. If none, make this the same value as Slot 2.
Slot 2: A role that low level staff have.
Slot 3: A role that high level staff have.
Slot 4: A role that owner(s) of a server have.

verified: Verification roles, for gated servers. May be left blank if not used. Slot 0 will be granted if no role name is passed as an argument.

lockdown: Role for lockdown. Should be high in role heirarchy and restrictive at channel level permissions.

Fleur will reference these channels in automated messages. All values should be IDs.

ruleschan: Channel ID for rules channel. Fleur will direct users here to read the rules.
general: Channel ID for general chat channel. Fleur will announce verified arrivals here.
greetchan: Channel ID for landing channel. Fleur will greet users with the greeting preamble and await verification.

colorchan: Channel ID where members should use the customcolor command.
roleschan: Channel ID where members should apply roles to themselves.

chanlog: Channel ID where channel parameter edits should be logged.
msglog: Channel ID where message edits/deletions should be logged.
rolelog: Channel ID where role additions/removals from members should be logged.
usrlog: Channel ID where user (global profile) changes should be logged.
cmdlog: Channel ID where ran commands should be logged.
watchlog: Channel ID where watched user logs should be copied to.

noimagechannels: Channels where no attachments are permitted. All attachments will be immediately deleted.
nologchannels: Channels omitted from all logging.
colorchannels: Channels to restrict the color command to.

emojikeys: Keyword/Emoji pairs
Adds emoji reactions to messages if the contents match a regex.
Ex: "aw+oo": 123456789012345678

repterm, rep, cept: Reputation triggers
Gives a user 1 reputation point if a message contains an @ and a matching term.
repterm: The term to use for rep.
rep: Words that trigger rep.
cept: Words caught by rep that should be ignored.