import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="git ", description="Git Gud - a utility for when you are told to 'git gud'")
bot.load_extension("gitgud_discord")

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    await bot.change_presence(activity=discord.Game(name="Git Gud (https://github.com/kaeptmblaubaer1000/gitgud2)"))
    print('Successfully set rich presence')

with open("bot_token.txt", "r") as fp:
    token = fp.read().strip()
bot.run(token)
