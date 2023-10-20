import discord
import responses
import music
from discord.ext import commands
from dotenv import load_dotenv
import os



async def send_msg(message,user_msg,is_private = False):
    try:
        response = responses.handle_response(user_msg)
        if is_private:
            await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.all()

    #intents.members = True

    #client = discord.Client(command_prefix="!",intents=intents)

    client  = commands.Bot(command_prefix="!",intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_msg = str(message.content)
        channel = str(message.channel)
        print(type(message.content),message.content)
        print(f"{username} said : '{user_msg}' ({channel})")

        if user_msg[0] == '!':
            user_msg = user_msg[1:]
            await send_msg(message, user_msg, is_private = True)
        else:
            await send_msg(message, user_msg, is_private = False)

    cogs = [music]
    for i in range(len(cogs)):
        cogs[i].setup(client)
   
    client.run(TOKEN)