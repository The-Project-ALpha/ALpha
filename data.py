import discord
import json
import os
import asyncio


class GuildData:
    def __init__(self, region: discord.VoiceRegion, logch: int):
        self.region = region
        if (region == discord.VoiceRegion.south_korea):
            self.lang = "kor"
        else:
            self.lang = "eng"
        self.logch = logch


def JoinGuild(client: discord.Client, guild: discord.Guild):
    path = f"./data/guilds/{guild.id}.json"
    region: discord.VoiceRegion = guild.region
    lang = "eng"
    if (region == discord.VoiceRegion.south_korea):
        lang = "kor"
    data = {"lang": lang, "logch": 0}
    with open(path, "w") as fp:
        fp.write(json.dumps(data))
    return lang


def LeaveGuild(guild: discord.Guild):
    path = f"./data/guilds/{guild.id}.json"
    os.remove(path)


def GetLang(guild: discord.Guild) -> str:
    path = f"./data/guilds/{guild.id}.json"
    with open(path, "r") as fp:
        d = fp.read()
    g = json.loads(d)
    return g["lang"]


def Check(client: discord.Client, guild: discord.Guild):
    path = f"./data/guilds/{guild.id}.json"
    if (os.path.isfile(path)):
        return None
    return JoinGuild(client, guild)
