import discord
import json
import os
import configparser


tg = dict
tu = dict
guild_json = dict

with open("./ALpha/data/traffic/guilds.json", "r") as fp:
    tg = json.load(fp)
with open("./ALpha/data/traffic/users.json", "r") as fp:
    tu = json.load(fp)
with open("./ALpha/data/guilds.json", "r") as fp:
    guild_json = json.load(fp)

kor = configparser.ConfigParser()
eng = configparser.ConfigParser()
kor.read("./ALpha/config/i18n/kor.ini", encoding="utf-8")
eng.read("./ALpha/config/i18n/eng.ini", encoding="utf-8")



def join_guild(guild: discord.Guild) -> str:
    global guild_json
    region: discord.VoiceRegion = guild.region
    lang = "eng"
    if region == discord.VoiceRegion.south_korea:
        lang = "kor"
    guild_json[str(guild.id)] = {"lang": lang, "logch": 0}
    return lang


def leave_guild(gid: int) -> None:
    global guild_json
    del guild_json[str(gid)]


def get_language(gid) -> str:
    global guild_json
    return guild_json[str(gid)]["lang"]


def check(guild: discord.Guild) -> str:
    global guild_json
    if str(guild.id) in guild_json:
        return
    return join_guild(guild)


def change_lang(gid, lang: str) -> None:
    global guild_json
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
    guild_json[str(gid)]["lang"] = l


def set_traffic(member: discord.Member):
    global tg, tu
    if not str(member.guild.id) in tg:
        tg[str(member.guild.id)] = 0
    if not str(member._user.id) in tu:
        tu[str(member._user.id)] = 0
    tg[str(member.guild.id)] += 1
    tu[str(member._user.id)] += 1


def get_log_channel(gid: int) -> int:
    return guild_json(str(gid))["logch"]


def get_i18n(lang: str, d: str) -> dict:
    global kor, eng
    dt = (kor if lang == "kor" else eng)[d]
    for k, v in dt.items():
        dt[k] = v.replace("[enter]", "\n").replace("[s]", "'").replace("[sh]", "#")
    return dt

def save():
    global tg, tu, guild_json
    print("Save")
    with open("./ALpha/data/traffic/guilds.json", "w") as fp:
        json.dump(tg, fp)
    with open("./ALpha/data/traffic/users.json", "w") as fp:
        json.dump(tu, fp)
    with open("./ALpha/data/guilds.json", "w") as fp:
        json.dump(guild_json, fp)
