import discord
from discord import app_commands
from discord.ext import commands



def read_bot_token():
  with open('token.txt', 'r') as file:
    return file.read().strip()


BOT_TOKEN = read_bot_token()
SERVER_ID = 976614776606167060
REACTION_ROLES_CHANNEL_ID = 1215753069522976911
REACTION_ROLES_EMOJIS = []
REACTION_ROLES_ROLE_NAMES = []


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
  print("Hello world")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

@bot.tree.command(name="hello")
async def hello(interation: discord.Interaction):
  await interation.response.send_message("Hello world", ephemeral=True)


@bot.tree.command(name="say")
@app_commands.describe(thing_to_say="what should I say?")
@app_commands.describe(channel="where should I send the message?")
async def say(interaction: discord.Interaction, thing_to_say: str, channel: discord.TextChannel):
  await interaction.response.send_message("The message is sent", ephemeral=True)
  await channel.send(thing_to_say)
  


@bot.tree.command(name="purge")
@app_commands.describe(num_of_messages_to_del="How many messages would you like me to delete?")
@app_commands.describe(channel="What channel should I delete the messages in?")
async def purge(interation: discord.Interaction, num_of_messages_to_del: int, channel: discord.TextChannel):
  await interation.response.send_message(f"I will now deleted {num_of_messages_to_del} messages in <#{channel.id}>!", ephemeral=True)
  await channel.purge(limit=int(num_of_messages_to_del))

@bot.tree.command(name="dmuser")
@app_commands.describe(user="What user would you like to send the message to?")
@app_commands.describe(message="What would you like to say?")
async def dmuser(interation: discord.Interaction, user: discord.User, message: str):
  await interation.response.send_message(f"I will now send a message to {user.mention}!", ephemeral=True)
  await user.send(message)

@bot.tree.command(name="sendembedmessage")
@app_commands.describe(title="What is the title of the embed?")
@app_commands.describe(description="What is the description of the embed?")
@app_commands.describe(channel="Where should I send the embed?")
async def sendembedmessage(interation: discord.Interaction, title: str, description: str, channel: discord.TextChannel):
  embed = discord.Embed(title=title)
  message = await channel.send(embed=embed)
  await message.add_reaction('😄')


@bot.tree.command(name="reactionroles")
@app_commands.describe(channel="Where should I send the reaction roles?")
@app_commands.describe(roles="How many roles are there?")
async def reactionroles(ctx: discord.Interaction, channel: discord.TextChannel, roles: int):

  emojis = []
  role_names = []
  command_channel_id = ctx.channel.id
  main_channel = bot.get_channel(command_channel_id)
  

  for i in range(roles):
    await main_channel.send(f"What is the emoji for role {i+1}?")
    def check(response_message):
      return response_message.author == ctx.user and response_message.channel == ctx.channel

    user_response = await bot.wait_for('message', check=check, timeout=60)
    if user_response:
      emojis.append(user_response.content)
      REACTION_ROLES_EMOJIS.append(user_response.content)
    else:
      await main_channel.send("I didn't receive a response. Exiting the poll setup.")
      return
    
    await main_channel.send(f"What is the the role name for that emoji that you just gave me?")
    def check(response_message):
      return response_message.author == ctx.user and response_message.channel == ctx.channel

    user_response = await bot.wait_for('message', check=check, timeout=60)
    if user_response:
      role_names.append(user_response.content)
      REACTION_ROLES_ROLE_NAMES.append(user_response.content)
    else:
      await main_channel.send("I didn't receive a response. Exiting the poll setup.")
      return

  await main_channel.purge(limit=int(roles * 4))

  
  embed = discord.Embed(title="Get your roles here!")
  for i in range(roles):
    embed.add_field(name=f"{emojis[i]} {role_names[i]}", value="", inline=False)
  rolesmessage = await channel.send(embed=embed)
  for emoji in emojis:
    await rolesmessage.add_reaction(f'{emoji}')

@bot.event
async def on_raw_reaction_add(payload):
  reaction = payload.emoji  # Get the emoji object
  user = payload.member
  message = payload.message_id
  channel = bot.get_channel(payload.channel_id)

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
  message = payload.message_id
  channel = bot.get_channel(payload.channel_id)
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


bot.run(BOT_TOKEN)
