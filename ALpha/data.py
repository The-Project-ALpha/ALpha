import discord
import json
import os
import asyncio


def join_guild(guild: discord.Guild):
    path = f"./data/guilds/{guild.id}.json"
    region: discord.VoiceRegion = guild.region
    lang = "eng"
    if region == discord.VoiceRegion.south_korea:
        lang = "kor"
    data = {"lang": lang, "logch": 0}
    with open(path, "w") as fp:
        fp.write(json.dumps(data))
    return lang


def leave_guild(gid):
    path = f"./data/guilds/{gid}.json"
    os.remove(path)


def __get_json(gid) -> dict:
    path = f"./data/guilds/{gid}.json"
    with open(path, "r") as fp:
        data = json.load(fp)
    return data


def __edit_json(gid, af) -> None:
    path = f"./data/guilds/{gid}.json"
    with open(path, "w") as fp:
        fp.write(str(af))


def get_language(gid) -> str:
    return __get_json(gid)["lang"]


def check(guild: discord.Guild):
    path = f"./data/guilds/{guild.id}.json"
    if os.path.isfile(path):
        return None
    return join_guild(guild)


def change_lang(gid, lang: str) -> None:
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
    g = __get_json(gid)
    g["lang"] = l
    __edit_json(gid, g)
    return


def set_traffic(member: discord.Member):
    with open("./data/traffic/guilds.json", "r") as fp:
        g = json.load(fp)
    with open("./data/traffic/users.json", "r") as fp:
        u = json.load(fp)
    if not str(member.guild.id) in g:
        g[str(member.guild.id)] = 0
    if not str(member._user.id) in u:
    g[str(member.guild.id)] += 1
    u[str(member._user.id)] += 1
    with open("./data/traffic/guilds.json", "w") as fp:
        json.dump(g, fp)
    with open("./data/traffic/users.json", "w") as fp:
        json.dump(u, fp)


def get_log_channel(gid: int) -> int:
    return __get_json(gid)["logch"]
