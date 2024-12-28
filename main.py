from data import *
import requests
import discord
from discord.ext import commands
import random
import aiohttp
from io import BytesIO
from itertools import permutations
import json
import urllib.request
import re
from PIL import Image, ImageChops
import basics
from chatterbot import ChatBot

cords = ['18,428']

basics.test(cords=cords)

CoinStorage=[]
UIDstorage=[]

Event = ["BlackHole", "PlanetBlast", "AmethystCloud", "CoinRainPlanet", "GirlsOnlyPlanet", "ShipBlasted", "KiledByBTS", "MemerBoi", "A RabitInSpace", "FlushedYourSelf", "MinecraftNoobInToilet", "Amongus"]

slots = [":coin:",":gem:",":fire:",":ice_cube:",":jack_o_lantern:",":roll_of_paper:",":poop:",":hourglass_flowing_sand:",":crossed_swords:"]

async def update_item(item, amount, user):
    users = await get_data()
    if item not in users[str(user.id)]["inv"]:
        print(1)
        users[str(user.id)]["inv"][item] = {"amount": amount}
        with open("database.json", "w") as f:
            json.dump(users, f)
    else:
        print(0)
        users[str(user.id)]["inv"][item]["amount"] += amount
        with open("database.json", "w") as f:
            json.dump(users, f)


async def rando1():
    randoEmoji1 = random.choice(slots)
    return randoEmoji1
async def rando2():
    randoEmoji2 = random.choice(slots)
    return randoEmoji2
async def rando3():
    randoEmoji3 = random.choice(slots)
    return randoEmoji3

def full():
    money = random.randrange(100,1000)
    return money
def half():
    money = random.randrange(50,200)
    return money

async def AddEmoji(ctx, url, messages, *, name):
    guild = ctx.guild
    if ctx.author.guild_permissions.manage_emojis_and_stickers:
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:

                try:
                    img_or_gif = BytesIO(await r.read())
                    b_value = img_or_gif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=b_value, name=name)
                        if messages == True:
                            await ctx.reply(f'Successfully Created Emoji {emoji}')
                        await ses.close()
                    else:
                        if messages == True:
                            await ctx.send(f'Error when making request | {r.status} response.')
                        await ses.close()

                except discord.HTTPException:
                    if messages == True:
                        await ctx.send('File size is too big!')

async def get_items():
    with open("items.json", "r") as f:
        users = json.load(f)
    return users

async def get_data():
    with open("database.json", "r") as f:
        users = json.load(f)
    return users

async def accounter(user):
    users = await get_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 100
        users[str(user.id)]["bank"] = 100
        users[str(user.id)]["bank space"] = 1000
        users[str(user.id)]["inv"] = {"StarterPack": {"img": "", "amount": 1}, "BankSpace": {"img": "", "amount": 1}}
    with open("database.json", "w") as f2:
        json.dump(users, f2)

async def update_bank(money, user):
    users = await get_data()
    bank = users[str(user.id)]["bank"]
    bank_space = users[str(user.id)]["bank space"]
    if money+bank > bank_space:
        ft = False
    else:
        users[str(user.id)]["bank"] += money
        with open("database.json", "w") as f3:
            json.dump(users, f3)
        ft = True
    return ft

async def update_wallet(money, user):
    users = await get_data()
    users[str(user.id)]["wallet"] += int(money)
    with open("database.json", "w") as f3:
        json.dump(users, f3)

