import discord
import json
import random
import data


def get_channel(guild: discord.Guild):
    return guild.get_channel(data.get_log_channel(guild.id)), data.get_language(
        guild.id
    )


embed = discord.Embed


def message_delete(message: discord.Message) -> discord.Embed:
    emb = data.get_i18n(data.get_language(message.guild.id), "lmd")
    return embed(
        title=emb["TITLE"],
        description="",
        color=random.randint(0, 1677215),
    )


def bulk_message_delete(messages: discord.Message) -> discord.Embed:
    emb = data.get_i18n(data.get_language(messages[0].guild.id), "lbmd")
    return embed(
        title=emb["TITLE"],
        description="",
        color=random.randint(0, 1677215),
    )


def message_edit(bf: discord.Message, af: discord.Message) -> discord.Embed:
    emb = data.get_i18n(data.get_language(bf.guild.id), "lmj")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def reaction_add(reaction: discord.Reaction, member: discord.Member) -> discord.Embed:
    emb = data.get_i18n(data.get_language(member.guild.id), "lra")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def reaction_remove(
    reaction: discord.Reaction, member: discord.Member
) -> discord.Embed:
    emb = data.get_i18n(data.get_language(member.guild.id), "lrr")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def reaction_clear(
    reactions: discord.Reaction, member: discord.Member
) -> discord.Embed:
    emb = data.get_i18n(data.get_language(member.guild.id), "lrc")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def guild_channel_delete(channel: discord.abc.GuildChannel) -> discord.Embed:
    emb = data.get_i18n(data.get_language(channel.guild.id), "lgcd")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )
