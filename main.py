import discord
import asyncio
import datetime
import os
import command
import data

from command import Command
from debug import Debug
intents = discord.Intents.all()
client = discord.Client(intents=intents)





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
    d = command.GetCommand(client, message)
    if (d == Command.none):
        return
    send = await message.channel.send
    if(d == Command.hello):
        


@client.event
async def on_guild_join(guild):
    data.JoinGuild(guild)


client.run(os.environ["ALPHATOKEN"])
