import asyncio
import atexit
import datetime
import discord
import logging
import os
import platform
import random
import sys
import re

from src import command
from src import data
from src import log

from src.command import Command

# client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# logger
logger = logging.getLogger("logger")
formatter = logging.Formatter(
    "%(levelname)s | %(asctime)s << %(message)s >> at file::%(filename)s"
)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
name = f"log/{datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"
file_handler = logging.FileHandler(filename=f"{name}.log")
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


async def send_emb(lang, t, ch) -> None:
    emb = data.get_i18n(lang, t)
    await ch.send(
        embed=discord.Embed(
            title=emb["TITLE"],
            description=emb["DESCRIPTION"],
            color=random.randint(0, 1677215),
        )
    )


@client.event
async def on_ready():
    os.system("cls")
    logger.info(f"Log in")
    logger.info(f"name : {client.user.name} , id : {client.user.id}")

    i = 0

    while True:
        act = (
            discord.Game(
                name=f"In service to {len(client.users)} users, {len(client.guilds)} guilds"
            )
            if i % 2
            else discord.Game(name=f"check help to mention me or type ~help")
        )
        i += 1

        await client.change_presence(status=discord.Status.idle, activity=act)
        await asyncio.sleep(60)

        data.save()


@client.event
async def on_disconnect():
    logger.info("disconnected")


@client.event
async def on_message(message: discord.Message):
    d = command.GetCommand(client, message)
    if d == Command.NONE:
        return
    data.set_traffic(message.author)
    c = data.check(message.guild)
    if c is not None:
        emb = data.get_i18n(c, "invited")
        await message.guild.owner.send(
            embed=discord.Embed(
                title=emb["TITLE"],
                description=emb["DESCRIPTION"].format(message.guild.name),
                color=random.randint(0, 1677215),
            )
        )
        await message.guild.owner.send(
            embed=discord.Embed(
                title="Language Setting / 언어 설정",
                description=f"ENG\nSet the bot's language to ~set lang <Language> command.\ncurrent bot's lang : {c}\n"
                f"\nKOR\n봇의 언어를 ~set lang <언어> 커맨드로 설정해보세요.\n현재 봇의 언어 : {c}",
            )
        )
        await client.get_guild(766164184060002314).get_channel(766164184060002317).send(
            embed=discord.Embed(
                title="ALpha is invited",
                description=f"`{message.guild.name}`, 인원 {len(message.guild.members)}명",
            )
        )
    send = message.channel.send
    lang = data.get_language(message.guild.id)
    """ 
    ####################
    #     Commands     #
    ####################
    """
    if d == Command.HELLO:
        await send_emb(lang, "hello", message.channel)
        return
    if d == Command.RESTART:
        await send(
            embed=discord.Embed(
                title="restarting...", color=random.randint(0, 16777215)
            )
        )
        save()
        os.system("cls")
        os.system("python ./ALpha/main.py")
        sys.exit()
    if d == Command.LANGSET:
        data.change_lang(message.guild.id, message.content.split()[2])
        lang = data.get_language(message.guild.id)
        await send_emb(lang, "langset", message.channel)
        return
    if d == Command.EXEC:
        exec(
            f"""
{message.content[6:].replace("print(", "ex = (")}

with open("data.txt", "w") as fp:
    fp.write(str(ex))
"""
        )
        with open("data.txt", "r") as fp:
            d = fp.read()
            d = "\n" + d
        await send(
            embed=discord.Embed(
                title="Done",
                description=f"```{d}```",
                color=random.randint(0, 16777215),
            )
        )
        return
    if d == Command.INFO:
        emb = data.get_i18n(lang, "info")
        await send(
            embed=discord.Embed(
                title=emb["TITLE"],
                description=emb["DESCRIPTION"].format(
                    discord.__version__, platform.platform(), client.latency * 1000
                ),
                color=random.randint(0, 16777215),
            )
        )
        return
    if d == Command.KICK:
        if not message.author.guild_permissions.kick_members:
            await send_emb(lang, "kickf", message.channel)
            return
        user: discord.Member = message.guild.get_member(
            int("".join(map(str, re.findall(r"\d", message.content.split()[1]))))
        )

        if message.author.roles[-1].position <= user.roles[-1].position:
            await send_emb(lang, "kickr", message.channel)
            return
        if not message.guild.me.guild_permissions.kick_members:
            await send_emb(lang, "kicka", message.channel)
            return
        if user.roles[-1].position > message.guild.me.roles[-1].position:
            await send_emb(lang, "kickp", message.channel)
            return
        reason = " ".join(message.content.split()[2:])
        emb = data.get_i18n(lang, "kicku")
        await user.send(
            embed=discord.Embed(
                title=emb["TITLE"].format(message.guild.name),
                description=emb["DESCRIPTION"].format(reason),
                color=random.randint(0, 1677215),
            )
        )
        await message.guild.kick(user, reason=reason)
        emb = data.get_i18n(lang, "kicks")
        await send(
            embed=discord.Embed(
                title=emb["TITLE"],
                description=emb["DESCRIPTION"].format(
                    user.name, user.user.id, user.user.discriminator
                ),
                color=random.randint(0, 1677215),
            )
        )
        return
    if d == Command.BAN:
        if not message.author.guild_permissions.ban_members:
            await send_emb(lang, "banf", message.channel)
            return
        user: discord.Member = message.guild.get_member(
            int("".join(map(str, re.findall(r"\d", message.content.split()[1]))))
        )

        if message.author.roles[-1].position <= user.roles[-1].position:
            await send_emb(lang, "banr", message.channel)
            return
        if not message.guild.me.guild_permissions.ban_members:
            await send_emb(lang, "bana", message.channel)
            return
        if user.roles[-1].position > message.guild.me.roles[-1].position:
            await send_emb(lang, "banp", message.channel)
            return
        reason = " ".join(message.content.split()[2:])
        emb = data.get_i18n(lang, "banu")
        await user.send(
            embed=discord.Embed(
                title=emb["TITLE"].format(message.guild.name),
                description=emb["DESCRIPTION"].format(reason),
                color=random.randint(0, 1677215),
            )
        )
        await message.guild.ban(user, reason=reason)
        emb = data.get_i18n(lang, "bans")
        await send(
            embed=discord.Embed(
                title=emb["TITLE"],
                description=emb["DESCRIPTION"].format(
                    user.name, user.user.id, user.user.discriminator
                ),
                color=random.randint(0, 1677215),
            )
        )
        return
    if d == Command.BLACKLIST:
        await send(file=discord.File("./ALpha/data/black.txt"))
        return
    if d == Command.ADDBLACK:

        def check(m):
            return m.author == message.author and m.channel == message.channel

        uid = message.content.split()[2]
        reason = " ".join(message.content.split()[3:])
        msg = await client.wait_for("message", check=check)
        embed = discord.Embed(
            title="신고",
            description=f"ID : {uid}\nReporter ID : {msg.author.id}\nREASON : {reason}",
        )
        embed.set_image(url=msg.attachments[0].url)
        await client.get_guild(766164184060002314).get_member(418023987864403968).send(
            embed=embed
        )
        return
    if d == Command.REMOVEBLACK:
        return


