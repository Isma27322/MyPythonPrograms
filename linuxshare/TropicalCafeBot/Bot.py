import discord
from discord import app_commands
from discord.ext import commands
import random
from fuzzywuzzy import fuzz



def read_bot_token():
  with open('token.txt', 'r') as file:
    return file.read().strip()
  
BOT_TOKEN = read_bot_token()
BAN_LOGS_CHANNEL_ID = 1207131101164740678
KICK_LOGS_CHANNEL_ID = 1207131160212279410
WARN_LOGS_CHANNEL_ID = 1207131272485412866
REQUIRED_ROLES_FOR_ADMIN_COMMANDS = ["Bot Maker", "˚<.`| Founder |`.>˚", "˚-.| Co-Founder |.-˚","Moderators"]
REQUIRED_ROLES_FOR_SAY_COMMAND = ["Bot Maker", "˚-.| Co-Founder |.-˚","Moderators"]


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
  print("Hello world")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)


@bot.tree.command(name="inspirational_or_humorous_quote")
async def inspirational_or_humorous_quote(interation: discord.Interaction):
  quotes = []
  with open('quotes.txt', 'r') as quotesfile:
    for line in quotesfile:
      remove1 = line.strip()
      remove2 = remove1.strip("\\")
      quotes.append(remove2)
  index = random.randint(0, len(quotes) - 1)
  await interation.response.send_message(quotes[index])

@bot.tree.command(name="say", description ="Have the bot say something on your behaf!")
@app_commands.describe(thing_to_say="what should I say?")
@app_commands.describe(channel="where should I send the message?")
async def say(interation: discord.Interaction, thing_to_say: str, channel: discord.TextChannel):
  if any(role.name in REQUIRED_ROLES_FOR_SAY_COMMAND for role in interation.user.roles):
    await interation.response.send_message("The message is sent", ephemeral=True)
    await channel.send(thing_to_say)
  else:
    await interation.response.send_message("You don't have the required permissions to use this command.", ephemeral=True)



@bot.tree.command(name="ban", description="Ban a user from the server")
@app_commands.describe(user="What user would you like to ban?")
@app_commands.describe(reason="What is the reason for the ban?")
async def ban(interation: discord.Interaction, user: discord.Member, reason: str):
  if any(role.name in REQUIRED_ROLES_FOR_ADMIN_COMMANDS for role in interation.user.roles):
    await interation.response.send_message(f"I will now ban {user.mention}!", ephemeral=True)
    await user.ban(reason=reason)
    Ban_log_channel = bot.get_channel(BAN_LOGS_CHANNEL_ID)
    Ban_log_channel.send(f"User: {user.mention} was banned from the server for: {reason}")
  else:
    await interation.response.send_message("You don't have the required permissions to use this command.", ephemeral=True)


@bot.tree.command(name="kick", description="Kick a user from the server")
@app_commands.describe(user="What user would you like to kick?")
@app_commands.describe(reason="What is the reason for the kick?")
async def kick(interation: discord.Interaction, user: discord.Member, reason: str):
  if any(role.name in REQUIRED_ROLES_FOR_ADMIN_COMMANDS for role in interation.user.roles):
    await interation.response.send_message(f"I will now kick {user.mention}!", ephemeral=True)
    await user.kick(reason=reason)
    Kick_log_channel = bot.get_channel(KICK_LOGS_CHANNEL_ID)
    Kick_log_channel.send(f"User: {user.mention} was kicked from the server for: {reason}")
  else:
    await interation.response.send_message("You don't have the required permissions to use this command.", ephemeral=True)

@bot.tree.command(name="warnuser", description="Give a user a warning")
@app_commands.describe(user="What is the user you would like to warn?")
@app_commands.describe(reason="What is the reason for the warning?")
async def warnuser(interation: discord.Interaction, user: discord.Member, reason: str):
  if any(role.name in REQUIRED_ROLES_FOR_ADMIN_COMMANDS for role in interation.user.roles):
    await interation.response.send_message(f"I will now warn {user.mention} for: {reason}", ephemeral=True)
    Warn_message = f'You have just recived a warning from the server "Tropical Cafe" for the reason: \n\n'
    Warn_message = Warn_message + f"{reason} \n\n If you think this is a mistake please feel free to reach out to a member of the moderation team there!"
    await user.send(Warn_message)
    Warn_log_channel = bot.get_channel(WARN_LOGS_CHANNEL_ID)
    await Warn_log_channel.send(f"The user {user.mention} just recived a warning for the reason: {reason}")
  else:
    await interation.response.send_message("You don't have the required permissions to use this command.", ephemeral=True)

@bot.tree.command(name="rps", description= "Play rock paper scissors against the bot")
@app_commands.describe(choices = "What would you like to play Rock, Paper, Or scissors?")
@app_commands.choices(choices=[
    discord.app_commands.Choice(name="Rock", value=1),
    discord.app_commands.Choice(name="Paper", value=2),
    discord.app_commands.Choice(name="Scissors", value=3)
])
async def rockpaperscissors(interaction: discord.Interaction, choices: discord.app_commands.Choice[int]):
  bot_choices_for_rps = ["Rock","Paper","Scissors"]
  bot_choice_int = random.randint(0, len(bot_choices_for_rps) - 1)
  bot_choice = bot_choices_for_rps[bot_choice_int]
  user_choice = choices.name
  if bot_choice == "Rock" and user_choice == "Rock":
    await interaction.response.send_message("It is a tie we both chose Rock")
  elif bot_choice == "Paper" and user_choice == "Paper":
    await interaction.response.send_message("It is a tie we both chose Paper")
  elif bot_choice == "Scissors" and user_choice == "Scissors":
    await interaction.response.send_message("It is a tie we both chose Scissors")
  elif bot_choice == "Paper" and user_choice == "Rock":
    await interaction.response.send_message("I win! You choice Rock and I chose Paper, Rock beats paper")
  elif bot_choice == "Rock" and user_choice == "Paper":
    await interaction.response.send_message("You win! You chose Paper and I chose Rock, Rock beats paper")
  elif bot_choice == "Scissors" and user_choice == "Rock":
    await interaction.response.send_message("You win! You chose Rock and I chose Scissors, Rock beats Scissors")
  elif bot_choice == "Rock" and user_choice == "Scissors":
    await interaction.response.send_message("I win! You chose scissors and I chose Rock, Rock beats Scissors")
  elif bot_choice == "Paper" and user_choice == "Scissors":
    await interaction.response.send_message("You win! You chose Scissors and I chose Paper, Scissors beats paper")
  elif bot_choice == "Scissors" and user_choice == "Paper":
    await interaction.response.send_message("I win! You chose Paper and I chose Scissors, Scissors beats paper")
  else:
    await interaction.response.send_message(f"If you are seeing this message there is part of the code that still needs to be added. The bot choice was: {bot_choice} and the user choice was: {user_choice} Please aleart the creator of the bot so that they can fix this issue!")









bot.run(BOT_TOKEN)

