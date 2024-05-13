import discord
from discord import app_commands
from discord.ext import commands
import random
from fuzzywuzzy import fuzz
from webcolors import name_to_hex

def read_bot_token():
  with open('token.txt', 'r') as file:
    return file.read().strip()

BOT_TOKEN = read_bot_token()
WELCOME_CHANNEL_ID = 1233787176735739995
SERVER_ID = 1233752229346021517
REACTION_ROLES_CHANNEL_ID = 1233756544202444801
REACTION_ROLES_EMOJIS = []
REACTION_ROLES_ROLE_NAMES = []
REQUIRED_ROLES_FOR_ADMIN_COMMANDS = ["ೄྀ࿐ ˊˎ- Senior mod", "୧ ‧₊˚ 🎐 ⋅ high mod"]

with open('ReactionRoles.txt', 'r') as file:
  # Read all lines at once (check if any lines exist)
  lines = file.readlines()
  if not lines:
    print("File is empty.")
  else:
    # Find the first non-empty line (assuming headers are at the beginning)
    start_line = 0
    for line in lines:
      line = line.strip()  # Remove leading/trailing whitespace
      if line:
        has_data = True  # Set flag if any line is found (excluding headers)
        break
      start_line += 1

    # Iterate through lines starting from the first non-empty line
    for line in lines[start_line:]:
      line = line.strip()

      # Add lines with emojis (assuming "<a:" format) directly to emojis
      if line.startswith("<a:") or line.startswith("<:"):
        REACTION_ROLES_EMOJIS.append(line)  # Append the entire line (including "<a:")
      else:
        # Add non-emoji lines as role names
        REACTION_ROLES_ROLE_NAMES.append(line)
  print(REACTION_ROLES_EMOJIS)
  print(REACTION_ROLES_ROLE_NAMES)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Hello world")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

@bot.event
async def on_message(message):
  # Check if the message is from the bot or not a ping
  if message.author == bot.user or not message.mentions.__contains__(bot.user):
    return

  # Now we know it's a ping, proceed with the original logic
  await message.channel.send(f'Hello <@!{message.author.id}>!')

  def check(response_message):
    return response_message.author == message.author and response_message.channel == message.channel

  try:
    user_response = await bot.wait_for('message', check=check)  # Wait for user response for 60 seconds
  except TimeoutError:
    await message.channel.send(
      "I didn't receive your response. If you want to talk, feel free to message me anytime!"
    )
  else:
    if fuzz.ratio(user_response.content, "How are you?") > 80:
      await message.channel.send(f'I am doing good <@!{message.author.id}>! How are you?')
    def check(response_message):
      return response_message.author == message.author and response_message.channel == message.channel

    try:
      user_response = await bot.wait_for(
        'message', check=check)  # Wait for user response for 60 seconds
    except TimeoutError:
      await message.channel.send(
        "I didn't receive your response. If you want to talk, feel free to message me anytime!"
      )
    else:
      good_words = [
          'good', 'great', 'fine', 'awesome', 'amazing', 'well', 'wonderful',
          'happy', 'joyful', 'excited', 'enjoy', 'ok', 'okay', 'fantastic',
          'excellent', 'positive', 'pleased', 'satisfied', 'content',
          'delighted', 'glad', 'contented', 'elated', 'sunny', 'cheerful',
          'blissful', 'merry', 'joyous', 'thrilled', 'overjoyed', 'upbeat',
          'satisfactory', 'pleasurable', 'uplifting', 'fortunate', 'grateful',
          'radiant', 'ecstatic', 'enthusiastic', 'fulfilled', 'heartening',
          'exuberant', 'sunny', 'vibrant'
      ]
      bad_words = [
          'bad', 'not good', 'not great', 'not fine', 'not awesome',
          'not amazing', 'not well', 'not wonderful', 'sad', 'not happy',
          'terrible', 'not joyful', 'not excited', 'not enjoy', 'not ok',
          'not okay', 'unfortunate', 'disappointing', 'negative', 'unpleasant',
          'regrettable', 'upset', 'miserable', 'unhappy', 'unfortunate',
          'dismal', 'gloomy', 'dreary', 'tragic', 'mournful', 'disheartening',
          'woeful', 'heartbreaking', 'discouraging', 'depressing', 'dreadful',
          'pitiful', 'distressing', 'unfavorable', 'grieving', 'melancholy',
          'unfortunate'
      ]

      def is_similar(word1, word2):
        return fuzz.ratio(word1, word2) > 80  # Adjust the threshold as needed

      def is_good(text):
        return any(is_similar(text, word) for word in good_words)

      def is_bad(text):
        return any(is_similar(text, word) for word in bad_words)

      if is_good(user_response.content.lower()):
        await message.channel.send("That's good!")
      elif is_bad(user_response.content.lower()):
        await message.channel.send("I am sorry to hear that")
      else:
        await message.channel.send("I hope whatever is happening to you gets better!")

  await bot.process_commands(message)


