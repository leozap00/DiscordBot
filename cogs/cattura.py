import datetime

import discord
from discord import app_commands
from discord.ext import commands
import sqlite3
import os
import random
import traceback


class Cattura(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="cattura",
        description="Cattura un Pokémon!")
    @app_commands.checks.cooldown(1, 60, key=lambda i: (i.user.id))
    async def cattura(self, interaction: discord.Interaction) -> None:

        try:
            db = sqlite3.connect("main.db")
            with db:
                cursor = db.cursor()
                print("Database Connesso!")
            shiny = os.listdir('./pokemon/Shiny/')
            lgnd = os.listdir('./pokemon/Legend/')
            fileList = ['nrm', 'shiny', 'lgnd']
            weights = [97, 0.02, 1]
            choices = random.choices(fileList, weights=weights)
            if choices == ['nrm']:
                cmn = os.listdir('./pokemon/Normal/Common/')
                ucmn = os.listdir('./pokemon/Normal/Uncommon/')
                rr = os.listdir('./pokemon/Normal/Rare/')
                filesList = ['cmn', 'ucmn', 'rr']
                weights = [94, 5, 1]
                choices = random.choices(filesList, weights=weights)
                if choices == ['cmn']:
                    imgString = random.choice(cmn)  # Selects a random element from the list
                    path = "./pokemon/Normal/Common/" + imgString
                    Name = os.path.splitext(imgString)[0]
                    embed = discord.Embed(color=discord.Color.blue())

                    embed.set_image(url=f"attachment://{imgString}")
                    embed.add_field(name="**Ecco un nuovo pokemon!**", value=f" **{Name}**")
                    name = interaction.user.name
                    pokemon = f'{Name}'
                    cursor.execute(f"SELECT name FROM membri")
                    row = cursor.fetchall()
                    for each_value in row:
                        if each_value[0] == name:
                            cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                            prow = cursor.fetchone()
                            pkmn = prow[0]
                            if pokemon in pkmn:
                                print("bisogna aggiungere il numero di pokemon già presi")
                                print("pokemon già preso")
                            else:
                                pkmn = prow[0] + ' \n ' + pokemon
                                cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                                print("nuovo pokemon")

                            await interaction.response.send_message(file=discord.File(path), embed=embed)
                            break

                    else:
                        print("questo profilo non esiste!")
                        await interaction.response.edit_message("Non hai un profilo! Per creare un profilo fai !crea.")

                elif choices == ['ucmn']:
                    imgString = random.choice(ucmn)  # Selects a random element from the list
                    path = "./pokemon/Normal/Uncommon/" + imgString
                    Name = os.path.splitext(imgString)[0]
                    embed = discord.Embed(color=discord.Color.orange())

                    embed.set_image(url=f"attachment://{imgString}")
                    embed.add_field(name="**Ecco un nuovo pokemon!**", value=f" **{Name}**")
                    name = interaction.user.name
                    pokemon = f'{Name}'
                    cursor.execute(f"SELECT name FROM membri")
                    row = cursor.fetchall()
                    for each_value in row:
                        if each_value[0] == name:
                            cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                            prow = cursor.fetchone()
                            pkmn = prow[0]
                            if pokemon in pkmn:
                                print("bisogna aggiungere il numero di pokemon già presi")
                            else:
                                pkmn = prow[0] + ' \n ' + pokemon
                                cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            await interaction.response.send_message(file=discord.File(path), embed=embed)
                            break
                    else:
                        print("questo profilo non esiste!")
                        await interaction.response.edit_message("Non hai un profilo! Per creare un profilo fai !crea.")

                elif choices == ['rr']:
                    imgString = random.choice(rr)  # Selects a random element from the list
                    path = "./pokemon/Normal/Rare/" + imgString
                    Name = os.path.splitext(imgString)[0]
                    embed = discord.Embed(color=discord.Color.dark_green())

                    embed.set_image(url=f"attachment://{imgString}")
                    embed.add_field(name="**Ecco un nuovo pokemon!**", value=f" **{Name}**")
                    name = interaction.user.name
                    pokemon = f'{Name}'
                    cursor.execute(f"SELECT name FROM membri")
                    row = cursor.fetchall()
                    for each_value in row:
                        if each_value[0] == name:
                            cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                            prow = cursor.fetchone()
                            pkmn = prow[0]
                            if pokemon in pkmn:
                                print("bisogna aggiungere il numero di pokemon già presi")
                            else:
                                pkmn = prow[0] + ' \n ' + pokemon
                                cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                            await interaction.response.send_message(file=discord.File(path), embed=embed)
                            break
                    else:
                        print("questo profilo non esiste!")
                        await interaction.response.edit_message("Non hai un profilo! Per creare un profilo fai !crea.")

            elif choices == ['shiny']:
                imgString = random.choice(shiny)
                path = "./pokemon/Shiny/" + imgString
                Name = os.path.splitext(imgString)[0]
                embed = discord.Embed(color=discord.Color.gold())

                embed.set_image(url=f"attachment://{imgString}")
                embed.add_field(name="**Ecco un nuovo pokemon!**", value=f" **{Name}**")
                name = interaction.user.name
                pokemon = f'{Name}'
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pokemon in pkmn:
                            print("bisogna aggiungere il numero di pokemon già presi")
                        else:
                            pkmn = prow[0] + ' \n ' + pokemon
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                        await interaction.response.send_message(file=discord.File(path), embed=embed)
                        break
                else:
                    print("questo profilo non esiste!")
                    await interaction.response.edit_message("Non hai un profilo! Per creare un profilo fai !crea.")

            elif choices == ['lgnd']:
                imgString = random.choice(lgnd)
                path = "./pokemon/Legend/" + imgString
                Name = os.path.splitext(imgString)[0]
                embed = discord.Embed(color=discord.Color.purple())

                embed.set_image(url=f"attachment://{imgString}")
                embed.add_field(name="**Ecco un nuovo pokemon!**", value=f" **{Name}**")
                name = interaction.user.name
                pokemon = f'{Name}'
                cursor.execute(f"SELECT name FROM membri")
                row = cursor.fetchall()
                for each_value in row:
                    if each_value[0] == name:
                        cursor.execute(f"SELECT pokemon FROM membri WHERE name = '{name}'")
                        prow = cursor.fetchone()
                        pkmn = prow[0]
                        if pokemon in pkmn:
                            print("bisogna aggiungere il numero di pokemon già presi")
                        else:
                            pkmn = prow[0] + ' \n ' + pokemon
                            cursor.execute(f"UPDATE membri SET 'pokemon' =? WHERE name=?", (pkmn, name))
                        await interaction.response.send_message(file=discord.File(path), embed=embed)
                        break
                else:
                    print("questo profilo non esiste!")
                    await interaction.response.edit_message("Non hai un profilo! Per creare un profilo fai !crea.")

            db.commit()
            cursor.close()

        except sqlite3.Error:
            print("Errore durante connessione a sqlite:", traceback.format_exc())

        finally:
            if db:
                db.close()
                print("La connessione a SQLite è terminata")

    @cattura.error
    async def catturaError(
            self,
            interaction: discord.Interaction,
            error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            timeRemaining = str(datetime.timedelta(seconds=int(error.retry_after)))
            await interaction.response.send_message(
                f"Attendi ancora {timeRemaining} secondi per utilizzare il comando di nuovo.",
                ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Cattura(bot),
                      guilds=[discord.Object(id=956957033767239701)])
