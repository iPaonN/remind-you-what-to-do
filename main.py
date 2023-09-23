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
    @bot.command(name='timer', help='Create a timer.', usage='<time> [s|m|h] (<message>)')
    async def knock(ctx, time, unit, *message):
        if not message:
            message = 'Time\'s up!'
        else:
            message = ' '.join(message)

        time = int(time)
        oldtime = time # time without unit calculation to seconds
        if unit == 's':
            pass
        elif unit == 'm':
            time *= 60
        elif unit == 'h':
            time *= 3600
        else:
            await ctx.send(':x: **ERROR**: Invalid unit.\nUnit can be \'s\' for seconds, \'m\' for minutes or \'h\' for hours.')
            return
        if time > 10000:
            await ctx.send(':x: **ERROR**: Timer can\'t be longer than 10000 seconds.')
            return
        await ctx.send(f':white_check_mark: Creating a timer for **{oldtime}{unit}** with message \"**{message}**\"...\nYou will get mentioned/pinged.')
        await asyncio.sleep(time)
        await ctx.send(f'{ctx.author.mention} **{message}** (**{oldtime}{unit}** passed.)')

    bot.run(token)

main()
