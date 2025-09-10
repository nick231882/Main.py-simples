import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot('seu prefixo', intents=intents)

@bot.event
async def on_ready():
    print(f'bot ligado como {bot.user}')

@bot.command()
async def ping(ctx:commands.Context):
    await ctx.send('Pong 🏓')

bot.run('token do bot')
