import discord
from discord.ext.commands import Bot

TOKEN = "NjgwODUzMzk4MTU3MTMxODc1.XlGcoQ.CdjlCK_w_MjrgqVnGbTV0cuJiE8"

client = discord.Client()
bot = Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Bot Hazır " + str(bot.user))


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "selam":
        await message.channel.send("selam naber")


bot.run(TOKEN)

