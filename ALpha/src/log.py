import discord
import random
import data


def get_channel(guild: discord.Guild) -> discord.TextChannel:
    return guild.get_channel(data.get_log_channel(guild.id)) if data.get_log_channel(guild.id) is not 0 else None


embed = discord.Embed


def message_delete(message: discord.Message) -> discord.Embed:
    emb = data.get_i18n(data.get_language(message.guild.id), "lmd")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def bulk_message_delete(messages: discord.Message) -> discord.Embed:
    emb = data.get_i18n(data.get_language(messages[0].guild.id), "lbmd")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
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


def guild_channel_delete(channel) -> discord.Embed:
    emb = data.get_i18n(data.get_language(channel.guild.id), "lgcd")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def guild_channel_create(channel) -> discord.Embed:
    emb = data.get_i18n(data.get_language(channel.guild.id), "lgcc")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def guild_channel_update(
    before, aefore
) -> discord.Embed:
    emb = data.get_i18n(data.get_language(before.guild.id), "lgcu")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def member_join(member: discord.Member):
    emb = data.get_i18n(data.get_language(member.guild.id), "lmj")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def member_remove(member: discord.Member):
    emb = data.get_i18n(data.get_language(member.guild.id), "lmr")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def member_update(before: discord.Member, after: discord.Member):
    emb = data.get_i18n(data.get_language(before.guild.id), "lmu")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def guild_update(before: discord.Guild, after: discord.Guild):
    emb = data.get_i18n(data.get_language(before.id), "lgu")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def guild_role_create(role: discord.Role):
    emb = data.get_i18n(data.get_language(role.guild.id), "lgrc")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def guild_role_delete(role: discord.Role):
    emb = data.get_i18n(data.get_language(role.guild.id), "lgrd")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def guild_role_update(before: discord.Role, after: discord.Role):
    emb = data.get_i18n(data.get_language(before.guild.id), "lgrd")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def guild_emojis_update(
    guild: discord.Guild, before: discord.Emoji, after: discord.Emoji
):
    emb = data.get_i18n(data.get_language(guild.id), "lgeu")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )


def voice_state_update(
    member: discord.Member, before: discord.VoiceState, after: discord.VoiceState
):
    emb = data.get_i18n(data.get_language(member.id), "lvsu")
    return embed(
        title=emb["TITLE"],
        description=emb["DESCRIPTION"],
        color=random.randint(0, 1677215),
    )
