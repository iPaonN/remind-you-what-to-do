"""TEST Reminder bot"""

import discord
import asyncio
import sys
import os
import pytz
from datetime import datetime
from discord.ext import commands
from wip.convert import convert

# เอาไว้สำหรับรอรับคำสั่ง
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())
slash = bot.create_group('knock', 'What do you want me to remind about?')
# User github 'Granvarden' = 66070291

@bot.event  # ดูสถานะ
async def on_ready():
    """standby"""
    await bot.change_presence(activity=discord.Game('!knock or /knock'))  # ทดสอบ
    print(f"I have logged in as {bot.user}!")
    print("--> Currenly working... GREEN!")
    print("--> Standing by... READY!")

# รอคำสั่ง
@bot.command()
async def hello(ctx):
    """hi"""
    await ctx.send("Hi, I am here!")


@bot.command()
async def test2(ctx):
    """test2"""
    await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"Embed Test"))


@bot.command()
async def sendpic(ctx):
    'test send pic'
    await ctx.send('This is picture', file=discord.File('timeup.png'))


@bot.command()
# คำสั่งบอกไทม์โซน
async def timezone(ctx, tz_name):
    """timezone as old fashion command"""
    try:
        # Check if the provided timezone is valid
        tz = pytz.timezone(tz_name)
    except pytz.UnknownTimeZoneError:
        await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"Invalid timezone: {tz_name}\n" #add somecolor -112
        "Please specify me, such as Europe/Vienna"))
        return

    # Get the current time in the specified timezone
    current_time = datetime.now(tz).strftime("**%Y-%m-%d %H:%M:%S**")

    await ctx.send(embed=discord.Embed(color=discord.Color.blue(), description=f"Current time in {tz_name}: {current_time}"))

# ลอง Basic Reminds - 66070105
@bot.command()
# Basic Reminds
async def knock(ctx, time, *task):

    task = ' '.join(task)
    converted_time = convert(time)

    if converted_time == -1:
        await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"Wrong Time Format!"))
        return

    if converted_time == -2:
        await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"The time must be an integer"))
        return

    await ctx.send(embed=discord.Embed(color=discord.Color.blue(), description=f"I Will remind **\"{task}\"** in **{time}**."))

    await asyncio.sleep(converted_time)
    await ctx.send(f":alarm_clock: {ctx.author.mention} It's time for you to **\"{task}\"**")


# return วิธีใช้คำสั่ง !knock - 66070105
@knock.error
async def knock_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"To use this command you have to type \"!knock <time> <task>\" \n \
        Time Format : **s** as second, **m** as minute, **h** as hour, **d** as day \n \
        Command Example : !knock 5s hello world"))

# return error timezone - 112
@timezone.error
async def timezone_error(ctx, error):
    """In case of timezone error"""
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"Please specify me. Type like this \"!timezone <Continent>/<City>\" \n \
        Here! Format : Continent such as Asia, City could be ... Bangkok \n \
        Command Example : !timezone Asia/Bangkok\n"
        "Yo! TRY SLASH COMMAND!"))

# slash commands
# ทดลองดัดแปลงให้เป็น slash command ต้องเพิ่มคำอธิบายการใช้งานลงคำสั่งเพิ่มเติ่ม รับคนช่วย
# wip in slash command 112

@slash.command()
async def test(interaction: discord.Interaction):
    """Testing"""
    await interaction.response.send_message(f"Hi! {interaction.user.mention} get the job done already!", ephemeral=False)


# คำสั่งบอกไทม์โซ
@slash.command(name="timezone", description='Continent/City')
async def sl_timezone(interaction: discord.Interaction, continent_city: str):
    """Slash Command of Timezone"""
    try:
        # Check if the provided timezone is valid
        tz = pytz.timezone(continent_city)
    except pytz.UnknownTimeZoneError:
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.red(), description=f"Invalid timezone: {continent_city}\n"
        "Please specify me, such as Europe/Vienna"))
        return

    # Get the current time in the specified timezone
    current_time = datetime.now(tz).strftime("**%Y-%m-%d %H:%M:%S**")

    await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description=f"Current time in {continent_city}: {current_time}"))


@slash.command(name='me', description='I will remind you!')
async def sl_remind(interaction: discord.Interaction,time: str, task: str): #used to be basicremind
    """Slash Command of Basic Reminder"""

    task = ''.join(task)
    converted_time = convert(time)

    if converted_time == -1:
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.red(), description=f"Wrong Time Format!"))
        return

    if converted_time == -2:
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.red(), description=f"The time must be an integer and unit of time such as s for second(s)"))
        return

    await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description=f"I Will remind **\"{task}\"** in **{time}**."))

    await asyncio.sleep(converted_time)
    await interaction.followup.send(f":alarm_clock: {interaction.user.mention} It's time for you to **\"{task}\"**")


def running():
    """always don't forget to remove token!!!"""
    # always don't forget to remove token!!!
    token = "" # สำหรับรันบอท
    # always don't forget to remove token!!!

    bot.run(token)  # run bot ja!

running()
