import discord
import json
import os
import asyncio


class GuildData:
    def __init__(self, region: discord.VoiceRegion, logch: int):
        self.region = region
        if region == discord.VoiceRegion.south_korea:
            self.lang = "kor"
        else:
            self.lang = "eng"
        self.logch = logch


def JoinGuild(client: discord.Client, guild: discord.Guild):
    path = f"./data/guilds/{guild.id}.json"
    region: discord.VoiceRegion = guild.region
    lang = "eng"
    if region == discord.VoiceRegion.south_korea:
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
    if os.path.isfile(path):
        return None
    return JoinGuild(client, guild)


def ChangeLang(guild: discord.Guild, lang: str) -> None:
    path = f"./data/guilds/{guild.id}.json"
    l = lang.lower()
    l = (
        l.replace("korean", "kor")
        .replace("한국어", "kor")
        .replace("korea", "kor")
        .replace("한국", "kor")
        .replace("한국말", "kor")
    )
    if not l == "kor":
        l = "eng"
    with open(path, "r") as fp:
        d = fp.read()
    g = json.loads(d)
    g["lang"] = l
    with open(path, "w") as fp:
        fp.write(json.dumps(g))
    return


def Traffic(member: discord.Member):
    with open("./data/traffic/guilds.json", "r") as fp:
        g = json.load(fp)
    with open("./data/traffic/users.json", "r") as fp:
        u = json.load(fp)
    if not str(member.guild.id) in g:
        g[str(member.guild.id)] = 0
    if not str(member._user.id) in u:
        u[str(member._user.id)] = 0
    g[str(member.guild.id)] += 1
    u[str(member._user.id)] += 1
    with open("./data/traffic/guilds.json", "w") as fp:
        json.dump(g, fp)
    with open("./data/traffic/users.json", "w") as fp:
        json.dump(u, fp)
