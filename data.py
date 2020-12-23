import discord
import json
import os


class GuildData:
    def __init__(self, region: discord.VoiceRegion):
        self.region = region
        if (region == discord.VoiceRegion.south_korea):
            self.lang = "kor"
        else:
            self.lang = "eng"
        self.logch = 0


def JoinGuild(guild: discord.Guild):
    path = f"./data/guilds/{guild.id}.json"
    region: discord.VoiceRegion = guild.region
    data = GuildData(region)
    with open(path, "w") as fp:
        fp.write(json.dumps(data))


def LeaveGuild(guild: discord.Guild):
    path = f"./data/guilds/{guild.id}.json"
    os.remove(path)

