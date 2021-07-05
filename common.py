# common.py
import discord
import discord.ext.commands as commands
import os
import random
from pathlib import Path
from types import SimpleNamespace
from PIL import Image, ImageDraw, ImageFont
import json

bot = commands.Bot(command_prefix='.')

emojis = SimpleNamespace(
    check="✅",
    x="❌",
    error="⚠️",
    question="❓",
    deny="⛔",
    bangbang="‼️",
    restart="🔄",
    sub="➖",
    add="➕",
    down="⤵️",
    zero=u"\U0001F534",
    one=u"\U0001F7E3"
)

TS = "%Y-%m-%d - %H:%M:%S"      

botid = 761705590203351102
owners_uids = [243901171121651712, 154766122317643776]

async def add_react(msg: discord.Message, react:str):
    try:
        await msg.add_reaction(react)
    except discord.Forbidden:
        print(f"[!!] Missing permissions to add reaction in '{msg.guild.id}/{msg.channel.id}'!")
    
async def check_if_owner(ctx: commands.Context):
    with open(Path(f'options/botconfig.json')) as botconf:
        data = json.loads(botconf.read())
        if ctx.author.id in data['owners_uids']:
            return True
        raise commands.NotOwner

def colorgen(h1, h2, he1, he2, s1, s2, v1, v2):
    h,s,v = random.randrange(h1, h2, 1), random.randrange(s1, s2, 1) / 360, random.randrange(v1, v2, 1) / 360
    while h in range(he1, he2, 1):
        h = random.randrange(h1, h2, 1)
    h = h / 360
    return h, s, v

def hexcolorgen():
    acolor = "#" + str(hex(random.randint(0, 255)))[2:].zfill(2) + str(hex(random.randint(0, 255)))[2:].zfill(2) + str(hex(random.randint(0, 255)))[2:].zfill(2)
    acolor = str(acolor.upper())
    return acolor

def colorimgcreate(col):
    image = Image.new("RGBA", (125, 75), (int(col[1:3], 16), int(col[3:5], 16), int(col[5:7], 16), 255))
    txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype(os.path.join("assets", "Lato-BoldItalic.ttf"), 25)
    d = ImageDraw.Draw(txt)
    
    W, H = (125,70)
    w, h = d.textsize(col, font=fnt)
    
    d.text(((W-w)/2+3,(H-h)/2 + 15), col, font=fnt, fill=(150, 150, 150, 200))
    d.text(((W-w)/2+3,(H-h)/2 - 15), col, font=fnt, fill=(150, 150, 150, 200))
    d.text(((W-w)/2,(H-h)/2 + 15), col, font=fnt, fill=(0, 0, 0, 255))
    d.text(((W-w)/2,(H-h)/2 - 15), col, font=fnt, fill=(255, 255, 255, 255))
    
    out = Image.alpha_composite(image, txt)
    
    return out