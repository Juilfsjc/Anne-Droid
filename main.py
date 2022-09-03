import discord
from discord.ext import commands
import datetime
from datetime import datetime
from config import *
from game import *

bot = commands.Bot(command_prefix=PREFIX, description="Test Bot for discord.py")


# Heart beat bot event
@bot.event
async def on_ready():
    print("I am alive!")


# Role addition bot event
@bot.event
async def on_raw_reaction_add(payload):
    ourMessageID = 1015717753224700054

    if ourMessageID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == '🦍':
            role = discord.utils.get(guild.roles, name='Cincinnati')
        elif emoji == '🌿':
            role = discord.utils.get(guild.roles, name='Kentucky')
        elif emoji == '🎮':
            role = discord.utils.get(guild.roles, name='Gamer')
        await member.add_roles(role)


# Role removal bot event
@bot.event
async def on_raw_reaction_remove(payload):
    ourMessageID = 1015717753224700054

    if ourMessageID == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == '🦍':
            role = discord.utils.get(guild.roles, name='Cincinnati')
        elif emoji == '🌿':
            role = discord.utils.get(guild.roles, name='Kentucky')
        elif emoji == '🎮':
            role = discord.utils.get(guild.roles, name='Gamer')
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("member not found.")


# Hello command
@bot.command(pass_context=True)
async def hello(ctx, name: str):
    await ctx.message.add_reaction('👋')
    embed = discord.Embed(
        title=f"Hello {name}! I am a Bot!"
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👋')


# Goodbye command
@bot.command(pass_context=True)
async def bye(ctx, name: str):
    await ctx.message.add_reaction('👋')
    embed = discord.Embed(
        title=f"Goodbye {name}! I will miss you!"
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👋')


# Hello sam command
@bot.command(pass_context=True)
async def sam(ctx):
    await ctx.message.add_reaction('👍')
    embed = discord.Embed(
        title="Annyeonghaseyo Sam!"
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🧡')


# Clear messages command (accepts an integer)
@bot.command(pass_context=True)
async def clear(ctx, amount: str):
    if amount == 'all':
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=(int(amount) + 1))


# Welcome: command to add roles
@bot.command(pass_context=True)
async def welcome(ctx):
    embed = discord.Embed(
        title="Welcome to the Server!",
        description='We hope you enjoy your stay!',
        url='https://www.numa.nz/',
        timestamp=datetime.now(),
        color=15418782
    )
    msg = await ctx.send(embed=embed)
    # Cincinnati Role
    await msg.add_reaction('🦍')
    # Kentucky Role
    await msg.add_reaction('🌿')
    # Gamer Role testestestrtrtrtt
    await msg.add_reaction('🎮')
    # Verify Emoji
    await msg.add_reaction('✅')


@bot.command(pass_context=True)
@commands.has_role("Gamer")
async def games(ctx):
    await games(ctx, bot)


bot.run(TOKEN, bot=True, reconnect=True)
