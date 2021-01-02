import discord
from enum import Enum


class Command(Enum):
    NONE = 1
    HELP = 2
    HELLO = 3
    RESTART = 4
    LANGSET = 5
    EXEC = 6
    INFO = 7

    KICK = 10
    BAN = 11
    MUTE = 12
    CLEAR = 13

    BLACKLIST = 20


def GetCommand(client: discord.client, msg: discord.Message) -> Command:
    if msg.content == client.user.mention or msg.content == "~help":
        return Command.HELP
    if not msg.content.startswith("~"):
        return Command.NONE
    mc = msg.content
    mcl = mc.lower()
    mcs = mc.split()
    mcsl = mcs[:]
    a = 0

    for i in mcs:
        mcsl[a] = i.lower()
        a += 1
    if mcl == "~restart" and msg.author.id == 418023987864403968:
        return Command.RESTART
    if mcl == "~info":
        return Command.INFO
    if mcsl[0] == "~exec" and msg.author.id == 418023987864403968:
        return Command.EXEC
    if mcl == "~hello":
        return Command.HELLO
    if (
        mcsl[0] == "~set" and (not len(mcsl) == 1)
    ) and msg.author.guild_permissions.administrator:
        if mcsl[1] == "lang":
            return Command.LANGSET
    if (
        mcsl[0] == "~kick"
        and (not len(mcsl) == 1)
    ):
        return Command.KICK
    if (
        mcsl[0] == "~ban"
        and (not len(mcsl) == 1)
        and msg.author.guild_permissions.ban_members
    ):
        return Command.BAN
    if (
        mcsl[0] == "~mute"
        and (not len(mcsl) == 1)
        and msg.author.guild_permissions.manage_roles
    ):
        return Command.MUTE
    if (
        mcsl[0] == "~clear"
        and (not len(mcsl) == 1)
        and msg.author.guild_permissions.manage_messages
    ):
        return Command.CLEAR
    if(mcl == "~black list"):
        return Command.BLACKLIST
    return Command.NONE
