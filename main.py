import os, datetime, time, asyncio
import pytz as tz

import discord 

from dotenv import load_dotenv 
from discord.ext import commands 

load_dotenv()

#Intents for accessing members in guild
intents = discord.Intents.default()
intents.members = True
#timezones for accurate times
easternTimeZone = tz.timezone("US/Eastern")

#initialize bot
bot = commands.Bot(command_prefix = "!", intents=intents)

#bot event ran when bot is ready. Calls church closed and open commands to start ticking
@bot.event
async def on_ready():
  print(f"{bot.user.name} is online")
  await schedule_church_Closed()
  await schedule_church_Open()


async def schedule_church_Open():
  while True:
    
    now = datetime.datetime.now(easternTimeZone) #get current time 
    then = now + datetime.timedelta(days=1)#get 1 day later from that time
    then.replace(hour = 8, minute = 0)#at 8am 
    wait_time = (then-now).total_seconds()#get seconds between those 2 times
    await asyncio.sleep(wait_time)
    chan = bot.get_channel(819705056538132503)
    await chan.send("Church is open!")
    await Add_Roles()


async def Add_Roles():
  guild = bot.get_guild(819705056076496958)
  role = guild.get_role(983636293193973782) #closed church role
  role2 = guild.get_role(980470728182886460)#open church role
  for member in role.members:
     chan = bot.get_channel(819705056538132503)
     await chan.send(member.display_name)
     await member.remove_roles(role)
     await member.add_roles(role2)
    
async def schedule_church_Closed():
  while True:
    
    now = datetime.datetime.now(easternTimeZone)
    then = now + datetime.timedelta(days=1)
    then.replace(hour = 20, minute = 0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)
    chan = bot.get_channel(819705056538132503)
    await chan.send("Church is closed!")
    await Remove_Roles()


async def Remove_Roles():
  guild = bot.get_guild(819705056076496958) 
  role = guild.get_role(980470728182886460) #open church role
  role2 = guild.get_role(983636293193973782) #closed church role
  for member in role.members:
     chan = bot.get_channel(819705056538132503)
     await chan.send(member.display_name)
     await member.remove_roles(role)
     await member.add_role(role2)
  

  
TOKEN = os.environ['Discord_Token']

bot.run(TOKEN)





