import os

import discord
from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            application_id="")

    async def setup_hook(self):
        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await self.load_extension("cogs." + f[:-3])
        await bot.tree.sync(guild=discord.Object(id=""))

    async def on_ready(self):
        print(f'{self.user} si è connesso su Discord!')


bot = MyBot()

# credenziali
TOKEN = ''

bot.run(TOKEN)
