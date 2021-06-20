"""
A Discord bot detecting dirty words and suggesting alternatives.

Language supported :
    - French    :   detection and suggestion
    - English   :   detection
"""

import discord
from dirty_word_detector import DirtyWordDetector

# enter here your bot token
BOT_TOKEN = ""

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    dw = DirtyWordDetector()
    for word in message.content.split(" "):
        word = word.lower()
        if dw.is_dirty(word):
            suggestions = dw.get_undirty_synonyms(word)
            await message.channel.send(f"Le mot {word} est vulgaire, je te conseille d'utiliser plutot : {', '.join(suggestions)}.")

if __name__ == "__main__":
    client.run(BOT_TOKEN)
