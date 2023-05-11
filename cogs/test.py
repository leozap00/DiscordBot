import discord
from discord import app_commands
from discord.ext import commands


class test(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="introduce",
        description="Introduce Yourself!")
    async def introduce(
            self,
            interaction: discord.Interaction,
            age: int) -> None:
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name="Prova!", value="Prova")
        await interaction.response.send_message(
            f"My name is {interaction.user.name} and my age is {age}", embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        test(bot),
        guilds=[discord.Object(id=956957033767239701)]
    )
