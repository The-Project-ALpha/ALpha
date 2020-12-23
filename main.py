import discord
import asyncio
import datetime
import os
import command
import data
import random
import sys
import logging

from command import Command
intents = discord.Intents.all()
client = discord.Client(intents=intents)


def __get_logger():

    __logger = logging.getLogger('logger')

    formatter = logging.Formatter(
        '%(levelname)s | %(asctime)s << %(message)s >> at file::%(filename)s'
    )

    stream_handler = logging.StreamHandler()

    stream_handler.setFormatter(formatter)

    name = f"log/{datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"

    print(name)

    file_handler = logging.FileHandler(filename=f"{name}.log")

    file_handler.setLevel(logging.INFO)

    __logger.addHandler(file_handler)

    __logger.addHandler(stream_handler)

    __logger.setLevel(logging.DEBUG)
    return __logger


logger = __get_logger()


@client.event
async def on_ready():
    logger.info(f"Log in")
    logger.info(f"name : {client.user.name} , id : {client.user.name}")
    i = 0
    while True:
        act = discord.Game(name="loading...")
        if (i % 2 == 0):
            act = discord.Game(
                name=f"{len(client.users)} users, {len(client.guilds)} guilds"
            )
        elif (i % 2 == 1):
            act = discord.Game(name=f"type ~help or mention me!")
        i += 1
        await client.change_presence(status=discord.Status.idle, activity=act)
        await asyncio.sleep(30)


@client.event
async def on_message(message: discord.Message):
    d = command.GetCommand(client, message)
    if (d == Command.none):
        return
    try:
        send = message.channel.send
        lang = data.GetLang(message.guild)
        if (d == Command.hello):
            title = "안녕하세요 👋" if lang == "kor" else "Hi there 👋"
            des = "ALpha는 Project ALpha에서 개발한 서버 관리 봇입니다.\n자세한 내용은 ~help로 알아보세요!" if lang == "kor" else "ALpha is a server management bot developed by Project ALpha.\n Find out more at ~help!"
            color = random.randint(0, 16777215)
            await send(
                embed=discord.Embed(title=title, description=des, color=color)
            )
            return
        if (d == Command.restart):
            await send(
                embed=discord.
                Embed(title="restarting...", color=random.randint(0, 16777215))
            )
            os.system("cls")
            os.system("python main.py")
            sys.exit()
    except Exception as e:
        logger.error(str(e))
        return


@client.event
async def on_guild_join(guild):
    data.JoinGuild(guild)


client.run(os.environ["ALPHATOKEN"])
