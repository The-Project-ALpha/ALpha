import discord
import json

def JoinGuild(guild:discord.Guild):
    region:discord.VoiceRegion = guild.region
    if(region == discord.VoiceRegion.south_korea):
        