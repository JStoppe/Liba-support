import discord
import random
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)

@client.event
async def on_message(message):
    if message.content.startswith("!hallo"):
        andworten = ["hi", "moin", "was gibt es denn?", "Guten Tag"]
        await client.send_message(message.channel, random.choice(andworten))

    elif message.content.startswith("!Zahlenspiel"):
        await client.send_message(message.channel, "willkommen beim Zahlenraten\n"
                                                   "scheib eine Zahl von 1 bis 10")
        zahl = random.randint(1, 10)

        richtig = False


        for i in range(3):
            msg = await client.wait_for_message(60, author=message.author)
            dieZahl = int(msg.content)
            if dieZahl == zahl:
                await client.send_message(message.channel, "richtig du hast gewonnen")
                richtig = True
                break
            elif dieZahl < zahl:
                await client.send_message(message.channel, "etwas mehr!")
            else:
                await client.send_message(message.channel, "etwas weniger!")

        if not richtig:
            await client.send_message(message.channel, zahl)


client.run("")