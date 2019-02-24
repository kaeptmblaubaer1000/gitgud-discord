from discord.ext import commands
from gitgud.gitgud import git
import io
import shlex

class GitGudCog(commands.Cog, name="Git Gud"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gud")
    async def gud(self, ctx, *, args=""):
        fp = io.StringIO()
        args = shlex.split(args)
        git.gud(args, output=fp.write)
        if "--super" in args:
            await ctx.send(f"```\n{fp.getvalue()}\n```")
        else:
            await ctx.send(fp.getvalue())

def setup(bot):
    bot.add_cog(GitGudCog(bot))
