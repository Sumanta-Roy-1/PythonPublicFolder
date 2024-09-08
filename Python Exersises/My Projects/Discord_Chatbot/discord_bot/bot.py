import discord
from discord.ext import commands
# import config
import os

Dkey=os.environ["DISCORD_KEY"]
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready.")
    await bot.tree.sync()


# @bot.command()
# async def ping(ctx):
#     await ctx.send("Pong!")

@bot.tree.command()
async def ping(interaction: discord.Integration):
    await interaction.response.send_message("Pong!")


@bot.tree.command()
async def hello(interaction: discord.Integration):
    await interaction.response.send_message("Hello!")

# bot.run(config.DISCORD_TOKEN)
bot.run(Dkey)