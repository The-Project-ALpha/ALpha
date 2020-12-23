import discord
from enum import Enum


class Command(Enum):
    none = 1
    helpme = 2
    hello = 3
    restart = 4
    langset = 5


def GetCommand(client: discord.client, msg: discord.Message) -> Command:
    if msg.content == client.user.mention or msg.content == "~help":
        return Command.helpme
    if not msg.content.startswith("~"):
        return Command.none
    mc = msg.content
    mcl = mc.lower()
    mcs = mc.split()
    mcsl = list()
    a = 0
    for i in mcs:
        mcsl[i] = i.lower()
        a += 1
    if mcl == "~restart" and msg.author.id == 418023987864403968:
        return Command.restart
    if mcl == "~hello":
        return Command.hello
    if (
        mcsl[0] == "~set" and (not len(mcsl) == 1)
    ) and msg.author.guild_permissions.administrator:
        if mcsl[1] == "lang":
            return Command.langset
