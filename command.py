import discord
from enum import Enum


class Command(Enum):
    none = 1
    helpme = 2
    hello = 3
    restart = 4


def GetCommand(client: discord.client, msg: discord.Message) -> Command:
    if (msg.content == client.user.mention or msg.content == "~help"):
        return Command.helpme
    if (not msg.content.startswith("~")):
        return Command.none
    mc = msg.content
    mcs = mc.split()
    if (mc == "~restart" and msg.author.id == 418023987864403968):
        return Command.restart
    if (mc == "~hello"):
        return Command.hello
