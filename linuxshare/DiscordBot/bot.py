import discord
import inflect
from discord import app_commands
from discord.ext import commands
import random
from fuzzywuzzy import fuzz

numtoword = inflect.engine()


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


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  content_lower = message.content.lower()

  if 'hi' in content_lower:
    await message.channel.send('Hi there')
  elif 'hello' in content_lower:
    await message.channel.send(f'Hello <@!{message.author.id}>! Welcome')
  elif 'how are you?' in content_lower:
    await message.channel.send(
      f"I am doing good <@!{message.author.id}>, how are you doing?")

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
        await message.channel.send("Ok")

  await bot.process_commands(message)


@bot.command()
async def add(ctx, *numbers):
  result = 0
  for i in numbers:
    result += int(i)
  await ctx.send(f"The result is: {result}")


@bot.tree.command(name="hello")
async def hello(interation: discord.Interaction):
  await interation.response.send_message("Hello world", ephemeral=True)


@bot.tree.command(name="say")
@app_commands.describe(thing_to_say="what should I say?")
@app_commands.describe(channel="where should I send the message?")
async def say(interaction: discord.Interaction, thing_to_say: str, channel: discord.TextChannel):
  await interaction.response.send_message("The message is sent", ephemeral=True)
  await channel.send(thing_to_say)
  channel2 = bot.get_channel(MOD_LOG_CHANEL_ID)
  await channel2.send(f"There was a message that was sent in <#{channel.id}> with the message: {thing_to_say}")


@bot.tree.command(name="purge")
@app_commands.describe(num_of_messages_to_del="How many messages would you like me to delete?")
@app_commands.describe(channel="What channel should I delete the messages in?")
async def purge(interation: discord.Interaction, num_of_messages_to_del: int,channel: discord.TextChannel):
  await interation.response.send_message(f"I will now deleted {num_of_messages_to_del} messages in <#{channel.id}>!",ephemeral=True)
  await channel.purge(limit=int(num_of_messages_to_del))
  channel2 = bot.get_channel(MOD_LOG_CHANEL_ID)
  await channel2.send(f"There was {num_of_messages_to_del} messeges deleted in <#{channel.id}>!")


@bot.tree.command(name="send_multible_messages")
@app_commands.describe(how_many_times_to_send_message= "How many times would you like to send the message?")
@app_commands.describe(message="What would you like to say?")
@app_commands.describe(channel="What channel should I send the messages in?")
async def send_multible_messages(interation: discord.Interaction, how_many_times_to_send_message: int, message: str, channel: discord.TextChannel):
  await interation.response.send_message(f"I will now send {message} {how_many_times_to_send_message} times in <#{channel.id}>!",ephemeral=True)
  for _i in range(how_many_times_to_send_message):
    await channel.send(message)
  channel2 = bot.get_channel(MOD_LOG_CHANEL_ID)
  await channel2.send(f"There was a message that was sent {how_many_times_to_send_message} times in <#{channel.id}>! The message is: {message}"
  )


@bot.tree.command(name="poll")
@app_commands.describe(num_of_options="how many options are there(min of 2, max of 10)?")
@app_commands.describe(question="What is the question?")
@app_commands.describe(channel="Where would you like me to send the poll?")
async def poll(ctx: discord.Interaction, num_of_options: int, question: str, channel: discord.TextChannel):

  options = []
  reactions = []
  command_channel_id = ctx.channel.id
  main_channel = bot.get_channel(command_channel_id)

  for i in range(num_of_options):
    await main_channel.send(f"What is option {i + 1}?")

    def check(response_message):
      return response_message.author == ctx.user and response_message.channel == ctx.channel

    user_response = await bot.wait_for('message', check=check, timeout=60)

    if user_response:
      options.append(user_response.content)
    else:
      await main_channel.send(
          "I didn't receive a response. Exiting the poll setup.")
      return

  await main_channel.purge(limit=int(num_of_options * 2))

  unicode_emojis = {
      'one': '\U00000031\U000020E3',
      'two': '\U00000032\U000020E3',
      'three': '\U00000033\U000020E3',
      'four': '\U00000034\U000020E3',
      'five': '\U00000035\U000020E3',
      'six': '\U00000036\U000020E3',
      'seven': '\U00000037\U000020E3',
      'eight': '\U00000038\U000020E3',
      'nine': '\U00000039\U000020E3',
      'ten': '\U0001F51F'
  }

  embed = discord.Embed(title=question)
  for i in range(num_of_options):
    reactions.append(unicode_emojis.get(numtoword.number_to_words(i + 1).lower(), ''))

    embed.add_field(name=f"{reactions[i]} {options[i]}",value="",inline=False)
  pollmessage = await channel.send(embed=embed)

  for i in range(num_of_options):
    await pollmessage.add_reaction(reactions[i])


@bot.tree.command(name="dogfact")
async def dogfact(interation: discord.Interaction):

  dogfacts = []
  with open('dogfacts.txt', 'r') as dogfactslist:
    for line in dogfactslist:
      dogfacts.append(line.strip().strip('.'))
  index = random.randint(0, len(dogfacts) - 1)
  await interation.response.send_message(dogfacts[index])


bot.run(BOT_TOKEN)