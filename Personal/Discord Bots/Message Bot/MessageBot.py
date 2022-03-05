import discord
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        user_id = "677639888102752266"
        channel = client.get_channel(881220579708002377)
        await channel.send(f"<@{user_id}>Hello Mr. Schmitt, I am online and ready to assist you.")

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('OTQ5NDkzMDAyMTMxMzc0MDkw.YiLKRA.psuWXMCbSeOfY2FXTO3ezKGwmdI')