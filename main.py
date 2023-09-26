"""TEST Reminder bot"""

import discord
import asyncio
import pytz
from discord.ext import commands

#เอาไว้สำหรับรอรับคำสั่ง
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Run the bot
# always don't forget to remove token

def main():
    """Bot"""
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

    #return วิธีใช้คำสั่ง !knock - 66070105
    @knock.error
    async def knock_error(ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(color=discord.Color.blurple(), description=f"To use this command you have to type \"!knock <time> <task>\" \n \
            Time Format : **s** as second, **m** as minute, **h** as hour, **d** as day \n \
            Command Example : !knock 5s hello world"))

    bot.run(token)

main()
