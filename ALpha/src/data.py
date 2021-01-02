import csv
import discord
import json
import os
import configparser


tg = dict
tu = dict
guild_json = dict
black = dict

with open("./ALpha/data/traffic/guilds.json", "r", encoding="UTF8") as fp:
    tg = json.load(fp)
with open("./ALpha/data/traffic/users.json", "r", encoding="UTF8") as fp:
    tu = json.load(fp)
with open("./ALpha/data/guilds.json", "r", encoding="UTF8") as fp:
    guild_json = json.load(fp)
with open("./ALpha/data/black.json", "r", encoding="UTF8") as fp:
    black = json.load(fp)
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
    guild_json[str(guild.id)] = {"lang": lang, "logch": 0, "black": False}
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


def is_black_on(gid: int) -> bool:
    return guild_json[str(gid)]["black"]


def is_in_black(uid: int) -> bool:
    return str(uid) in black


def add_black(uid: int, reason: str, reporter: int) -> None:
    black[str(uid)] = {"reason": reason, "reporter": reporter}


def get_black_reason(uid: int) -> str:
    return black[str(uid)]["reason"]


def save():
    print("Save")
    with open("./ALpha/data/traffic/guilds.json", "w") as traffic_guild, open(
        "./ALpha/data/traffic/users.json", "w"
    ) as traffic_user, open("./ALpha/data/guilds.json", "w") as guild_data, open(
        "./ALpha/data/black.json", "w"
    ) as blacklist, open(
        "./ALpha/data/black.txt", "w"
    ) as black_readable:
        json.dump(tg, traffic_guild)
        json.dump(tu, traffic_user)
        json.dump(guild_json, guild_data)
        json.dump(black, blacklist)
        data = ""
        for key, value in black.items():
            data += f"================\nid:{key}\nreason:{value['reason']}\nreporter:{value['reporter']}\n================\n\n\n\n"
        black_readable.write(data)


def change_black_into_readable():
    data = ""
    for key, value in black.items():
        data += f"================\nid:{key}\nreason:{value['reason']}\nreporter:{value['reporter']}\n================\n\n\n\n"
    with open("./ALpha/data/black.txt", "w") as fp:
        fp.write(data)
    return


if __name__ == "__main__":
    change_black_into_readable()
save()
