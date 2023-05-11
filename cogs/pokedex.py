import sqlite3

import discord
from discord import app_commands
from discord.ext import commands


class Pokedex(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="pokedex",
        description="Conosci le informazioni di un pokemon"
    )
    async def pokedex(self, interaction: discord.Interaction, pokemon: str) -> None:
        try:
            db = sqlite3.connect("main.db")
            with db:
                cursor = db.cursor()
                print("Database Connesso!")

                cursor.execute(f'SELECT * FROM pokemon WHERE pokemon = "{pokemon}"')
                row = cursor.fetchone()
                cursor.close()

        except sqlite3.Error as error:
            print("Errore durante connessione a sqlite", error)
        finally:
            if db:
                db.close()
                print("La connessione a SQLite è terminata")

        id = row[0]
        pokemon = row[1]
        em = discord.Embed(title=f"#{id} : {pokemon}", description=row[7], color=discord.Color.red())

        em.set_image(url=row[8])
        em.add_field(name="Tipo", value=row[2])
        em.add_field(name="Abilità", value=row[3])
        em.add_field(name="Categoria", value=row[4])
        em.add_field(name="Altezza", value=row[5])
        em.add_field(name="Peso", value=row[6])

        await interaction.response.send_message(embed=em)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Pokedex(bot),
        guilds=[discord.Object(id=956957033767239701)]
    )
