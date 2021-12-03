import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'plz ')

@client.event
async def on_ready():
    print('Boto is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'uÃ¯n heh: {client.latency * 1000}')

@client.command(brief="sends the bot's invite link")
async def invite(ctx):
    async with ctx.typing():
        await ctx.send('insert invite link here')

@commands.Cog.listener()
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hi')
            break

@client.event
async def on_message(message):
    if 'bruh' in message.clean_content.lower():
        message.channel.send('BRUH')
    await client.process_commands(message)

@client.command()
async def stop(ctx):
    await ctx.send('no u :c')

client.run('')
