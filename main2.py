import discord
from discord.ext import commands
import music

TOKEN ="MTE2NDQ1NDAwNDg5NDQ3MDIwNQ.GZZoXU.gpRtCMdXpuXKRbhYd2nnUTJ9JcZczzXCwqclNE"
intents = discord.Intents.all()

#intents.members = True

#client = discord.Client(command_prefix="!",intents=intents)

client  = commands.Bot(command_prefix="!",intents = intents)

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(TOKEN)