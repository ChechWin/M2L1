import discord
import random
import os
import requests
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def meme(ctx):
    images = random.choice(os.listdir("Actividad_M2L1/images"))
    with open(f"Actividad_M2L1/images/{images}", 'rb') as f:
            picture = discord.File(f)  
    await ctx.send(file=picture)

@bot.command()
async def perro(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    img_url = data['message']
    embed = discord.Embed(title='Perro aleatorio', color=discord.Color.gold())
    embed.set_image(url=img_url)
    await ctx.send(embed=embed)
    

bot.run("")
