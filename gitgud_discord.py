from discord.ext import commands
from gitgud.gitgud import git
import io
import shlex

class GitGudCog(commands.Cog, name="Git Gud"):
    def __init__(self, bot):
        self.bot = bot

    def _make_command(name):
        gudcommand = getattr(git, name)

        @commands.command(name=name)
        async def command(self, ctx, *, args=""):
            fp = io.StringIO()
            args = shlex.split(args)
            gudcommand(args, output=fp.write)
            if "--super" in args:
                await ctx.send(f"```\n{fp.getvalue()}\n```")
            else:
                await ctx.send(fp.getvalue())
        command.__name__ = name
        return command

    gud = _make_command("gud")
    rekt = _make_command("rekt")
    spooked = _make_command("spooked")
    job = _make_command("job")
    money = _make_command("money")

def setup(bot):
    bot.add_cog(GitGudCog(bot))
