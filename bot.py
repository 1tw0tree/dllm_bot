import discord
import random
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)
lucklist = []

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1063374703613456454)
    await channel.send(f'歡迎 @{member} on9仔入群!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1063374737771872286)
    await channel.send(f'屌你 @{member} on9仔退群!')

@bot.command()
async def ping(ctx):
    await ctx.send('你有'f'{round(bot.latency*1000)}ms延遅')
    if bot.latency*1000 >= 200:
        await ctx.send('你都幾撚LAG下')
    elif bot.latency*1000 >= 100:
        await ctx.send('少LAG')
    elif bot.latency*1000 < 100:
        await ctx.send('暢通無阻')


bot.run('MTA2MzMzMTczNDk2OTY1OTQxMg.GcZHiJ.ITR9A6u6ElXCAcKay-Fgq-Fq8v3ImhOAUx6hbs')