@bot.event
async def on_member_join(member):
  channel = bot.get_channel(WELCOME_CHANNEL_ID)
  embed = discord.Embed(title="Welcome New User!!!!", description=f"Welcome to the discord server <@!{member.id}>!!")
  embed.add_field(name="Please read what is below!!", value="", inline=False)
  embed.add_field(name=f"Read the rules in: <#1233756767582683198>!", value="", inline=False)
  embed.add_field(name=f"Get your roles in: <#1233756544202444801>!", value="", inline=False)
  embed.add_field(name=f"Verify your account in <#1233770461029204060>!", value="", inline=False)
  with open('WelcomeImage.png', 'rb') as welcomeimage:
    welcomepicure = discord.File(welcomeimage)
  await channel.send(member.mention, embed=embed, file=welcomepicure)

@bot.tree.command(name="reactionroles", description = "Setup the reaction roles")
@app_commands.describe(roles="How many roles are there?")
async def reactionroles(interaction: discord.Interaction, roles: int):
  if any(role.name in REQUIRED_ROLES_FOR_ADMIN_COMMANDS for role in interaction.user.roles):
    await interaction.response.send_message("We will now create the reaction roles. Pay attention to the messages below this!!", ephemeral=True)
    emojis = []
    role_names = []
    command_channel_id = interaction.channel.id
    main_channel = bot.get_channel(command_channel_id)
    reaction_roles_channel = bot.get_channel(REACTION_ROLES_CHANNEL_ID)


    for i in range(roles):
      await main_channel.send(f"What is the emoji for role {i+1}?")
      def check(response_message):
        return response_message.author == interaction.user and response_message.channel == interaction.channel

      user_response = await bot.wait_for('message', check=check, timeout=60)
      if user_response:
        emojis.append(user_response.content)
        REACTION_ROLES_EMOJIS.append(user_response.content)
      else:
        await main_channel.send("I didn't receive a response. Exiting the poll setup.")
        return
      
      await main_channel.send(f"What is the the role name for that emoji that you just gave me?")
      def check(response_message):
        return response_message.author == interaction.user and response_message.channel == interaction.channel

      user_response = await bot.wait_for('message', check=check, timeout=60)
      if user_response:
        role_names.append(user_response.content)
        REACTION_ROLES_ROLE_NAMES.append(user_response.content)
      else:
        await main_channel.send("I didn't receive a response. Exiting the poll setup.")
        return

    await main_channel.purge(limit=int(roles * 4))
    with open('ReactionRoles.txt', 'a') as reactionRoles:
      for name in role_names :
        reactionRoles.write("\n")
        reactionRoles.write(name)
      for emoji in emojis :
        reactionRoles.write("\n")
        reactionRoles.write(emoji)

    
    embed = discord.Embed(title="Get your roles here!")
    for i in range(roles):
      embed.add_field(name=f"{emojis[i]} {role_names[i]}", value="", inline=False)
    rolesmessage = await reaction_roles_channel.send(embed=embed)
    for emoji in emojis:
      await rolesmessage.add_reaction(f'{emoji}')

  else:
    await interaction.response.send_message("You don't have the required permissions to use this command.", ephemeral=True)
  
  
