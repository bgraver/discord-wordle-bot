import discord
import json
import command


with open('config.json') as f:
    file = json.load(f)

client = discord.Client()

square_list = ['🟩', '🟨', '⬛', '⬜']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    ret = command.handle_command(message)
    print(message.author)
    if ret != '':
        if ret == 'Valid':
            await message.add_reaction('👍')
        else:
            await message.add_reaction('👎')
client.run(file['token'])