@client.event
async def on_guild_join(guild):
    c = data.join_guild(guild)
    emb = data.get_i18n(c, "invited")
    await guild.owner.send(
        embed=discord.Embed(
            title=emb["TITLE"],
            description=emb["DESCRIPTION"].format(guild.name),
            color=random.randint(0, 1677215),
        )
    )
    await guild.owner.send(
        embed=discord.Embed(
            title="Language Setting / 언어 설정",
            description=f"ENG\nSet the bot's language to ~set lang <Language> command.\ncurrent bot's lang : {c}\n"
            f"\nKOR\n봇의 언어를 ~set lang <언어> 커맨드로 설정해보세요.\n현재 봇의 언어 : {c}",
        )
    )
    await client.get_guild(766164184060002314).get_channel(766164184060002317).send(
        embed=discord.Embed(
            title="ALpha is invited",
            description=f"`{guild.name}`, 인원 {len(guild.members)}명",
        )
    )


def save():
    data.save()


@client.event
async def on_message_delete(msg: discord.Message):
    if log.get_channel(msg.guild.id) is None:
        return


@client.event
async def on_bulk_message_delete(msgs: discord.Message):
    pass


@client.event
async def on_message_edit(bf: discord.Message, af: discord.Message):
    pass


@client.event
async def on_reaction_add(react: discord.Reaction, user: discord.Member):
    pass


@client.event
async def on_reaction_remove(react: discord.Reaction, user: discord.Member):
    pass


@client.event
async def on_reaction_clear(msg: discord.Message, reacts: discord.Reaction):
    pass


@client.event
async def on_guild_channel_delete(ch):
    pass


@client.event
async def on_guild_channel_create(ch):
    pass


@client.event
async def on_guild_channel_update(bf, af):
    pass


@client.event
async def on_member_join(member: discord.Member):
    if data.is_black_on(member.guild.id):
        if data.is_in_black(member.user.id):
            emb = data.get_i18n(data.get_language(member.guild.id), "blackk")
            await member.guild.owner.send(
                embed=discord.Embed(
                    title=emb["TITLE"],
                    description=emb["DESCRIPTION"].format(
                        f"{member.user.name}#{member.user.discriminator}",
                        data.get_black_reason(member.user.id),
                    ),
                    color=random.randint(0, 1677215),
                )
            )
            await member.guild.ban(member)


@client.event
async def on_member_remove(member: discord.Member):
    pass


@client.event
async def on_member_update(bf: discord.Member, af: discord.Member):
    pass


@client.event
async def on_guild_update(bf: discord.Guild, af: discord.Guild):
    pass


@client.event
async def on_guild_role_create(role: discord.Role):
    pass


@client.event
async def on_guild_role_delete(role: discord.Role):
    pass


@client.event
async def on_guild_role_update(bf: discord.Role, af: discord.Role):
    pass


@client.event
async def on_guild_emojis_update(
    guild: discord.Guild, bf: discord.Emoji, af: discord.Emoji
):
    pass


@client.event
async def on_voice_state_update(
    member: discord.Member, bf: discord.VoiceState, af: discord.VoiceState
):
    pass


@client.event
async def on_member_ban(guild: discord.Guild, member: discord.Member):
    pass


@client.event
async def on_member_unban(guild: discord.Guild, member: discord.user):
    pass


@client.event
async def on_invite_create(invite: discord.Invite):
    pass


@client.event
async def on_invite_delete(invite: discord.Invite):
    pass


@client.event
async def on_raw_message_delete(payload):
    pass


@client.event
async def on_raw_bulk_message_delete(payload):
    pass


@client.event
async def on_raw_message_edit(payload):
    pass


@client.event
async def on_raw_reaction_add(payload):
    pass


@client.event
async def on_raw_reaction_remove(payload):
    pass


@client.event
async def on_raw_reaction_clear(payload):
    pass


@client.event
async def on_raw_reaction_clear_emoji(payload):
    pass


atexit.register(save)
client.run(os.environ["ALPHATOKEN"])
