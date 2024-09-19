import discord
from discord.ext import commands

from pie import check, i18n, logger, utils

_ = i18n.Translator(__file__).translate
bot_log = logger.Bot.logger()
guild_log = logger.Guild.logger()


class Broadcast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @check.acl2(check.ACLevel.MOD)
    @commands.guild_only()
    @commands.group(name="broadcast")
    async def broadcast(self, ctx):
        """Send message to all guild users"""
        await utils.discord.send_help(ctx)


async def setup(bot) -> None:
    await bot.add_cog(Broadcast(bot))