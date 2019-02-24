from discord.ext import commands

bot = commands.Bot(command_prefix="git ", description="Git Gud - a utility for when you are told to 'git gud'")
bot.load_extension("gitgud_discord")
with open("bot_token.txt", "r") as fp:
    token = fp.read().strip()
bot.run(token)
