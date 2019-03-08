from discord.ext import commands
from gitgud.gitgud import git
import io
import shlex
import sys


cleaner = commands.clean_content(fix_channel_mentions=True)

class GitGudCog(commands.Cog, name="Git Gud"):
    def __init__(self, bot):
        self.bot = bot

    def _make_command(name):
        gudcommand = getattr(git, name)

        @commands.command(name=name)
        async def command(self, ctx, *, args=""):
            args = await cleaner.convert(ctx, args)
            err = 0
            fp = io.StringIO()
            args = shlex.split(args)
            dstderr = sys.stderr
            dstdout = sys.stdout
            sys.stderr = fp
            sys.stdout = fp
            dargs = sys.argv
            sys.argv = [f"{ctx.prefix}{ctx.command.qualified_name}"] + args
            try:
                gudcommand(args, output=fp.write)
            except SystemExit as se:
                err = se.args[0]
            sys.argv = dargs
            sys.stderr = dstderr
            sys.stdout = dstdout
            s = fp.getvalue()
            if err:
                await ctx.send(f"```\nError {err}:\n{s}```")
            elif "\n" in s:
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

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("You got a ping!")


def setup(bot):
    bot.add_cog(GitGudCog(bot))
