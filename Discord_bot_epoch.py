from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from datetime import datetime
from important import token
import nextcord
import requests
import calendar
intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)
@client.event
async def on_ready():
    print("Ready")
@client.slash_command(guild_ids=[1197502933634404363])
async def hello(interaction: Interaction):
    await interaction.response.send_message(f"Hi {interaction.user.mention}!", ephemeral=True)
@client.slash_command(guild_ids=[1197502933634404363])
async def fox(interaction: Interaction):
        response = requests.get("https://randomfox.ca/floof/") 
        fox_data = response.json()
        image_url = fox_data["image"]
        await interaction.response.send_message(f"{image_url}")
@client.slash_command(guild_ids=[1197502933634404363])
async def dog(interaction: Interaction):
    url = f'http://shibe.online/api/shibes?count={1}&urls=true&httpsUrls=true'
    response = requests.get(url)
    data = response.json()
    for img_url in data:
        await interaction.response.send_message(img_url)
@client.slash_command(guild_ids=[1197502933634404363])
async def cat(interaction: Interaction):
    url = f'http://shibe.online/api/cats?count={1}&urls=true&httpsUrls=true'
    response = requests.get(url)
    data = response.json()
    for img_url in data:
        await interaction.response.send_message(img_url)
@client.slash_command(guild_ids=[1197502933634404363])
async def bird(interaction: Interaction):
    url = f'http://shibe.online/api/birds?count={1}&urls=true&httpsUrls=true'
    response = requests.get(url)
    data = response.json()
    for img_url in data:
        await interaction.response.send_message(img_url)
@client.slash_command(guild_ids=[1197502933634404363], description="Write in UTC 0 timezone")
async def epoch(interaction: Interaction, choice: int = SlashOption(name="mode", choices={"short time": 1, "long time": 2, "short date": 3, "long date": 4, "long date with short time": 5,
 "long date with day of week": 6, "relative": 7, "print out unix time": 8})
 ,date: int=-1, month: int=-1, year: int=-1, hours: int=-1, minutes: int=-1, seconds: int=-1):
    if(hours == -1): hours = datetime.utcnow().hour
    if(date == -1): date = datetime.utcnow().day
    if(year == -1): year = datetime.utcnow().year
    if(month == -1): month = datetime.utcnow().month
    if(minutes == -1): minutes = datetime.utcnow().minute
    if(seconds == -1): seconds = datetime.utcnow().second
    t=datetime(year, month, date, hours, minutes, seconds)
    time = str(calendar.timegm(t.timetuple()))
    match choice:
        case 1:
            await interaction.response.send_message("<t:"+time+":t>")
        case 2:
            await interaction.response.send_message("<t:"+time+":T>")
        case 3:
            await interaction.response.send_message("<t:"+time+":d>")
        case 4:
            await interaction.response.send_message("<t:"+time+":D>")
        case 5:
            await interaction.response.send_message("<t:"+time+":f>")
        case 6:
            await interaction.response.send_message("<t:"+time+":F>")
        case 7:
            await interaction.response.send_message("<t:"+time+":R>")
        case _:
            await interaction.response.send_message(time)
client.run(token)