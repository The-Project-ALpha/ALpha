import discord
import asyncio
import datetime
import os
import event

intents = discord.Intents.all()
client = discord.Client(intents=intents)


class Debug:
    @staticmethod
    def GetTime() -> str:
        now: datetime.datetime = datetime.datetime.now()
        return f"{now.year} {now.month} {now.day}/{now.hour}:{now.minute}:{now.second} - "

    @staticmethod
    def Log(msg: str) -> None:
        print(Debug.GetTime() + msg)


@client.event
async def on_ready():
    Debug.Log(f"Log in")
    Debug.Log(f"name : {client.user.name} , id : {client.user.name}")
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
    d = GetCommand(message)
    if (d == None):
        return


@client.event
async def on_guild_join(guild):
    event.JoinGuild(guild)


def GetCommand(msg: discord.Message) -> str:
    if (msg.content == client.user.mention or "~help"):
        return "help"
    if (not msg.content.startwith("~")):
        return None
    mc = msg.content
    mcs = mc.split()


client.run(os.environ["ALPHATOKEN"])
