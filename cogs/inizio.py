import sqlite3
from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands


class Inizio(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="pokestart",
        description="Viene creato il profilo e mostra il messaggio iniziale per tuffarsi in una nuova avventura"
    )
    async def crea(self, interaction: discord.Interaction) -> None:
        name = interaction.user.name
        user_id = interaction.user.id
        now = datetime.now()
        join_server_date = now.strftime("%m/%d/%Y")
        try:
            db = sqlite3.connect("main.db")
            with db:
                cursor = db.cursor()
                print("Database Connesso!")

                cursor.execute(
                    f"INSERT INTO membri(user_id, name, join_server_date) VALUES ('{user_id}', '{name}', '{join_server_date}')")

                await interaction.response.send_message(
                    (f"Profilo aggiunto **{name}**! Ora puoi usare"
                     " `/profile` per vedere il tuo profilo!"
                     )
                )

                db.commit()
                cursor.close()

                print(f"Aggiunto {name} al database")

        except sqlite3.Error as error:
            print("Errore durante connessione a sqlite:", error)
            if print:
                await interaction.response.send_message("Profilo già esistente")

        finally:
            if db:
                db.close()
                print("La connessione a SQLite è terminata")

    async def inizia(self, interaction: discord.Interaction) -> None:

        name = interaction.user.name
        em = discord.Embed(title=f"Ciao {name} !", color=discord.Color.blue())
        em.add_field(name="Benvenuto nel mondo pokémon", value=(
            "Per iniziare a catturare i tuoi pokemon usa il comando `/prendi <pokemon>`.Ad esempio: /prendi "
            "Charmander`."))
        em.add_field(name='I Generazione "Kanto" :', value="Bulbasaur | Charmander | Squirtle", inline=False)

        em.add_field(name='II Generazione "Johto" :', value="Chikorita | Cyndaquil | Totodile", inline=False)

        em.add_field(name='III Generazione "Hoenn" :', value="Treecko | Torchic | Mudkip", inline=False)
        await interaction.response.send_message(embed=em)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Inizio(bot),
        guilds=[discord.Object(id=956957033767239701)]
    )
