import discord
import random
import json
with open('setting.json', mode='r', encoding="utf8") as jfile:
    jdata = json.load(jfile)
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['joinchannel_id']))
    await channel.send(f'歡迎 {member} on9仔入群!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['leavechannel_id']))
    await channel.send(f'屌你 {member} on9仔退群!')

@bot.event
async def on_message(message):
    if message.content == '小丑':
        random_clown = random.choice(jdata['clown'])
        await message.channel.send(random_clown)
    await bot.process_commands(message)

@bot.command()
async def luck(ctx):
    random_luck = random.choice(jdata['lucklist'])
    await ctx.send(f'你的運勢為{random_luck}')
    
@bot.command()
async def ping(ctx):
    await ctx.send('你有'f'{round(bot.latency*1000)}ms延遅')
    if bot.latency*1000 >= 200:
        await ctx.send('你都幾撚LAG下')
    elif bot.latency*1000 >= 100:
        await ctx.send('少LAG')
    elif bot.latency*1000 < 100:
        await ctx.send('暢通無阻')


bot.run(jdata['TOKEN'])