import discord
from discord import app_commands
from discord.ext import commands
from webcolors import name_to_hex


def read_bot_token():
  with open('token.txt', 'r') as file:
    return file.read().strip()

def get_hex_from_name(color_name):
  color_name_no_spaces = ""
  for char in color_name:
    if char != " ":
      color_name_no_spaces += char
  try:
    hex_code = name_to_hex(color_name_no_spaces).upper()  # Convert to uppercase for consistent format
    # Check if "#" exists and remove it before prepending "0x"
    if hex_code.startswith("#"):
      hex_code = hex_code[1:]  # Remove leading "#" if present
    return f"0x{hex_code}"  # Prepend "0x" without the "#"
  except ValueError:
    return None
  


BOT_TOKEN = read_bot_token()
SERVER_NAMES = []
SERVER_IDS = []
REACTION_ROLES_CHANNEL = []
COUNTDOWN_CHANNEL = []
REACTION_ROLES = []
BIRTHDAY_ROLE = []
WELCOME_CHANNEL = []
PERSONAL_MESSAGES_CATEGORY = []
RULES_CHANNEL = []
CARD_CHANNEL = []
WISHES_CHANNEL = []
GIFTS_CHANNEL = []
MEMORIES_CHANNEL = []

def get_server_names():
  with open('./StuffForKeeping/server_names.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      SERVER_NAMES.append(line_striped)

def get_server_ids():
  with open('./StuffForKeeping/server_ids.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      SERVER_IDS.append(line_striped)

def get_reaction_roles_channel():
  with open('./StuffForKeeping/roles_channel.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      REACTION_ROLES_CHANNEL.append(line_striped)

def get_countdown_channel():
  with open('./StuffForKeeping/countdown_channel.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      COUNTDOWN_CHANNEL.append(line_striped)

def get_birthday_role():
  with open('./StuffForKeeping/birthday_role.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      BIRTHDAY_ROLE.append(line_striped)

def get_welcome_channel():
  with open('./StuffForKeeping/welcome_channel.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      WELCOME_CHANNEL.append(line_striped)

def get_personal_messages_cat():
  with open('./StuffForKeeping/personal_messages_cat.txt','r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      PERSONAL_MESSAGES_CATEGORY.append(line_striped)

def get_rules_channel():
  with open('./StuffForKeeping/rules_channel.txt','r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      RULES_CHANNEL.append(line_striped)

def get_card_channel():
  with open('./StuffForKeeping/card_channel.txt','r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      CARD_CHANNEL.append(line_striped)

def get_wishes_channel():
  with open('./StuffForKeeping/wishes_channel.txt','r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      WISHES_CHANNEL.append(line_striped)

def get_gifts_channel():
  with open('./StuffForKeeping/gifts_channel.txt','r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      GIFTS_CHANNEL.append(line_striped)

def get_memories_channel():
  with open('./StuffForKeeping/memories_channel.txt','r') as file:
    lines = file.readlines()
    for line in lines:
      line_striped = line.strip()
      MEMORIES_CHANNEL.append(line_striped)

def get_reaction_roles(server_name):
  reaction_roles_local = []
  with open(f'./StuffForKeeping/reactionroles/{server_name}_reaction_roles.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      reaction_roles_local.append(line.strip())
    REACTION_ROLES.append(reaction_roles_local)

get_server_names()
get_server_ids()
get_reaction_roles_channel()
get_countdown_channel()
get_birthday_role()
get_welcome_channel()
get_personal_messages_cat()
get_rules_channel()
get_card_channel()
get_wishes_channel()
get_gifts_channel()
get_memories_channel()
for server in SERVER_NAMES:
  get_reaction_roles(server)
print(SERVER_NAMES)
print(SERVER_IDS)
print(REACTION_ROLES_CHANNEL)
print(COUNTDOWN_CHANNEL)
print(REACTION_ROLES)
print(BIRTHDAY_ROLE)
print(WELCOME_CHANNEL)
print(PERSONAL_MESSAGES_CATEGORY)
print(RULES_CHANNEL)
print(CARD_CHANNEL)
print(WISHES_CHANNEL)
print(GIFTS_CHANNEL)
print(MEMORIES_CHANNEL)




bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Hello world")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)
  
@bot.tree.command(name="help", description="Get help for using the bot")
async def help(interaction: discord.Interaction):
  await interaction.response.send_message("""First of all. If you don't already have the server set up or you would like the bot to set it up for you 
please run the /setup_server command.
If you use /setup_server you do not need to do /setup_bot because it will do it for you!
Then you should run the /setup_bot command to give the server stuff to the bot. 
Then you should run the /setup_roles command to set up the reaction roles.
Then you should run the /countdown when you are ready to start the countdown.
NOTE!! Please do not use the same emojis for two different roles it might break it.
Also when createing the reaction roles you only have 60 seconds for each input so don't be too slow
Also when you are createing the reaction roles don't use external emojis that arn't eather part of this server or default discord emojis as the bot can't have nitro.""", ephemeral=True)

@bot.tree.command(name="setup_server", description="Have the bot set up the server for you!")
@app_commands.describe(gender="What gender is the birthday person? Male, female, or non binary")
@app_commands.choices(gender=[
    discord.app_commands.Choice(name="Male", value=1),
    discord.app_commands.Choice(name="Female", value=2),
    discord.app_commands.Choice(name="Non Binary", value=3)
])
@app_commands.describe(favcolor="What is that persons favorite color?")
async def setup_server(interaction: discord.Interaction, gender: discord.app_commands.Choice[int], favcolor: str):
  BirthdayPersonGender = gender.name
  await interaction.response.send_message("I will now setup the server for you please stand by.", ephemeral=True)
  guild = interaction.guild
  birthday_role = ""
  await guild.create_category("Temp")
  categoryTemp = discord.utils.get(guild.categories, name="Temp")
  WelcomeChannel = await guild.create_text_channel("Welcome!", topic="Welcomeing new users!", category=categoryTemp)
  await guild.create_text_channel("Announcements", news=True, category=categoryTemp)
  CountdownChannel = await guild.create_text_channel("Countdown", topic="Countdown till their birthday", news=True, category=categoryTemp)
  RolesChannel = await guild.create_text_channel("Roles", topic="Get your roles here!", category=categoryTemp)
  Rules_channel = await guild.create_text_channel("Rules", topic="View the rules for this server here!", category=categoryTemp)
  await guild.create_category("Community")
  categoryGeneral = discord.utils.get(guild.categories, name="Community")
  await guild.create_text_channel("General", topic="General Chat", category=categoryGeneral)
  await guild.create_text_channel("Commands", topic="For running commands", category=categoryGeneral)
  await guild.create_category("Birthday stuff")
  categoryBirthday = discord.utils.get(guild.categories, name="Birthday stuff")
  CardChannel = await guild.create_text_channel("Birthday card", topic="Sign the birthday card!", category=categoryBirthday)
  WishesChannel = await guild.create_text_channel("Birthday wishes", topic="Give a wish for their birthday!", category=categoryBirthday)
  GiftsChannel = await guild.create_text_channel("Birthday gifts", topic="Give them a gift for them to enojoy on their birthday", category=categoryBirthday)
  MemoriesChannel = await guild.create_text_channel("Memories", topic="Share some of your memories with them!", category=categoryBirthday)
  categoryPersonalMessagesawait = await guild.create_category("Personal Messages")
  hex_color = get_hex_from_name(favcolor)
  color = discord.Colour(int(hex_color, 16))
  if BirthdayPersonGender == "Male":
    birthday_role = await guild.create_role(name="Birthday Boy!", mentionable=True, color=color)
  elif BirthdayPersonGender == "Female":
    birthday_role = await guild.create_role(name="Birthday Girl!", mentionable=True, color=color)
  elif BirthdayPersonGender == "Non Binary":
    birthday_role = await guild.create_role(name="Birthday Person!", mentionable=True, color=color)
  else:
    print("This is somehow not working")
  SERVER_NAMES.append(guild.name)
  SERVER_IDS.append(guild.id)
  WELCOME_CHANNEL.append(guild.name)
  WELCOME_CHANNEL.append(WelcomeChannel.id)
  COUNTDOWN_CHANNEL.append(guild.name)
  COUNTDOWN_CHANNEL.append(CountdownChannel.id)
  REACTION_ROLES_CHANNEL.append(guild.name)
  REACTION_ROLES_CHANNEL.append(RolesChannel.id)
  BIRTHDAY_ROLE.append(guild.name)
  BIRTHDAY_ROLE.append(birthday_role.name)
  PERSONAL_MESSAGES_CATEGORY.append(guild.name)
  PERSONAL_MESSAGES_CATEGORY.append(categoryPersonalMessagesawait.name)   
  RULES_CHANNEL.append(guild.name)
  RULES_CHANNEL.append(Rules_channel.id)
  CARD_CHANNEL.append(guild.name)
  CARD_CHANNEL.append(CardChannel.id)
  WISHES_CHANNEL.append(guild.name)
  WISHES_CHANNEL.append(WishesChannel.id)
  GIFTS_CHANNEL.append(guild.name)
  GIFTS_CHANNEL.append(GiftsChannel.id)
  MEMORIES_CHANNEL.append(guild.name)
  MEMORIES_CHANNEL.append(MemoriesChannel.id)
  #with open('./')
     


@bot.tree.command(name="remove_channels_and_categ", description="Remove channels and categories. For testing only!")
async def remove_channels_and_categ(interaction: discord.Interaction):
  await interaction.response.send_message("Please stand by as I do that!", ephemeral=True)
  guild = interaction.guild
  categoryTemp = discord.utils.get(guild.categories, name="Temp")
  categoryBirthday = discord.utils.get(guild.categories, name="Birthday stuff")
  categoryGeneral = discord.utils.get(guild.categories, name="Community")
  categoryPersMess = discord.utils.get(guild.categories, name="Personal Messages") 
  TempChannels = categoryTemp.channels
  BirthdayChannels = categoryBirthday.channels
  GeneralChannels = categoryGeneral.channels
  PersMessChannels = categoryPersMess.channels
  for channel in TempChannels: # We search for all channels in a loop
        try:
            await channel.delete() # Delete all channels
        except AttributeError: # If the category does not exist/channels are gone
            pass
  for channel in BirthdayChannels: # We search for all channels in a loop
        try:
            await channel.delete() # Delete all channels
        except AttributeError: # If the category does not exist/channels are gone
            pass
  for channel in GeneralChannels: # We search for all channels in a loop
        try:
            await channel.delete() # Delete all channels
        except AttributeError: # If the category does not exist/channels are gone
            pass
  for channel in PersMessChannels: # We search for all channels in a loop
        try:
            await channel.delete() # Delete all channels
        except AttributeError: # If the category does not exist/channels are gone
           pass
  await categoryTemp.delete()
  await categoryBirthday.delete()
  await categoryGeneral.delete()
  await categoryPersMess.delete()



@bot.tree.command(name="setup_bot", description="Setup the bot on this server")
@app_commands.describe(reaction_roles = "Where are the reaction roles for this server?")
@app_commands.describe(countdown_channel = "Where is the birthday countdown for this server?")
@app_commands.describe(welcome_channel="What channel would you like the people who are first joining to be sent in?")
@app_commands.describe(birthday_role="What is the role for the birthday person at this server?")
@app_commands.describe(personal_messages="What category are the personal messages in?")
@app_commands.describe(card_channel="What channel will the card signing happen?")
@app_commands.describe(wishes_channel="What channel will people send their wishes?")
@app_commands.describe(memories_channel="What channel will people use to send their memories?")
@app_commands.describe(rules_channel="What channel is used for the rules?")
@app_commands.describe(gifts_channel="What channel is used for sending gifts?")
async def setup_bot(interaction: discord.Interaction, reaction_roles: discord.TextChannel, countdown_channel: discord.TextChannel
  , welcome_channel: discord.TextChannel, birthday_role: discord.Role, card_channel: discord.TextChannel, wishes_channel: discord.TextChannel
  , memories_channel: discord.TextChannel, personal_messages: discord.CategoryChannel=None, rules_channel: discord.TextChannel=None,
  gifts_channel: discord.TextChannel=None):
  
  server = interaction.guild

  server_name = server.name  # Get the server name
  server_id = server.id

  SERVER_NAMES.append(server_name)
  SERVER_IDS.append(server_id)
  REACTION_ROLES_CHANNEL.append(server_name)
  REACTION_ROLES_CHANNEL.append(reaction_roles.id)
  COUNTDOWN_CHANNEL.append(server_name)
  COUNTDOWN_CHANNEL.append(countdown_channel.id)
  WELCOME_CHANNEL.append(server_name)
  WELCOME_CHANNEL.append(welcome_channel.id)
  if personal_messages != None:
    PERSONAL_MESSAGES_CATEGORY.append(server_name)
    PERSONAL_MESSAGES_CATEGORY.append(personal_messages.name)
  if rules_channel != None:
    RULES_CHANNEL.append(server_name)
    RULES_CHANNEL.append(rules_channel.id)
  BIRTHDAY_ROLE.append(server_name)
  BIRTHDAY_ROLE.append(birthday_role.name)
  CARD_CHANNEL.append(server_name)
  CARD_CHANNEL.append(card_channel.id)
  WISHES_CHANNEL.append(server_name)
  WISHES_CHANNEL.append(wishes_channel.id)
  if gifts_channel != None:
    GIFTS_CHANNEL.append(server_name)
    GIFTS_CHANNEL.append(gifts_channel.id)
  MEMORIES_CHANNEL.append(server_name)
  MEMORIES_CHANNEL.append(memories_channel.id)

  await interaction.response.send_message(f"You have now setup the bot", ephemeral=True)
  await bot.tree.sync()

@bot.tree.command(name="setup_roles", description = "Setup the reaction roles")
@app_commands.describe(roles="How many roles are there?")
async def setup_roles(interaction: discord.Interaction, roles: int):
  await interaction.response.send_message("We will now create the reaction roles. Pay attention to the messages below this!!", ephemeral=True)
  server = interaction.guild
  server_name = server.name
  command_channel_id = interaction.channel_id
  main_channel = bot.get_channel(command_channel_id)
  roles_channels = REACTION_ROLES_CHANNEL[REACTION_ROLES_CHANNEL.index(server_name) + 1]
  roles_channel = bot.get_channel(roles_channels)
  reaction_roles = []
  emojis = []
  role_names = []
  foundNameAlready = False

  for i in range(roles):
    await main_channel.send(f"What is the emoji for role {i+1}?")
    def check(response_message):
      return response_message.author == interaction.user and response_message.channel == interaction.channel

    user_response = await bot.wait_for('message', check=check, timeout=60)
    if user_response:
      reaction_roles.append(user_response.content)
      emojis.append(user_response.content)
    else:
      await main_channel.send("I didn't receive a response. Exiting the poll setup.")
      return
      
    await main_channel.send(f"What is the the role name for that emoji that you just gave me?")
    def check(response_message):
      return response_message.author == interaction.user and response_message.channel == interaction.channel

    user_response = await bot.wait_for('message', check=check, timeout=60)
    if user_response:
      reaction_roles.append(user_response.content)
      role_names.append(user_response.content)
    else:
      await main_channel.send("I didn't receive a response. Exiting the poll setup.")
      return

  await main_channel.purge(limit=int(roles * 4))

   
  for role_for in REACTION_ROLES:  # Iterate directly through REACTION_ROLES
    if role_for[0] == server_name:  # Check only the first element of each inner list
      foundNameAlready = True
      serverindex = REACTION_ROLES.index(role_for)
      break
    else:
      foundNameAlready = False

  if foundNameAlready: 
    for role in reaction_roles:
      REACTION_ROLES[serverindex].append(role)
  else:
    reaction_roles.insert(0, server_name)
    REACTION_ROLES.append(reaction_roles)
  
  with open(f'./StuffForKeeping/reactionroles/{server_name}_reaction_roles.txt', 'a') as file:
    for roles in reaction_roles:
      file.write(f"{roles}\n")
  
  embed = discord.Embed(title="Get your roles here!")
  for i in range(roles):
    embed.add_field(name=f"{emojis[i]} {role_names[i]}", value="", inline=False)
  rolesmessage = await roles_channel.send(embed=embed)
  for emoji in emojis:
    await rolesmessage.add_reaction(f'{emoji}')

@bot.event
async def on_raw_reaction_add(payload):
  server = bot.get_guild(payload.guild_id)  # Fetch the server object
  server_name = server.name  # Get the server name directly
  reaction = payload.emoji  # Get the emoji object
  user = payload.member  # Get the member object who reacted
  channel = bot.get_channel(payload.channel_id)  # Get the channel object

  # Find the reaction roles channel for this server
  reaction_roles_channel = None
  for channel_id in REACTION_ROLES_CHANNEL:
    if channel_id == channel.id: # Check if channel ID matches server ID
      reaction_roles_channel = bot.get_channel(channel_id)
      break  # Exit loop after finding a match

  if not reaction_roles_channel:
    print(f"Couldn't find reaction roles channel for server: {server.name}")
    return  # Exit if no reaction roles channel found

  # Check if reaction happened in the designated reaction role channel and for the correct server
  if payload.channel_id != reaction_roles_channel.id or server.id != payload.guild_id:
    print("This is failing")
    return

  # Ignore reactions from the bot itself
  if user.bot:
    print("They are a bot")
    return

  # Build the list of reaction roles for this server
  reaction_roles_local = []
  for roles in REACTION_ROLES:
    if roles[0] == server_name:
      reaction_roles_local.extend(roles[1:])  # Add all elements from index 1 onwards
      break  # Exit loop after finding a match

  # Check if the emoji matches a configured reaction role
  if f'{reaction}' in reaction_roles_local:
    role_name = reaction_roles_local[reaction_roles_local.index(f'{reaction}') + 1]

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
  user_id = payload.user_id
  guild_id = payload.guild_id
  server = bot.get_guild(payload.guild_id)  # Fetch the server object
  server_name = server.name  # Get the server name directly
  reaction = payload.emoji  # Get the emoji object
  user = payload.member  # Get the member object who reacted
  channel = bot.get_channel(payload.channel_id)  # Get the channel object

  reaction_roles_channel = None
  for channel_id in REACTION_ROLES_CHANNEL:
    if channel_id == channel.id: # Check if channel ID matches server ID
      reaction_roles_channel = bot.get_channel(channel_id)
      break  # Exit loop after finding a match



  if payload.channel_id != reaction_roles_channel.id or server.id != payload.guild_id:
    print("This is failing")
    return
  
  guild = bot.get_guild(guild_id)  # Fetch the guild object
  user = guild.get_member(user_id)  # Get the member object  

  # Ignore reactions from the bot itself
  if user.bot:
    print("They are a bot")
    return


  reaction_roles_local = []
  for roles in REACTION_ROLES:
    if roles[0] == server_name:
      reaction_roles_local.extend(roles[1:])  # Add all elements from index 1 onwards
      break  # Exit loop after finding a match

  # Check if the emoji matches a configured reaction role
  if f'{reaction}' in reaction_roles_local:
    role_name = reaction_roles_local[reaction_roles_local.index(f'{reaction}') + 1]
    
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

@bot.tree.command(name="create_personal_message", description="Create a channel for someone to create a personal message for this person!")
@app_commands.describe(user="Who is the person writing the personal message?")
@app_commands.describe(name="What would you like to name the channel?")
async def create_personal_message(interaction: discord.Interaction, user: discord.Member, name: str):
  guild = interaction.guild
  await interaction.response.send_message("I will now create that channel!", ephemeral=True)
  categoryPersMess = discord.utils.get(guild.categories, name="Persional Messages")
  birthday_boy_role = discord.utils.get(guild.roles, name="Birthday Boy!")
  overwrites = {
    guild.default_role: discord.PermissionOverwrite(send_messages=False, read_message_history=False),
    birthday_boy_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
    user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
  }

  await guild.create_text_channel(name, category=categoryPersMess, overwrites=overwrites)

@bot.event
async def on_member_join(member):
  serverName = member.guild.name
  welcome_channel_id = 0
  countdown_channel_id = 0
  reaction_roles_channel_id = 0
  rules_channel_id = 0
  rules_channel_found = False
  card_channel_id = 0
  wishes_channel_id = 0
  gifts_channel_id = 0
  gifts_channel_found = False
  memories_channel_id = 0
  index = 0
  for Welcome_channel in WELCOME_CHANNEL:
    if Welcome_channel == serverName:
      index = WELCOME_CHANNEL.index(Welcome_channel)
      welcome_channel_id = WELCOME_CHANNEL[index+1]
    else:
      continue

  for countdown_channel in COUNTDOWN_CHANNEL:
    if countdown_channel == serverName:
      index = COUNTDOWN_CHANNEL.index(countdown_channel)
      countdown_channel_id = COUNTDOWN_CHANNEL[index+1]
    else:
      continue

  for roles_channel in REACTION_ROLES_CHANNEL:
    if roles_channel == serverName:
      index = REACTION_ROLES_CHANNEL.index(roles_channel)
      reaction_roles_channel_id = REACTION_ROLES_CHANNEL[index+1]
    else:
      continue

  for rules_channel in RULES_CHANNEL:
    if rules_channel == serverName:
      index = RULES_CHANNEL.index(rules_channel)
      rules_channel_id = RULES_CHANNEL[index+1]
      rules_channel_found = True
    else:
      continue

  for card_channel in CARD_CHANNEL:
    if card_channel == serverName:
      index = CARD_CHANNEL.index(card_channel)
      card_channel_id = CARD_CHANNEL[index+1]
    else:
      continue

  for wishes_channel in WISHES_CHANNEL:
    if wishes_channel == serverName:
      index = CARD_CHANNEL.index(wishes_channel)
      wishes_channel_id = WISHES_CHANNEL[index+1]
    else:
      continue

  for gifts_channel in GIFTS_CHANNEL:
    if gifts_channel == serverName:
      index = GIFTS_CHANNEL.index(gifts_channel)
      gifts_channel_id = WISHES_CHANNEL[index+1]
      gifts_channel_found = True
    else:
      continue

  for memories_channel in MEMORIES_CHANNEL:
    if memories_channel == serverName:
      index = MEMORIES_CHANNEL.index(memories_channel)
      memories_channel_id = MEMORIES_CHANNEL[index+1]
    else:
      continue
  
  channel = bot.get_channel(welcome_channel_id)
  embed = discord.Embed(title="Welcome New User!!!!", description=f"Welcome to the {serverName} discord server <@!{member.id}>!!")
  embed.add_field(name="Please read what is below!!", value="", inline=False)
  embed.add_field(name=f"Get your roles in: <#{reaction_roles_channel_id}>!", value="", inline=False)
  embed.add_field(name=f"View the countdown here: <#{countdown_channel_id}>!", value="", inline=False)
  if rules_channel_found:
    embed.add_field(name=f"Read the rules here: <#{rules_channel_id}>!", value="", inline=False)
  embed.add_field(name=f"Sign the card here: <#{card_channel_id}>!", value="", inline=False)
  embed.add_field(name=f"Send your wishes here: <#{wishes_channel_id}>!", value="", inline=False)
  if gifts_channel_found:
    embed.add_field(name=f"Give some gifts here: <#{gifts_channel_id}>!", value="", inline=False)
  embed.add_field(name=f"Share your memories here: <#{memories_channel_id}>!", value="", inline=False)
  await channel.send(member.mention, embed=embed)


bot.run(BOT_TOKEN)
