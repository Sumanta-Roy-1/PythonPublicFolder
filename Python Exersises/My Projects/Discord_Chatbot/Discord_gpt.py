


import discord
import os
import google.generativeai as genai  #added

Dkey = os.environ["DISCORD_KEY"]
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])   #added

model = genai.GenerativeModel("gemini-1.5-flash")   #added


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        response = model.generate_content(message.content)  #added
        if self.user!= message.author:
            if self.user in message.mentions:
                channel = message.channel
                await channel.send(response.text)  #added
                # await channel.send("Hello, I am ROY!")
                

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(Dkey)