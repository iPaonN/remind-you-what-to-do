"""TEST Reminder bot"""

import discord
import asyncio
from discord.ext import commands
<<<<<<< Updated upstream
from discord import app_commands
=======
from wip.convert import convert
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======

def running():
    """always don't forget to remove token!!!"""
    # always don't forget to remove token!!!
    token = "" # สำหรับรันบอท
    # always don't forget to remove token!!!

    bot.run(token)  # run bot ja!

running()

# below, all func
>>>>>>> Stashed changes

#เอาไว้สำหรับรอรับคำสั่ง
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Run the bot
# always don't forget to remove token

<<<<<<< Updated upstream
def main():
    """Bot"""
=======
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

    histor.append(task)
    await ctx.send(embed=discord.Embed(color=discord.Color.blue(), description=f"I Will remind **\"{task}\"** in **{time}**."))

    await asyncio.sleep(converted_time)
    await ctx.send(f":alarm_clock: {ctx.author.mention} It's time for you to **\"{task}\"**")


# return วิธีใช้คำสั่ง !knock - 66070105
@knock.error
async def knock_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"To use this command you have to type \"!knock <time> <task>\" \n \
        Time Format : **s** as second, **m** as minute, **h** as hour, **d** as day \n \
        Command Example : !knock 5s hello world or use slash command!"))

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
<<<<<<< Updated upstream

def running():
    """always don't forget to remove token!!!"""
>>>>>>> Stashed changes
    # always don't forget to remove token!!!
    token = '' #สำหรับรันบอท
    # always don't forget to remove token!!!

    @bot.event #ดูสถานะ
    async def on_ready():
        """standby"""
        print("Hi, This is Yu! I'm here")
        print("<---------------------->")
        try:
            synced_wip = await bot.tree.sync()
            print(f"Synced {len(synced_wip)} command(s)")
        except Exception as syn:
            print(syn)

    #รอคำสั่ง
    @bot.command()
    async def hello(ctx):
        """hi"""
        await ctx.send("Hi, I am here!")

    # wip in slash command 112
    @bot.tree.command()
    async def test(interaction: discord.Interaction):
        """test"""
        await interaction.response.send_message(f"Hi! {interaction.user.mention} get the job done already!", ephemeral=False)

    @bot.command()
    async def test2(ctx):
        """test2"""
        await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"Embed Test"))

    #ลอง Basic Reminds - 66070105
    @bot.command()
    async def knock(ctx, time, *task):

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
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"Wrong Time Format!"))
            return

        if converted_time == -2:
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"The time must be an integer"))
            return

        await ctx.send(embed=discord.Embed(color=discord.Color.blue(), description=f"I Will remind **\"{task}\"** in **{time}**."))

        await asyncio.sleep(converted_time)
        await ctx.send(f" :alarm_clock: {ctx.author.mention} It's time for you to **\"{task}\"**")

    bot.run(token)

main()
=======
    
>>>>>>> Stashed changes
