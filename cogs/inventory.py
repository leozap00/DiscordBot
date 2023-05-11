import sqlite3

import discord
from discord import app_commands
from discord.ext import commands



class Inventory(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    @app_commands.command(
        name="profilo",
        description="Visualizza il tuo profilo."
    )
    async def profile(self, interaction: discord.Interaction) -> None:
        try:
            db = sqlite3.connect("main.db")
            with db:
                cursor = db.cursor()
                print("Database Connesso!")
                name = interaction.user.name
                cursor.execute(f'SELECT * FROM membri WHERE name = "{name}" ')
                row = cursor.fetchone()
                cursor.close()
        except sqlite3.Error as error:
            print("Errore durante connessione a sqlite", error)
        finally:
            if db:
                db.close()
                print("La connessione a SQLite è terminata")

        name = interaction.user.name

        em = discord.Embed(title=f"Il profilo di {name}", color=interaction.user.color)
        em.set_thumbnail(url='{}'.format(interaction.user.display_avatar))
        em.add_field(name="profilo creato il", value=row[2])
        await interaction.response.send_message(embed=em)

    @app_commands.command(
        name="box",
        description="Visualizza i pokemon catturati."
    )
    async def pokemon(self, interaction: discord.Interaction) -> None:
        try:
            db = sqlite3.connect("main.db")
            with db:
                cursor = db.cursor()
                print("Database Connesso!")
                name = interaction.user.name
                cursor.execute(f'SELECT * FROM membri WHERE name = "{name}" ')
                row = cursor.fetchone()
                cursor.close()
        except sqlite3.Error as error:
            print("Errore durante connessione a sqlite", error)
        finally:
            if db:
                db.close()
                print("La connessione a SQLite è terminata")
        pkmn = row[4]

        em = discord.Embed(title=f"I pokémon di {name}", color=interaction.user.color)
        em.set_thumbnail(url="https://icon-library.com/images/pokeball-icon-png/pokeball-icon-png-27.jpg")
        em.add_field(name='Pokémon:', value=pkmn)
        await interaction.response.send_message(embed=em)


"""
        @pag.embed_generator(max_chars=2048)
        def cooler_embed(paginator, page, page_index):
            em = discord.Embed(title=f"I pokémon di {name}", color=interaction.user.color)
            em.set_thumbnail(url="https://icon-library.com/images/pokeball-icon-png/pokeball-icon-png-27.jpg")
            em.add_field(name='Pokémon:', value=pkmn)
            return em

        nav = pag.EmbedNavigatorFactory(factory=cooler_embed, max_lines=10, suffix='\n')

        nav += pkmn

        nav.start(interaction)
"""

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Inventory(bot),
        guilds=[discord.Object(id=956957033767239701)]
    )