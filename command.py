import discord
from enum import Enum


class Command(Enum):
    none = 1
    helpme = 2
    hello = 3


def GetCommand(client: discord.client, msg: discord.Message) -> Command:
    if (msg.content == client.user.mention or "~help"):
        return Command.helpme
    if (not msg.content.startwith("~")):
        return Command.none
    mc = msg.content
    mcs = mc.split()
