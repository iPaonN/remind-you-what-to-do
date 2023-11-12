"""TEST Reminder bot"""

import asyncio
from datetime import datetime
from discord.enums import WebhookType
import pytz

import discord
from discord.ext import commands

from system.settings import token
from system.convert import convert

# User github 'Granvarden' = 66070291


def running():
    """always don't forget to remove token!!!"""
    # always don't forget to remove token!!!
    # always don't forget to remove token!!!

    bot.run(token)  # run bot ja!


# เอาไว้สำหรับรอรับคำสั่ง
# bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())
bot = discord.Bot()
slash = bot.create_group('knock', 'What do you want me to remind about?')


class Queue:
    """Queue, thanks to mickey083 for idea"""

    def __init__(self):
        """a list"""
        self._queue = []

    def enqueue(self, item):
        """add task to list"""
        self._queue.append(item)

    def display_q(self):
        """display queue list show added recently"""
        if not self._queue:
            return "The queue is empty."
        return '\n'.join(
            [f'{i + 1}. {s}' for i, s in enumerate(self._queue[::-1])])

    def dequeue(self):
        """clear all set tasks"""
        self._queue.clear()


my_queue = Queue()


@bot.event  # ดูสถานะ
async def on_ready():
    """standby"""
    await bot.change_presence(activity=discord.Game('!knock or /knock'))  # ทดสอบ
    print(f"I have logged in as {bot.user}!")
    print("--> Currenly working... GREEN!")
    print("--> Standing by... READY!")


# ลอง Basic Reminds - 66070105
# Basic Reminds
# @bot.command()
# async def knock(ctx, time, *task):
#     """Basic Reminds"""

#     task = ' '.join(task)
#     converted_time = convert(time)

#     if converted_time == -1:
#         await ctx.send(embed=discord.Embed(color=discord.Color.red(),
#                                            description="Wrong Time Format!"))
#         return

#     if converted_time == -2:
#         await ctx.send(embed=discord.Embed(
#             color=discord.Color.red(),
#             description="The time must be an integer"))
#         return

#     my_queue.enqueue(task)

#     await ctx.send(embed=discord.Embed(
#         color=discord.Color.blue(),
#         description=f"I will remind **\"{task}\"** in **{time}**."))

#     await asyncio.sleep(converted_time)
#     await ctx.send(
#         f":alarm_clock: {ctx.author.mention} It's time for you to **\"{task}\"**"
#     )


# return วิธีใช้คำสั่ง !knock - 66070105
# @knock.error
# async def knock_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send(embed=discord.Embed(
#             color=discord.Color.red(),
#             description="To use this command you have to type \"!knock <time> <task>\" \n \
#         Time Format : **s** as second, **m** as minute, **h** as hour, **d** as day \n \
#         Command Example : !knock 5s hello world or try slash commands!"))


# slash commands
# ทดลองดัดแปลงให้เป็น slash command ต้องเพิ่มคำอธิบายการใช้งานลงคำสั่งเพิ่มเติ่ม รับคนช่วย
# wip in slash command 112


@bot.slash_command(name='help', description="I'd like to introduce myself! To show what I can do!")
async def test(interaction: discord.Interaction):
    """Testing"""
    embed = discord.Embed(title='Help Menu',
                          description='Here what you need to know,\n'
                                      'Time Format\n'
                                      '**s** - second\n'
                                      '**m** - minute\n'
                                      '**h** - hour\n'
                                      '**d** - day\n'
                                      'Even you gonna give me negative time, I will put it in abs!',
                          timestamp=datetime.now(),
                          color=discord.Color.blue())
  
    embed.add_field(name="/knock me 5m Hello World or /knock me 5s5m Hello JA!",
    value="I will remind you with this command!",
    inline=False)
  
    embed.add_field(name="/knock who 1h main @<someone>",
    value="I will remind someone that you mention with this command!",
    inline=False)
  
    embed.add_field(name="/knock everyone 15m 3 Hello Nemo",
    value="I will remind everyone,there's something important! \n"
          "In during 15m I will remind you 3 times before time's up na.",
    inline=False)
  
    embed.add_field(name="/knock remind_list",
    value="List of your set tasks!",
    inline=False)
  
    embed.add_field(name="/knock clear_list",
    value="Yes! You can clear all the set tasks list",
    inline=False)

    embed.add_field(name="/timezone <continent>/<city>, such as Asia/Bangkok",
    value="You know what, I can tell you the other timezone!",
    inline=False)
  
    embed.add_field(name="/subject_score",
    value="Score? Here! Links to your scores.",
    inline=False)
  
    await interaction.response.send_message(embed=embed)


# คำสั่งบอกไทม์โซน
@bot.slash_command(name="timezone", description='Continent/City')
async def sl_timezone(interaction: discord.Interaction, continent_city: str):
    """Slash Command of Timezone"""

    continent_city = continent_city.replace(' ', '_')

    try:
        # Check if the provided timezone is valid
        tz = pytz.timezone(continent_city)
    except pytz.UnknownTimeZoneError:
        await interaction.response.send_message(embed=discord.Embed(
            color=discord.Color.red(),
            description=f"Invalid timezone: {continent_city.title()}\n"
            "Please specify me, such as Europe/Vienna."))
        return

    # Get the current time in the specified timezone
    current_time = datetime.now(tz).strftime("**%Y-%m-%d %H:%M:%S**")

    await interaction.response.send_message(embed=discord.Embed(
        color=discord.Color.blue(),
        description=f"Current time in {continent_city.title()}: {current_time}",
        timestamp=datetime.now()))


