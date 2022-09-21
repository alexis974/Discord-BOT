#!/usr/bin/env python3

from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def d6(ctx):
    import random
    n = random.randint(1,6)
    await ctx.send(n)

@bot.event
async def on_message(ctx):
    if ctx.content == "Salut tout le monde":
        await ctx.reply("Salut tout seul")

bot.run(token)  # Starts the bot
