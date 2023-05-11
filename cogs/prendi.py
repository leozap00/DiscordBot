import sqlite3
import traceback

import discord
from discord import app_commands
from discord.ext import commands


class Prendi(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="prendi",
        description="Ottieni il tuo primo pokemon!"
    )
    async def prendi(self, interaction: discord.Interaction, pokemon: str) -> None:
        name = interaction.user.name
        try:
            db = sqlite3.connect("main.db")
            with db:
                cursor = db.cursor()
                print("Database Connesso!")
            if 'Charmander' in {pokemon}:
                chrm = discord.File("./pokemon/Normal/UnCommon/Charmander.png", filename="Charmander.png")
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_image(url=f"attachment://{chrm}")
                embed.add_field(name="**Hai ottenuto il tuo primo pokemon!**", value="Charmander")
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pkmn == None:
                            pkmn = "Charmander"
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            print("nuovo pokemon")
                        else:
                            print("pokemon già preso")
                            await interaction.response.send_message("Hai già un pokémon!")
                            break
                        await interaction.response.send_message(embed=embed, file=chrm)
                        break
            elif 'Bulbasaur' in {pokemon}:
                bulb = discord.File("./pokemon/Normal/UnCommon/Bulbasaur.png", filename="Bulbasaur.png")
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_image(url=f"attachment://{bulb}")
                embed.add_field(name="**Hai ottenuto il tuo primo pokemon!**", value="Bulbasaur")
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pkmn == None:
                            pkmn = "Bulbasaur"
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            print("nuovo pokemon")
                        else:
                            print("pokemon già preso")
                            await interaction.response.send_message("Hai già un pokémon!")
                            break
                        await interaction.response.send_message(embed=embed, file=bulb)
                        break
            elif 'Squirtle' in {pokemon}:
                sqrt = discord.File("./pokemon/Normal/UnCommon/Squirtle.png", filename="Squirtle.png")
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_image(url=f"attachment://{sqrt}")
                embed.add_field(name="**Hai ottenuto il tuo primo pokemon!**", value="Squirtle")
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pkmn == None:
                            pkmn = "Squirtle"
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            print("nuovo pokemon")
                        else:
                            print("pokemon già preso")
                            await interaction.response.send_message("Hai già un pokémon!")
                            break
                        await interaction.response.send_message(embed=embed, file=sqrt)
                        break

            elif 'Chikorita' in {pokemon}:
                ckr = discord.File("./pokemon/Normal/UnCommon/Chikorita.png", filename="Chikorita.png")
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_image(url=f"attachment://{ckr}")
                embed.add_field(name="**Hai ottenuto il tuo primo pokemon!**", value="Chikorita")
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pkmn == None:
                            pkmn = "Chikorita"
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            print("nuovo pokemon")
                        else:
                            print("pokemon già preso")
                            await interaction.response.send_message("Hai già un pokémon!")
                            break
                        await interaction.response.send_message(embed=embed, file=ckr)
                        break
            elif 'Cyndaquil' in {pokemon}:
                cyq = discord.File("./pokemon/Normal/UnCommon/Cyndaquil.png", filename="Cyndaquil.png")
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_image(url=f"attachment://{cyq}")
                embed.add_field(name="**Hai ottenuto il tuo primo pokemon!**", value="Cyndaquil")
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pkmn == None:
                            pkmn = "Cyndaquil"
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            print("nuovo pokemon")
                        else:
                            print("pokemon già preso")
                            await interaction.response.send_message("Hai già un pokémon!")
                            break
                        await interaction.response.send_message(embed=embed, file=cyq)
                        break

            elif 'Tododile' in {pokemon}:
                tdl = discord.File("./pokemon/Normal/UnCommon/Tododile.png", filename="Tododile.png")
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_image(url=f"attachment://{tdl}")
                embed.add_field(name="**Hai ottenuto il tuo primo pokemon!**", value="Tododile")
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pkmn == None:
                            pkmn = "Tododile"
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            print("nuovo pokemon")
                        else:
                            print("pokemon già preso")
                            await interaction.response.send_message("Hai già un pokémon!")
                            break
                        await interaction.response.send_message(embed=embed, file=tdl)
                        break

            elif 'Treecko' in {pokemon}:
                trk = discord.File("./pokemon/Normal/UnCommon/Treecko.png", filename="Treecko.png")
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_image(url=f"attachment://{trk}")
                embed.add_field(name="**Hai ottenuto il tuo primo pokemon!**", value="Treecko")
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pkmn == None:
                            pkmn = "Treecko"
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            print("nuovo pokemon")
                        else:
                            print("pokemon già preso")
                            await interaction.response.send_message("Hai già un pokémon!")
                            break
                        await interaction.response.send_message(embed=embed, file=trk)
                        break

            elif 'Torchic' in {pokemon}:
                trc = discord.File("./pokemon/Normal/UnCommon/Torchic.png", filename="Torchic.png")
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_image(url=f"attachment://{trc}")
                embed.add_field(name="**Hai ottenuto il tuo primo pokemon!**", value="Torchic")
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pkmn == None:
                            pkmn = "Torchic"
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            print("nuovo pokemon")
                        else:
                            print("pokemon già preso")
                            await interaction.response.send_message("Hai già un pokémon!")
                            break
                        await interaction.response.send_message(embed=embed, file=trc)
                        break

            elif 'Mudkip' in {pokemon}:
                mdk = discord.File("./pokemon/Normal/UnCommon/Mudkip.png", filename="Mudkip.png")
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_image(url=f"attachment://{mdk}")
                embed.add_field(name="**Hai ottenuto il tuo primo pokemon!**", value="Mudkip")
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pkmn == None:
                            pkmn = "Mudkip"
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            print("nuovo pokemon")
                        else:
                            print("pokemon già preso")
                            await interaction.response.send_message("Hai già un pokémon!")
                            break
                        await interaction.response.send_message(embed=embed, file=mdk)
                        break

            else:
                print("Nome errato e/o inesistente!")
                await interaction.response.send_message(
                    "Nome errato e/o inesistente!!! Controlla se hai scritto bene il nome del pokémon controllando in !inizia.")
            db.commit()
            cursor.close()

        except sqlite3.Error:
            print("Errore durante connessione a sqlite:", traceback.format_exc())

        finally:
            if db:
                db.close()
                print("La connessione a SQLite è terminata")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Prendi(bot),
                      guilds=[discord.Object(id=956957033767239701)])
