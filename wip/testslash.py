"""Reminder"""

import discord
import asyncio
import os
#import pytz
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# wip in slash command 112
@bot.tree.command()
async def test(interaction: discord.Interaction):
    """test"""
    await interaction.response.send_message(f"Hi! {interaction.user.mention} get the job done already!", ephemeral=False)

@bot.tree.command()
@app_commands.describe(ctx=int, time=str, task=str)
async def knockslash(interaction: discord.Interaction,ctx, time, *task):
    task = ' '.join(task)

    def convert(time):
        pos = ['s', 'm', 'h', 'd']

        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    converted_time = convert(time)

    if converted_time == -1:
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.red(), description=f"Wrong Time Format!"))
        return

    if converted_time == -2:
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.red(), description=f"The time must be an integer"))
        return

    await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description=f"I Will remind **\"{task}\"** in **{time}**."))

    await asyncio.sleep(converted_time)
    await interaction.response.send_message(f" :alarm_clock: {ctx.author.mention} It's time for you to **\"{task}\"**")
