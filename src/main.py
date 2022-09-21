#!/usr/bin/env python3

from discord.ext import commands
from discord.utils import get
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.reply("Salut tout seul")
    await bot.process_commands(message)

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

@bot.command()
async def admin(ctx, arg = None):
    """
    TODO:
        - Permission are not set if role already exist
    """
    if arg is None:
        await ctx.send("Missing nickname to assign admin role")
        return

    role_name = "admin"
    role = get(ctx.guild.roles, name=role_name)

    if not role:
        perms = discord.Permissions(manage_channels=True, kick_members=True, ban_members=True)
        await ctx.guild.create_role(name=role_name, colour=discord.Colour(0x0062ff), permissions=perms)
        await ctx.send(f"Role {role_name} has been created")
        role = get(ctx.guild.roles, name=role_name)

    user = discord.utils.get(ctx.guild.members, name=arg)
    if not user:
        await ctx.send(f"Nickname \"{arg}\" does not exist")
        return

    await user.add_roles(role)
    await ctx.send(f"User {arg} ({user}) have been given {role_name} role")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, arg = None):
    if arg is None:
        await ctx.send("Missing nickname to assign admin role")
        return

    user = discord.utils.get(ctx.guild.members, name=arg)
    if not user:
        await ctx.send(f"Nickname \"{arg}\" does not exist")
        return

    await user.ban(reason=None)

    await ctx.send(f"User {arg} ({user}) has been banned")

@bot.command()
async def count(ctx):
    discord_status = list(discord.Status)

    for i in range(len(discord_status)):
        status = list(filter(lambda member: member.status == discord_status[i], ctx.guild.members))
        plural = ""
        if len(status) > 1:
            plural = "s"

        if len(status) > 0:
            await ctx.send(f"{len(status)} member{plural} are {discord_status[i]}")


import requests
@bot.command()
async def xkcd(ctx):
    url = "https://c.xkcd.com/random/comic/"
    res = requests.get(url)
    if res.status_code != 200:
        await ctx.send("Could not fetch image")
        return

    await ctx.send(res.url)


@bot.command()
async def poll(ctx, arg = None):
    if arg is None:
        await ctx.send("You must specify a question")
        return

    #allowed_mentions = discord.AllowedMentions(everyone = True)
    #await ctx.send(content = "@here", allowed_mentions = allowed_mentions)
    await ctx.send("@here")

    emoji_up = '\N{THUMBS UP SIGN}'
    emoji_down = '\N{THUMBS DOWN SIGN}'
    message = await ctx.send(arg)
    await message.add_reaction(emoji_up)
    await message.add_reaction(emoji_down)

bot.run(token)  # Starts the bot
