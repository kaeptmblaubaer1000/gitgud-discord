import discord
from discord.ext import commands
import logging
import sys
logger = logging.getLogger("gitgud_discord").getChild(__name__)
handler = logging.StreamHandler(sys.stdout)
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger(discord.__name__).setLevel(logging.INFO)

bot = commands.Bot(command_prefix=["git ", "git-", "$ git ", "$ git-", "git", "$ git"],
                   description="Git Gud - a utility for when you are told to 'git gud'")
bot.load_extension("gitgud_discord")
bot.load_extension("jishaku")
bot.load_extension("kb1000_discordpy_common")
bot.load_extension("kb1000_discordpy_common.help")


@bot.event
async def on_ready():
    print(
        f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    await bot.change_presence(activity=discord.Game(name="Git Gud (https://git.io/fhhbL or https://github.com/kaeptmblaubaer1000/gitgud-discord)"))
    print('Successfully set rich presence')
    logger.info(bot.guilds)

with open("bot_token.txt", "r") as fp:
    token = fp.read().strip()
bot.run(token)
