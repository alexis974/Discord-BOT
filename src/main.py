#!/usr/bin/env python3

from discord.ext import commands
from discord.utils import get
import discord

from bot_config import bot

from warm_up import *
from administration import *
from fun_and_games import *


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


@bot.command()
async def pong(ctx):
    await ctx.send('pong')

token =  # FIXME
bot.run(token)  # Starts the bot
