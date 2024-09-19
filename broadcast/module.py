import discord
from discord.ext import commands

from pie import check, i18n, logger

_ = i18n.Translator(__file__).translate
bot_log = logger.Bot.logger()
guild_log = logger.Guild.logger()


class Broadcast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @check.acl2(check.ACLevel.MOD)
    @commands.guild_only()
    @commands.group(name="broadcast")
    async def broadcast(self, ctx: discord.ext.commands.Context, message: str):
        """Send message to all guild users"""
        bot_counter = 0
        embed = discord.Embed(color=discord.Color.teal(), title="Zpráva z Discordu "+ str(ctx.guild.name),description="Ahoj, já jsem Bob, Discord bot z serveru "+str(ctx.guild.name)+". Někdo ti právě poslal komunitní zprávu! Divíš se, proč ti ji posílám já? Komunitní zprávy byly totiž automatizovány. Sám určitě usoudíš, že lepší je napsat jeden příkaz, než obepisovat XY lidí. ;)")
        embed.add_field(name="Zpráva od "+ str(ctx.author.name), value=message, inline=False)
        embed.set_footer(text="Pokud jsi to dočetl až sem, dej mi prosím vědět do general channelu na "+str(ctx.guild.name)+" Discord, dík...")

        for x in ctx.guild.members:
            if not x.bot:
                channel = await x.create_dm()
                await channel.send(embed=embed)
            else:
                bot_counter += 1

        await ctx.reply("Zpráva úspěšně odeslána. Pro kontrolu počet botů na serveru: "+str(bot_counter))







async def setup(bot) -> None:
    await bot.add_cog(Broadcast(bot))