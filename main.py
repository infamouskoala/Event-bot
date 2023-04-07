from discord.ext import commands
import discord
import asyncio
token = input("Enter token: ") # [INPUT] bot token

koala = commands.Bot(command_prefix="ar!", intents=discord.Intents.all())

content = "@everyone we hope you all enjoying the event. Make sure to follow the artists on their socials!"
x = int(input("channel id: ")) # [INPUT] channel id to send message in
time = int(input("time delay: ")) # [INPUT] time delay

@koala.event 
async def on_ready():
    print(f"Starting to send messages in channel id {x}. Made with love by https://github.com/infamous-koala")
    while True:
        await koala.get_channel(x).send(content)
        await asyncio.sleep(time)

koala.run(token)
