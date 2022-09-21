from discord.ext import commands

from bot_config import bot


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
