"""TEST Reminder bot"""

import discord
from discord.ext import commands
import asyncio

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

    #รอคำสั่ง
    @bot.command()
    async def hello(ctx):
        """hi"""
        await ctx.send("Hi, I am here!")

    @bot.command()
    async def test(ctx):
        """test"""
        await ctx.send("arai ja!")

    #ลอง Basic Reminds - 66070105
    @commands.command()
    async def knock(self, ctx, time, task):
        def convert(time):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

            unit = time[-1]

            if unit not in pos:
                return -1
            try:
                val - int(time[:-1])
            except:
                return -2

            return val * time_dict[unit]

        converted_time = convert(time)

        if converted_time == -1:
            await ctx.send("Wrong Time Format!")
            return

        if converted_time == -2:
            await ctx.send("The time must be an integer")
            return

        await ctx.send(f"I Will remind **{task}** in **{time}**.")

        await asyncio.sleep(converted_time)
        await ctx.send(f"{ctx.author.mention} It's time for you to **{task}** !")

    bot.run(token)

main()
