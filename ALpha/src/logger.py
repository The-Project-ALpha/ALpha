import discord
import json
import random
import data


def get_channel(guild: discord.Guild):
    return guild.get_channel(data.get_log_channel(guild.id)), data.get_language(
        guild.id
    )


embed = discord.Embed


def member_join(guild, member) -> discord.Embed:
    lang = data.get_language(guild.id)
    emb = data.get_i18n(lang, "l_join")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"].format(),
        color=random.randint(0, 1677215),
    )