@bot.event
async def on_raw_reaction_add(payload):
  reaction = payload.emoji  # Get the emoji object
  user = payload.member

  if payload.channel_id != REACTION_ROLES_CHANNEL_ID or payload.guild_id != SERVER_ID:
    return

  # Ignore reactions from the bot itself
  if user.bot:
    return

  # Print the emoji being reacted with and the list for debugging

  # Check if the emoji matches a configured reaction role
  if f'{reaction}' in REACTION_ROLES_EMOJIS:
    role_name = REACTION_ROLES_ROLE_NAMES[REACTION_ROLES_EMOJIS.index(f'{reaction}')]
    
    # Check if role_name is not None before assigning
    if role_name:
      role = discord.utils.get(user.guild.roles, name=role_name)
      if role:
        try:
          await user.add_roles(role)
          print(f"Assigned role '{role.name}' to {user.name}")
        except discord.HTTPException as e:
          print(f"Error assigning role: {e}")
      else:
        print(f"Role '{role_name}' not found on the server.")
      
@bot.event
async def on_raw_reaction_remove(payload):
  reaction = payload.emoji  # Get the emoji object
  user_id = payload.user_id
  guild_id = payload.guild_id

  if payload.channel_id != REACTION_ROLES_CHANNEL_ID or guild_id != SERVER_ID:
    return
  
  guild = bot.get_guild(guild_id)  # Fetch the guild object
  user = guild.get_member(user_id)  # Get the member object  

  # Ignore reactions from the bot itself
  if user.bot:
    return

  # Print the emoji being reacted with and the list for debugging

  # Check if the emoji matches a configured reaction role
  if f'{reaction}' in REACTION_ROLES_EMOJIS:
    role_name = REACTION_ROLES_ROLE_NAMES[REACTION_ROLES_EMOJIS.index(f'{reaction}')]
    
    # Check if role_name is not None before assigning
    if role_name:
      role = discord.utils.get(user.guild.roles, name=role_name)
      if role:
        try:
          await user.remove_roles(role)
          print(f"Removed role '{role.name}' to {user.name}")
        except discord.HTTPException as e:
          print(f"Error removeing role: {e}")
      else:
        print(f"Role '{role_name}' not found on the server.")

@bot.tree.command(name="ban", description="Ban a user from the server")
@app_commands.describe(user="What user would you like to ban?")
@app_commands.describe(reason="What is the reason for the ban?")
async def ban(interaction: discord.Interaction, user: discord.Member, reason: str):
  if any(role.name in REQUIRED_ROLES_FOR_ADMIN_COMMANDS for role in interaction.user.roles):
    await interaction.response.send_message(f"I will now ban {user.mention}!", ephemeral=True)
    await user.ban(reason=reason)
  else:
    await interaction.response.send_message("You don't have the required permissions to use this command.", ephemeral=True)


@bot.tree.command(name="kick", description="Kick a user from the server")
@app_commands.describe(user="What user would you like to kick?")
@app_commands.describe(reason="What is the reason for the kick?")
async def kick(interaction: discord.Interaction, user: discord.Member, reason: str):
  if any(role.name in REQUIRED_ROLES_FOR_ADMIN_COMMANDS for role in interaction.user.roles):
    await interaction.response.send_message(f"I will now kick {user.mention}!", ephemeral=True)
    await user.kick(reason=reason)
  else:
    await interaction.response.send_message("You don't have the required permissions to use this command.", ephemeral=True)

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
    await interaction.response.send_message("I win! You choice Rock and I chose Paper, Paper beats Rock")
  elif bot_choice == "Rock" and user_choice == "Paper":
    await interaction.response.send_message("You win! You chose Paper and I chose Rock, Paper beats Rock")
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

@bot.tree.command(name="purge", description="Deleate messages in a specific channel")
@app_commands.describe(num_of_messages_to_del="How many messages would you like me to delete?")
@app_commands.describe(channel="What channel should I delete the messages in?")
async def purge(interaction: discord.Interaction, num_of_messages_to_del: int, channel: discord.TextChannel):
  await interaction.response.send_message(f"I will now deleted {num_of_messages_to_del} messages in <#{channel.id}>!", ephemeral=True)
  await channel.purge(limit=int(num_of_messages_to_del))


bot.run(BOT_TOKEN)

