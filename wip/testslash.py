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
