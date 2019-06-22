import discord
from discord.ext import commands




bot = commands.Bot(command_prefix='GB', case_insensitive=True)


@bot.command()
async def Ping(ctx):
    await ctx.send('I\'m here and online V1.0 :smile:')






bot.run(TOKEN)
