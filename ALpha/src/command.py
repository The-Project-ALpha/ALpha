import discord
from enum import Enum


class Command(Enum):
    none = 1
    helpme = 2
    hello = 3
    restart = 4
    langset = 5
    _exec = 6
    info = 7

    kick = 10
    ban = 11
    mute = 12
    clear = 13


def GetCommand(client: discord.client, msg: discord.Message) -> Command:
    if msg.content == client.user.mention or msg.content == "~help":
        return Command.helpme
    if not msg.content.startswith("~"):
        return Command.none
    mc = msg.content
    mcl = mc.lower()
    mcs = mc.split()
    mcsl = mcs[:]
    a = 0

    for i in mcs:
        mcsl[a] = i.lower()
        a += 1
    if mcl == "~restart" and msg.author.id == 418023987864403968:
        return Command.restart
    if mcl == "~info":
        return Command.info
    if mcsl[0] == "~exec" and msg.author.id == 418023987864403968:
        return Command._exec
    if mcl == "~hello":
        return Command.hello
    if (
        mcsl[0] == "~set" and (not len(mcsl) == 1)
    ) and msg.author.guild_permissions.administrator:
        if mcsl[1] == "lang":
            return Command.langset
    if (
        mcsl[0] == "~kick"
        and (not len(mcsl) == 1)
        and msg.author.guild_permissions.kick_members
    ):
        return Command.kick
    if (
        mcsl[0] == "~ban"
        and (not len(mcsl) == 1)
        and msg.author.guild_permissions.ban_members
    ):
        return Command.ban
    if (
        mcsl[0] == "~mute"
        and (not len(mcsl) == 1)
        and msg.author.guild_permissions.manage_roles
    ):
        return Command.mute
    if (
        mcsl[0] == "~clear"
        and (not len(mcsl) == 1)
        and msg.author.guild_permissions.manage_messages
    ):
        return Command.clear
    return Command.none