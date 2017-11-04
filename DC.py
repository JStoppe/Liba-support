import discord
import asyncio
import random
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)

@client.event
async def on_message(message):
    if message.content.lower().startswith("!hallo"):
        andworten = ["hi", "moin", "was gibt es denn?", "Guten Tag"]
        await client.send_message(message.channel, random.choice(andworten))

    elif message.content.lower().startswith("!zahlenspiel"):
        await client.send_message(message.channel, "Willkommen beim zahlenraten\n"
                                                   "scheib eine Zahl von 1 bis 10",tts=True)
        zahl = random.randint(1, 10)

        richtig = False


        for i in range(3):
            msg = await client.wait_for_message(60, author=message.author)
            dieZahl = int(msg.content)
            if dieZahl == zahl:
                await client.send_message(message.channel, "richtig du hast gewonnen",tts=True)
                richtig = True
                break
            elif dieZahl < zahl:
                await client.send_message(message.channel, "etwas mehr!",tts=True)
            else:
                await client.send_message(message.channel, "etwas weniger!",tts=True)
        if not richtig:
            await client.send_message(message.channel, zahl)

    if message.content.lower().startswith("!coin"):
            choice = random.randint(1,2)
            if choice == 1:
                    await client.add_reaction(message,"⚫")
            elif choice == 2:
                    await client.add_reaction(message,"⚪")

    if message.content.lower().startswith("!ssp"):
            choice = random.randint(1,3)
            if choice == 1:
                 await client.send_message(message.channel, "✂ (!!weil DC das nich als reaction anhängen kann!!)️️")
            elif choice == 2:
                 await client.add_reaction(message, "🌚")
            elif choice == 3:
                 await client.add_reaction(message, "📄")

    if client.user in message.mentions:
        await client.send_message(message.channel, "schreibe `Was kannst du tommy?` um zu sehen was ich kann 🔍")

    if message.content.lower().startswith("was kannst du tommy?"):
                await client.send_message(message.channel, "Das kann ich: \n"
                                                    "- Münzenwerfen = (!coin) \n"
                                                    "- ein Zahlenspiel = (!Zahlenspil) \n "
                                                    "- Schere,Stein,Papier = (!SSP)")
    






client.run("Mzc0OTM3MjA1NjQ4NTIzMjY0.DNojkA.zNuJkkKHJQg1229U52BIeeub9EA")