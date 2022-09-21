from discord.ext import commands

from bot_config import bot

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def d6(ctx):
    import random
    n = random.randint(1,6)
    await ctx.send(n)

@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.reply("Salut tout seul")
    await bot.process_commands(message)
