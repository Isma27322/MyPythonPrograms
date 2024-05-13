import discord
from discord import app_commands
from discord.ext import commands

def read_bot_token():
  with open('token.txt', 'r') as file:
    return file.read().strip()
  
BOT_TOKEN = read_bot_token()
SERVER_ID = 976614776606167060
MOD_LOG_CHANEL_ID = 1195089151662497905

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Hello world")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)


keywords = ["shit","fuck","son of a bitch","cunt"]

@bot.event
async def on_message(message):
      message_text = message.content.strip().lower()
      for word in keywords :
        if word in message_text:
                # do something here, change to whatever you want
                await message.channel.purge(limit=1)
                await message.channel.send(f"Don't say that! <@!{message.author.id}>")
                sent_message = "Hello you have recived a warning from the server 'Server Isaac and Glade' the reason for the warning is:\n\n swearing \n\nif you think this is a mistake please feel free to reach out to a member of the staff there!"
                await message.author.send(sent_message)
                channel2 = bot.get_channel(MOD_LOG_CHANEL_ID)
                await channel2.send(f"There was a warning that was sent to {message.author.mention} with the message: {sent_message}")


@bot.tree.command(name="warnuser")
@app_commands.describe(user="What is the user that is geting the warning")
@app_commands.describe(message="What is the warning?")
async def dmuser(interation: discord.Interaction, user: discord.User, message: str):
  await interation.response.send_message(f"I will now send a message to {user.mention}!", ephemeral=True)
  sent_message = "Hello you have recived a warning from the server: 'Isaac and Glade' the reason for the warning is:\n\n" + message + "\n\nif you think this is a mistake please feel free to reach out to a member of the staff there!"
  await user.send(sent_message)
  channel2 = bot.get_channel(MOD_LOG_CHANEL_ID)
  await channel2.send(f"There was a message that was sent to {user.mention} with the message: {message}")


@bot.tree.command(name="ban")
@app_commands.describe(user="What user would you like to ban?")
@app_commands.describe(reason="What is the reason for the ban?")
async def ban(interation: discord.Interaction, user: discord.Member, reason: str):
  await interation.response.send_message(f"I will now ban {user.mention}!", ephemeral=True)
  await user.ban(reason=reason)
  channel2 = bot.get_channel(MOD_LOG_CHANEL_ID)
  await channel2.send(f"There was a ban that was sent to {user.mention} with the reason: {reason}")


@bot.tree.command(name="kick")
@app_commands.describe(user="What user would you like to kick?")
@app_commands.describe(reason="What is the reason for the kick?")
async def kick(interation: discord.Interaction, user: discord.Member, reason: str):
  await interation.response.send_message(f"I will now kick {user.mention}!", ephemeral=True)
  await user.kick(reason=reason)
  channel2 = bot.get_channel(MOD_LOG_CHANEL_ID)
  await channel2.send(f"There was a kick that was sent to {user.mention} with the reason: {reason}")


bot.run(BOT_TOKEN)