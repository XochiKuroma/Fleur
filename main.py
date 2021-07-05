# main.py
import discord
from discord.utils import get
from discord.ext import commands

import os
import sys
import json
import shutil

from pathlib import Path
from dotenv import load_dotenv
from types import SimpleNamespace

import common as cmn

os.chdir(Path(os.path.abspath(sys.path[0])))

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)
bot.fleur = SimpleNamespace()
bot.fleur.gcfg = {}
bot.fleur.cfg = {}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

initial_cogs = ['cogs.core', 'cogs.admin', 'cogs.silly', 'cogs.log', 'cogs.customcolor', 'cogs.roles', 'cogs.utilities']

@bot.command(name="reload", aliases=["rl"])
@commands.check(cmn.check_if_owner)
async def reload(ctx):
    await cmn.add_react(ctx.message, cmn.emojis.restart)
    for guild in bot.guilds:
        guildid = str(guild.id)
        with open(Path(f'options/{guildid}.json')) as guildconf:
            data = json.loads(guildconf.read())
            data = {int(guildid): data}
            bot.fleur.gcfg.update(data)

    if __name__ =='__main__':
        cogsloaded = []
        out = ', '
        for cog in initial_cogs:
            bot.unload_extension(cog)
        for cog in initial_cogs:
            bot.load_extension(cog)
            cogsloaded.append(cog)
        if cogsloaded:
            out = out.join(cogsloaded)
        else:
            out = 'None.'
        print(f'\nCogs reloaded: {out}')
    await cmn.add_react(ctx.message, cmn.emojis.check)
        
@bot.event
async def on_connect():
    print(f'{bot.user.name} initializing...')

@bot.event
async def on_ready():
    print(f'{bot.user.name} initialized.')
    try:
        f = open('restart.json', 'r+')
        g = json.load(f)
        message = await bot.get_guild(g['guildid']).get_channel(g['channelid']).fetch_message(g['messageid'])
        await cmn.add_react(message, cmn.emojis.check)
        f.close()
    except:
        pass

    if os.path.exists('restart.json'): 
        os.remove('restart.json')
    
    if __name__ =='__main__':
        cogsloaded = []
        out = ', '
        for cog in initial_cogs:
            bot.load_extension(cog)
            cogsloaded.append(cog)
        if cogsloaded:
            out = out.join(cogsloaded)
        else:
            out = 'None.'
        print(f'\nCogs loaded: {out}')

    with open(Path(f'options/botconfig.json')) as botconf:
        data = json.loads(botconf.read())
        bot.fleur.cfg.update(data)

    for guild in bot.guilds:
        guildid = str(guild.id)
        if not Path(f'options/{guildid}.json').exists():
            shutil.copy(Path('options/defaultconf.json'), Path(f'options/{guildid}.json'))
            with open(Path(f'options/{guildid}.json'), 'r+') as guildconf:
                data = json.loads(guildconf.read())
                data["guildname"] = guild.name
                data["guildid"] = guildid
                data["botid"] = str(bot.fleur.cfg['botid'])

                guildconf.seek(0)
                guildconf.truncate()
                json.dump(data, guildconf)
        with open(Path(f'options/{guildid}.json')) as guildconf:
            data = json.loads(guildconf.read())
            data = {int(guildid): data}
            bot.fleur.gcfg.update(data)

bot.run(TOKEN)