async def random_names():
    with open("names.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split(",")))
        return random.choice(words)

def all_cmds(message):
    alls = [''.join(x) for x in permutations(list(message)+list(message.upper()), 3) if ''.join(x).lower() == message]
    for all in alls:
        if all == message:
            alls.remove(all)
    print(alls)
    return alls

intents = discord.Intents.all()
amethyst = commands.Bot(command_prefix='$', intents=intents)

@amethyst.event
async def on_ready():
    print(f"Joined discord With @{amethyst.user}")
    print(amethyst.command_prefix)

spacepic=["https://images.squarespace-cdn.com/content/v1/551a19f8e4b0e8322a93850a/1544972636400-3X0P40MZM5CQ5Q3PXDC9/Title_Image.png", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/05ae7fdf-1ed9-4261-ab43-8ae6a2e1d02a/ddfoxqx-09886676-4017-4cbf-af17-8060afcd0a64.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzA1YWU3ZmRmLTFlZDktNDI2MS1hYjQzLThhZTZhMmUxZDAyYVwvZGRmb3hxeC0wOTg4NjY3Ni00MDE3LTRjYmYtYWYxNy04MDYwYWZjZDBhNjQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QN7t7WLkgwC9UDjEwX-FUtZaZUGZqoMjCBFV-Uqls6w", "https://pbs.twimg.com/media/FG1l17wWYAAqa6m?format=jpg&name=large", "https://pbs.twimg.com/media/DkP7527XcAAl7Pv.png", "https://pbs.twimg.com/media/EErIPZFWwAEYZBj.png", "https://pbs.twimg.com/media/FGmw_OXWQAkHHJV?format=jpg&name=large"]

@amethyst.command(name="ping")
async def ping(ctx):
    await ctx.send("pong!")

@amethyst.command(name="cat")
async def cat(ctx):
  url_cat = requests.get("https://api.thecatapi.com/v1/images/search").json()
  embed_cat = discord.Embed(title = f"**Meow!!**", description = f"**`#LoveCats`**", color = discord.Colour.purple())
  embed_cat.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar.url)
  cat = url_cat[0]['url']
  embed_cat.set_image(url = cat)
  await ctx.reply(embed = embed_cat)

@amethyst.command(name="adv", aliases=["Adv", "Adventure", "adventure"])
async def adv(ctx):
    win = True
    wait = True
    Em = discord.Embed(title=f"**`{ctx.author.name}'s` Adventure Game**", color=discord.Colour.purple())
    Em.set_image(url=random.choice(spacepic))
    Em.set_footer(text=f"Are You Sure {ctx.author} (Y / N)")
    EMBED = await ctx.reply(embed=Em)
    try:
        msg = await amethyst.wait_for("message", timeout=30)
        msg = msg.content
    except TimeoutError:
        await ctx.reply(f"You Took Too Long To Reply !!")
    if not msg == None:
        if msg.lower() == "y":
            eventchoices = ["AmethystCloud", "PlanetBlast", "Blackhole"]
            eventchoice = eventchoices[random.randint(0,2)]
            with open("adv.json", "r") as f:
                load = json.load(f)
            event = load["events"][eventchoice]
            event_msg = event["msg"]
            won_item = event["item"]
            event_msg2 = event["msg2"]
            event_footer = event["foot"]
            won = event["won"]
            event_options = event["op"]
            color = event["color"]
            color2 = event["color2"]
            amt1 = event["amt1"]
            amt2 = event["amt2"]
            if color == "r":
                color = discord.Colour.red()
                if color2 == "r":
                    color2 = discord.Colour.red()
                else:
                    color2 = discord.Colour.green()
            else:
                color = discord.Colour.green()
                if color2 == "r":
                    color2 = discord.Colour.red()
                else:
                    color2 = discord.Colour.green()
            if event_options == "None":
                wait = False
            if won == "None":
                win = False
            EMbed = discord.Embed(title=f"**`{ctx.author.name}'s` Adventure Game**", description=f"{event_msg}\n\n{event_msg2}", color=color)
            EMbed.set_footer(text=event_footer)
            newEMbed = discord.Embed(title=f"**`{ctx.author.name}'s` Adventure Game**", description=f"{event_msg}\n\n{won}", color=color2)
            await EMBED.edit(embed = EMbed)
            await update_item(won_item, amt1, ctx.author)
            if win == True:
                if wait == True:
                    try:
                        msg2 = await amethyst.wait_for("message", timeout=30)
                        msg2 = msg2.content
                    except TimeoutError:
                        msg.reply("You Took Too Long To Reply")
                    if msg2 == event_options:
                        await EMBED.edit(embed=newEMbed)
                        await update_item(won_item, amt2, ctx.author)
                else:
                    await update_item(won_item, amt2, ctx.author)



@amethyst.command(name="AddEmoji")
async def AddEmojis(ctx, url, *, name):
    if url[0:4] != "http":
        print(1)
        url = discord.emoji.emojize(url)
        url = url.url
    else:
        print(0)
        pass
    print(url)
    await AddEmoji(ctx=ctx, url=url, messages=True, name=name)

@amethyst.command(name="RemoveEmoji")
async def DeleteEmoji(ctx, emoji: discord.Emoji):
	if ctx.author.guild_permissions.manage_emojis:
		await ctx.send(f'Successfully deleted : {emoji}')
		await emoji.delete()

@amethyst.command(name="ChangePic")
async def ChangePic(ctx, emoji: discord.Emoji, *,url):
    if ctx.author.guild_permissions.manage_emojis_and_stickers:
        await ctx.reply(f'Successfully Changed Emoji Photo')
        name = emoji.name
        await AddEmoji(ctx=ctx, url=url, messages=False, name=name)
        await emoji.delete()

@amethyst.command(name="RenameEmoji")
async def RenameEmoji(ctx, emoji: discord.Emoji, *, Name):
    if ctx.author.guild_permissions.manage_emojis_and_stickers:
        await ctx.reply(f'Successfully renamed : {emoji.name} to {Name}')
        url = emoji.url
        await AddEmoji(ctx=ctx, url=url, messages=False, name=Name)
        await emoji.delete()

@amethyst.command(name="Slots", aliases=["slots", "slot", "Slot"])
async def Slots(ctx, bet):
    account = await accounter(ctx.author)
    users = await get_data()
    wallet = users[str(ctx.author.id)]["wallet"]
    bank = users[str(ctx.author.id)]["bank"]
    breaker = True
    try:
        bet = int(bet)
    except:
        await ctx.reply("The Bet Should Be A Integer")
    if bet < 49:
        await ctx.reply(f"Im Sorry But The Bet Should Be Higher Than 50 gems")
        breaker = False

    if bet == None:
        await ctx.reply(f"Im Sorry But You Gotta Bet Something")
        breaker = False
    if bet > wallet:
        if bet > wallet+bank:
            await ctx.reply(f"Im Sorry But You Dont Have Enough Money In Your Bank Or Your Wallet")
        else:
            withdraw = bet-wallet
            await ctx.reply(f"Pls Withdraw More ⏣ {withdraw}")
        breaker = False
    else:
        randoEmoji1 = await rando1()
        randoEmoji2 = await rando2()
        randoEmoji3 = await rando3()
        print(randoEmoji1,randoEmoji2,randoEmoji3)
        if randoEmoji1 == randoEmoji2:
            if randoEmoji1 == randoEmoji3:
                money = bet*3
                l_or_w = "Won"
            else:
                money = bet*2
                l_or_w = "Won"
        elif randoEmoji2 == randoEmoji3:
            money = bet
            l_or_w = "Won"
        elif randoEmoji1 == randoEmoji3:
            money = bet/2
            l_or_w = random.randrange(0,1)
        elif not randoEmoji1 == randoEmoji2:
            if not randoEmoji1 == randoEmoji3:
                money = bet
                l_or_w = "Lost"
        if l_or_w == 1:
            l_or_w = "Won"
        if l_or_w == 0:
            l_or_w = "Lost"
        if l_or_w == "Won":
            await update_wallet(int(money), ctx.author)
            balance = users[str(ctx.author.id)]["wallet"] + money
        elif l_or_w == "Lost":
            await update_wallet(int(f"-{money}"), ctx.author)
            balance = users[str(ctx.author.id)]["wallet"] - money
        if breaker == True:
            embed = discord.Embed(title=f"{ctx.author.name}'s slot machine results\n>>  {randoEmoji1}  {randoEmoji2}  {randoEmoji3}  <<", description=f"\n\nYou {l_or_w}  ⏣ {money}\nYour Current Balance Is {balance}\n\n")
            await ctx.reply(embed=embed)

@amethyst.command(name="Withdraw", aliases=["with", "With", "WithDraw", "AddToWallet"])
async def withdraw(ctx, coins : int):
    users = await get_data()
    wallet = users[str(ctx.author.id)]["wallet"]
    bank = users[str(ctx.author.id)]["bank"]
    if coins > bank:
        await ctx.reply(f"You Can Withdraw Only Equal (or) Less Than : ⏣ {bank}")
    else:
        await update_bank(-coins,ctx.author)
        await update_wallet(coins,ctx.author)
        await ctx.reply(f"Successfully Withdrawed ⏣ {coins} From Your Bank\n\n**Bank** : {bank-coins}   **Wallet** : {wallet+coins}")

async def convert(ctx, argument):
        try:
            invite = await ctx.bot.fetch_invite(argument)
            return invite
        except Exception as exc:
            pass

@amethyst.command(name="Deposit", aliases=["Dep", "dep", "AddToBank", "deposit"])
async def deposit(ctx, coins : int):
    users = await get_data()
    wallet = users[str(ctx.author.id)]["wallet"]
    bank = users[str(ctx.author.id)]["bank"]
    bank_space = users[str(ctx.author.id)]["bank space"]
    if coins > wallet:
        await ctx.reply(f"You Can Deposit Only Equal (or) Less Than : ⏣ {wallet}")
    else:
        ft = await update_bank(coins,ctx.author)
        if ft == False:
            await ctx.reply(f"Sorry But Your Bank Space Isn't Enough Pls Buy BankSpace Tokens To Upgrade Your Space\n\n```Command: a!buy B-Space (or) BankSpace```  ```CurrentSpace: {bank_space}```")
        elif ft == True:
            await update_wallet(-coins,ctx.author)
            await ctx.reply(f"Successfully Added ⏣ {coins} To Your Bank\n\n**Wallet** : {wallet-coins}   **Bank** : {bank+coins}")

@amethyst.command(name="Youtube", aliases=["youtube", "YT", "Yt", "yt", "Youtube Search", "url", "link", "Link", "Url"])
async def get_url_yt(ctx, *, search):
    if " " in search:
        search = search.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
    print(search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(video_ids)
    des = []
    for num in range(6):
        print(num)
        breaker=False
        url = "https://www.youtube.com/watch?v=" + video_ids[num]
        print(url)
        for i in des:
            if num == i:
                breaker = True
        if breaker == False:
            des.append(url)
        else:
            pass
    i = 0
    current = 0
    vid = des[i]
    desc = 'If Its Not This Video Type **next**'
    print(desc)
    embed = discord.Embed(title=f"Results For {search.replace('+', ' ')}", description=desc, color=discord.Colour.red())

    embed.set_image(vid)
    await ctx.send(embed=embed)
    async def givevid(i, embed):
        vid = des[i]
        desc = 'If Its Not This Video Type **next**'
        print(desc)
        em2 = vid
        await em.edit(embed=em2)
        await ctx.send(embed = em2)
    msg = await amethyst.wait_for('message', timeout=120)
    if msg.author == ctx.author:
        if msg.content.lower == 'next':
            em2 = vid
            givevid(current+1, em2)

@amethyst.command()
async def partner(ctx):
    await ctx.author.send("Pls Enter Your Server Invite Link```")
    invitelink = await amethyst.wait_for("message", timeout=120)
    print(amethyst.user.id)
    print()
    if invitelink.author.id != amethyst.user.id:
        await ctx.author.send("```Pls Enter Your Server Description```")
        description = await amethyst.wait_for("message", timeout=120)
    if invitelink.author.id != amethyst.user.id:
        await ctx.author.send("```Pls Enter Your Regards```")
        msg = await amethyst.wait_for("message", timeout=300)
    print(invitelink.author.id)
    invite_code = invitelink.content.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get('https://discordapp.com/api/invite/' + invite_code) as response:
            data = await response.text()
            json_data = json.loads(data)
            invitelink = await amethyst.fetch_guild(json_data["guild"]["id"])
    embed = discord.Embed(
        title=f"Partnership Request from {invitelink.name}",
        description=f"**Description:** {description}",
    )
    embed.set_thumbnail(url=invitelink.i)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
    partnershipreq = await amethyst.fetch_user(806744243472695296)
    print(partnershipreq)
    em = discord.Embed(title=invitelink.name, description=description, color=0x2F3136)
    em.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
    em.set_thumbnail(url=invitelink.icon._url)
    em.set_footer(text=msg, icon_url=ctx.author.avatar.url)
    await ctx.author.send(embed=embed)
    await partnershipreq.send(embed=em)

@amethyst.command(name="Shop", aliases=["shop", "shoping", "open shop"])
async def shop(ctx, item, number=1):
    data = await get_items()
    find = data["items"][item]
    if item == None:
        print(1)
    else:
        catagory = find["cat"]
        if "Buyable" in catagory:
            cost = find["cost"] * number
            users = await get_data()
            wallet = users[str(ctx.author.id)]["wallet"]
            if cost > wallet:
                await ctx.reply(f"Im Sorry But You Dont Have Enough Money to Buy `{number}x {item}`")
            else:
                await update_item(item, number, ctx.author)
                await update_wallet(-cost,ctx.author)
                em = discord.Embed(title=f"Successful {item} Purchase", description=f"{ctx.author.mention} Bought {number}x {item} And Paid `⏣ {cost}`", color=discord.Colour.purple())
                em.set_thumbnail(url=find["img"])
                em.set_footer(text=f"Thank You Do Visit Again :)", icon_url=ctx.author.avatar.url)
                await ctx.reply(embed=em)

@amethyst.command(name="Balance", aliases=["balance", "Bal", "bal", "BAL", "BALANCE"])
async def bal(ctx, user: discord.Member=None):
    if user == None:
        user = ctx.author
    account = await accounter(user)
    users = await get_data()
    wallet = users[str(user.id)]["wallet"]
    bank = users[str(user.id)]["bank"]
    em = discord.Embed(title=f"{user.name}'s balance")
    em.add_field(name="Wallet", value=f"⏣ {wallet}", inline=False)
    em.add_field(name="Bank", value=f"⏣ {bank}", inline=False)
    await ctx.reply(embed=em)

@amethyst.command(name="beg", aliases=["Beg", "BEG"])
async def beg(ctx):
    account = await accounter(user=ctx.author)
    luck = 1
    print(luck)
    if luck == 1:
        earning = random.randrange(10,100)
    else:
        earning = 0
    if not earning == 0:
        message = f"Here Beggar Take ⏣ {earning}"
        name = await random_names()
        em = discord.Embed(title=f"**{name}**", description=f"'' {message} ''", colour=discord.Colour.green())
        em.set_footer(text=f"Begged By {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=em)
    await update_wallet(earning,ctx.author)


@amethyst.command(name="snake&ladder", aliases=["s&l","snakeladder", "sl", "snl"])
async def snakenladder(ctx):
    def showsteps(start, end, same, player):
        for i in range(start-1, end):
            print(i)
            cord = cords[i]
            if player == True:
                img = Image.open("player.png")
            else:
                img = Image.open("enemy.png")
            img = img.convert("RGBA")
            img = Image.Image.resize(img, (46,46))
            background = Image.open("snl.webp")
            background = background.convert("RGBA")
            if same == True:
                x,y = cord[1:-1].split(",")
                x = float(x)+2
                y = float(y)+2
                cord = (int(x),int(y))
            Image.Image.paste(background, img, cord)
            background.save('output.png',"PNG")

    def check(author):
        def inner_check(message):
            return message.author == author
        return inner_check
    pos = 1
    enemypos = 1
    endgame = False
    activesprt = ['97:78', '95:56', '88:24', '80:99', '71:92', '62:18', '50:67', '48:26', '36:6', '32:10', '21:42', '28:76', '1:38', '4:14']
    embed = discord.Embed(title="Type 'R' To Roll", color=discord.Color.dark_purple())
    #embed.setImage(url='')
    await ctx.reply(embed=embed)
    while endgame == False:
        same = False
        if enemypos == pos:
            same = True
        msg = await amethyst.wait_for('message', timeout=120)
        if msg.author == ctx.author:
            if msg.content == 'R':
                number = random.randrange(1, 7)
                print(number)
                showsteps(pos, number, same, True)
                pos += number
                if enemypos == pos:
                    same = True
                number2 = random.randrange(1, 7)
                print(number2)
                showsteps(enemypos, number2, same, False)
        for asprt in activesprt:
            checkpos, endpos = asprt.split(":")


chatbot = ChatBot("Chatter")
@amethyst.command(name="talk")
async def talk(ctx, *, msg):
    while True:
        response = chatbot.get_response(msg)
        await ctx.reply(str(response))
        break

import discord
from discord.ext import commands
import youtube_dl
import random

import asyncio
import youtube_dl

from discord.ext import commands

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource (discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls (discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, amethyst):
        self.bot = amethyst

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {query}')

    @commands.command()
    async def music(self, ctx, *, url):
        """Plays from a URL (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def stream(self, ctx, *, url):
        """Streams from a URL (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    @music.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

amethyst.add_cog(Music(amethyst))
            
amethyst.run('secret-token')
