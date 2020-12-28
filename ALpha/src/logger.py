import discord
import json
import data


def get_channel(guild: discord.Guild):
    return guild.get_channel(data.get_log_channel(guild.id)), data.get_language(
        guild.id
    )


def member_join(guild, member) -> discord.Embed:
    lang = data.get_language(guild.id)
    return discord.Embed(
        title="길드 가입" if lang == "kor" else "guild join",
        description=f"유저```{member.mention}\nid : {member._user.id}\n이름 : {member._user.name}#{member._user.avatar}\n계정 생성일 : {member._user.created_at.strftime('%Y-%m-%d %H:%M:%S')}```",
    )
