Client = discord.Client()
bot_prefix = "w."
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='type w.help'))


@client.command(pass_context=True)
async def rules(ctx):
    await client.say("""Rules:
    1. Be respectful - Be respectful to everyone in this discord.
    2. No Spam - We don't spam you, so don't spam us!
    3. Clean usernames - Keep your names clean and respectful, if your name isn't clean or
    respectful a nickname will be assigned to you!
    4. No bots allowed - Only our bots. Any unauthorized bots will be banned.""")

client.run(NDE5NDk2ODMyOTM5NTg5NjMy.DXw-pQ.5oeSUo1VHeCZzJJ0G6IDQP8sSb8)
