from discord.ext import commands
import requests

from bot_config import bot


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

    await ctx.send("@here")

    emoji_up = '\N{THUMBS UP SIGN}'
    emoji_down = '\N{THUMBS DOWN SIGN}'

    message = await ctx.send(arg)

    await message.add_reaction(emoji_up)
    await message.add_reaction(emoji_down)
