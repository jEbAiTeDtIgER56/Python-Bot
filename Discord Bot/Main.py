import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'plz ')

@client.event
async def on_ready():
    print('Boto is ready.')

@client.command()
async def ping(ctx):
    await ctx.send('uïn heh')

@client.command()
async def stop(ctx):
    await ctx.send('no u :c')

client.run('OTEyNzMxMDA5ODM2MDIzODY4.YZ0M_g.VyGyMS5ZHajNr8CHXezvOWtEN_A')