@slash.command(name='me', description='I will remind you!')
async def sl_remind(interaction: discord.Interaction, time: str, task: str):
    """Slash Command of Basic Reminder"""

    task = ''.join(task)
    converted_time = convert(time)

    if converted_time == -1:
        await interaction.response.send_message(embed=discord.Embed(
                                                color=discord.Color.red(),
                                                description="Wrong Time Format!"))
        return

    if converted_time == -2:
        await interaction.response.send_message(embed=discord.Embed(
                                                color=discord.Color.red(),
                                                description="The time must be an integer and unit of time such as s for second(s)"))
        return

    my_queue.enqueue(task)

    await interaction.response.send_message(embed=discord.Embed(
                                            color=discord.Color.blue(),
                                            description=f"I Will remind **\"{task}\"** in **{time}**."))

    await asyncio.sleep(converted_time)
    await interaction.followup.send(embed=discord.Embed(color=discord.Color.green(),
                                                        description=f":alarm_clock: {interaction.user.mention}\
                                                        It's time for you to **\"{task}\"**"
                                                        ))


# code belong to mickey
@slash.command(name='who', description='I will remind to someone that you mention!')
async def sl_remindwho(interaction: discord.Interaction, time: str, task: str, who: str):
    """Slash Command of Basic Reminder"""

    task = ''.join(task)
    converted_time = convert(time)

    if converted_time == -1:
        await interaction.response.send_message(embed=discord.Embed(
                                                color=discord.Color.red(),
                                                description="Wrong Time Format!"))
        return

    if converted_time == -2:
        await interaction.response.send_message(embed=discord.Embed(
                                                color=discord.Color.red(),
                                                description="The time must be integer and unit of time such as s for second(s)"))
        return

    my_queue.enqueue(task)

    await interaction.response.send_message(embed=discord.Embed(
                                            color=discord.Color.blue(),
                                            description=f"I Will remind {who} **\"{task}\"** in **{time}**."))

    await asyncio.sleep(converted_time)
    await interaction.followup.send(embed=discord.Embed(
                                    color=discord.Color.green(),
                                    description=f":alarm_clock: {who} It's time for you to **\"{task}\"**"))
# code belong to mickey


@slash.command(name='remind_list', description='Task List')
async def queue(interaction: discord.Interaction):
    '''display the histor'''

    embed = discord.Embed(title='Task List',
                          description='Here, all set tasks.',
                          timestamp=datetime.now(),
                          color=discord.Color.yellow())

    embed.add_field(name="Recently!", value=my_queue.display_q(), inline=False)

    await interaction.response.send_message(embed=embed)


@slash.command(name='clear_list', description='Clear all set tasks')
async def re_queue(interaction: discord.Interaction):
    '''clear the histor'''

    my_queue.dequeue()

    embed = discord.Embed(title='All set tasks has been cleared.',
                          timestamp=datetime.now(),
                          color=discord.Color.purple())

    embed.add_field(name="All clear!",
                    value=my_queue.display_q(), inline=False)

    await interaction.response.send_message(embed=embed)


@slash.command(name='everyone', descripton='Important Message and To Everyone')
async def important(interaction: discord.Interaction, time: str, repeats: int, *, task: str):
    """Command to set a reminder with repeats"""

    original_time = convert(time)

    if original_time <= 0 or repeats <= 0:
        await interaction.response.send_message("Invalid time or repeats format.")
        return

    my_queue.enqueue(task)
    interval = original_time // repeats
    await interaction.response.send_message(embed=discord.Embed(
                                            color=discord.Color.red(),
                                            description=f"I will remind @everyone {repeats} Times about {task}."))

    for i in range(repeats):
        if repeats - i == 1:
            await interaction.followup.send(embed=discord.Embed(
                                            color=discord.Color.brand_red(),
                                            description=f"Final reminder! At {i} time."))
        elif i == 0:
            pass
        elif i == 1:
            await interaction.followup.send(embed=discord.Embed(
                                            color=discord.Color.orange(),
                                            description=f"Remind you {i}st time for {task}"))
        elif i == 2:
            await interaction.followup.send(embed=discord.Embed(
                                            color=discord.Color.orange(),
                                            description=f"Remind you {i}nd time for {task}"))
        elif i == 3:
            await interaction.followup.send(embed=discord.Embed(
                                            color=discord.Color.orange(),
                                            description=f"Remind you {i}rd time for {task}"))
        else:
            await interaction.followup.send(embed=discord.Embed(
                                            color=discord.Color.orange(),
                                            description=f"Remind you {i}th time for {task}"))
        await asyncio.sleep(interval)
    await interaction.followup.send(embed=discord.Embed(
                                    color=discord.Color.green(),
                                    description=f"Time's up! @everyone it's time for {task}"))


@bot.slash_command(name='subject_score', description="Score? PSCP? ITF? ICS?")
async def first_yearscore(interaction: discord.Interaction):
    '''link to all subject's score page'''

    embed = discord.Embed(title='I had all of them already!',
                          timestamp=datetime.now(),
                          color=discord.Color.nitro_pink())

    embed.add_field(name="PSCP's score",
                    value="https://shorturl.at/cdGUX",
                    inline=False)

    embed.add_field(name="ITF's score",
                    value="https://bd3s.short.gy/ITF-66-Lab-Score",
                    inline=False)

    embed.add_field(name="ICS's score",
    value="https://supakit.net/learning/?file=ics/score",
    inline=False)

    embed.add_field(name="M4IT's score?",
    value="Unavailable",
    inline=False)

    await interaction.response.send_message(embed=embed)

running()
