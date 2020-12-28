import asyncio
import datetime
import discord
import logging
import os
import platform
import random
import sys

from src import command
from src import data
from src import logger

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


@client.event
async def on_ready():
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
        await asyncio.sleep(30)


@client.event
async def on_disconnect():
    logger.info("disconnected")


@client.event
async def on_message(message: discord.Message):
    d = command.GetCommand(client, message)
    if d == Command.none:
        return
    data.set_traffic(message.author)
    c = data.check(message.guild)
    if not c == None:
        title = "안녕하세요 👋" if c == "kor" else "Hi there 👋"
        des = (
            f"ALpha 봇을 `{message.guild.name}` 서버에 추가해 주셔서 감사합니다!\n~help 명령어로 열 수 있는 도움말을 참고해보세요!"
            if c == "kor"
            else f"Thank you for adding the ALpha bot to the {message.guild.name} server!See the help that you can open with the \n~help command!"
        )
        color = random.randint(0, 1677215)
        await message.guild.owner.send(
            embed=discord.Embed(title=title, description=des, color=color)
        )
        await message.guild.owner.send(
            embed=discord.Embed(
                title="Language Setting / 언어 설정",
                description=f"ENG\nSet the bot's language to ~set lang <Language> command.\ncurrent bot's lang : {c}\n\nKOR\n봇의 언어를 ~set lang <언어> 커맨드로 설정해보세요.\n현재 봇의 언어 : {c}",
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
    if d == Command.hello:
        emb = data.get_i18n(lang, "hello")
        await send(
            embed=discord.Embed(
                title=emb["TITLE"],
                description=emb["DESCRIPTION"],
                color=random.randint(0, 16777215),
            )
        )
        return
    if d == Command.restart:
        await send(
            embed=discord.Embed(
                title="restarting...", color=random.randint(0, 16777215)
            )
        )
        os.system("cls")
        os.system("python main.py")
        sys.exit()
    if d == Command.langset:
        data.change_lang(message.guild, message.content.split()[2])
        lang = data.get_language(message.guild)
        emb = data.get_i18n(lang, "langset")
        await send(
            embed=discord.Embed(
                title=emb["TITLE"],
                description=emb["DESCRIPTION"],
                color=random.randint(0, 16777215),
            )
        )
    if d == Command._exec:
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
    if d == Command.info:
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


@client.event
async def on_guild_join(guild):
    c = data.join_guild(guild)
    title = "안녕하세요 👋" if c == "kor" else "Hi there 👋"
    des = (
        f"ALpha 봇을 `{guild.name}` 서버에 추가해 주셔서 감사합니다!\n~help 명령어로 열 수 있는 도움말을 참고해보세요!"
        if c == "kor"
        else f"Thank you for adding the ALpha bot to the {guild.name} server!See the help that you can open with the \n~help command!"
    )
    color = random.randint(0, 1677215)
    await guild.owner.send(
        embed=discord.Embed(title=title, description=des, color=color)
    )
    await guild.owner.send(
        embed=discord.Embed(
            title="Language Setting / 언어 설정",
            description=f"ENG\nSet the bot's language to ~set lang <Language> command.\ncurrent bot's lang : {c}\n\nKOR\n봇의 언어를 ~set lang <언어> 커맨드로 설정해보세요.\n현재 봇의 언어 : {c}",
        )
    )
    await client.get_guild(766164184060002314).get_channel(766164184060002317).send(
        embed=discord.Embed(
            title="ALpha is invited",
            description=f"`{guild.name}`, 인원 {len(guild.members)}명",
        )
    )


client.run(os.environ["ALPHATOKEN"])
