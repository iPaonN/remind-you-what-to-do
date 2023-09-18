"""TEST Reminder bot"""

import discord
from discord.ext import commands

#เอาไว้สำหรับรอรับคำสั่ง
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Run the bot
# always don't forget to remove token

def main():
    """Bot"""
    token = '' #สำหรับรันบอท

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

    bot.run(token)

#This is a test - 66070105


main()
