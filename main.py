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
        act = discord.Game(
            name=f"In service to {len(client.users)} users, {len(client.guilds)} guilds"
        ) if i % 2 else discord.Game(
            name=f"check help to mention me or type ~help"
        )
        i += 1
        await client.change_presence(status=discord.Status.idle, activity=act)
        await asyncio.sleep(30)


@client.event
async def on_message(message: discord.Message):
    d = command.GetCommand(client, message)
    if (d == Command.none):
        return
    c = data.Check(client, message.guild)
    if (not c == None):
        title = "안녕하세요 👋" if c == "kor" else "Hi there 👋"
        des = f"ALpha 봇을 `{message.guild.name}` 서버에 추가해 주셔서 감사합니다!\n~help 명령어로 열 수 있는 도움말을 참고해보세요!" if c == "kor" else f"Thank you for adding the ALpha bot to the {message.guild.name} server!See the help that you can open with the \n~help command!"
        color = random.randint(0, 1677215)
        await message.guild.owner.send(
            embed=discord.Embed(title=title, description=des, color=color)
        )
        await client.get_guild(766164184060002314).get_channel(
            766164184060002317
        ).send(
            embed=discord.Embed(
                title="ALpha is invited",
                description=
                f"`{message.guild.name}`, 인원 {len(message.guild.members)}명"
            )
        )

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
    c = data.JoinGuild(client, guild)
    title = "안녕하세요 👋" if c == "kor" else "Hi there 👋"
    des = f"ALpha 봇을 `{guild.name}` 서버에 추가해 주셔서 감사합니다!\n~help 명령어로 열 수 있는 도움말을 참고해보세요!" if c == "kor" else f"Thank you for adding the ALpha bot to the {guild.name} server!See the help that you can open with the \n~help command!"
    color = random.randint(0, 1677215)
    await guild.owner.send(
        embed=discord.Embed(title=title, description=des, color=color)
    )
    await client.get_guild(766164184060002314).get_channel(
        766164184060002317
    ).send(
        embed=discord.Embed(
            title="ALpha is invited",
            description=f"`{guild.name}`, 인원 {len(guild.members)}명"
        )
    )


client.run(os.environ["ALPHATOKEN"])
