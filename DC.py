import discord
import asyncio
import random
client = discord.Client()  # 'client' repräsentiert den Bot

@client.event
async def on_ready():  # wenn das Programm eingeloggt ist
    print(client.user.name)  # schreibt Namen des Bots in Konsole

@client.event
async def on_message(message):

    if message.content.lower().startswith("!hallo"):
        andworten = ["hi", "moin", "was gibt es denn?", "Guten Tag"]  # Liste mit möglichen Antworten
        await client.send_message(message.channel, random.choice(andworten))  # sendet zufällige Antwort aus Liste

    elif message.content.lower().startswith("!zahlenspiel"):
        await client.send_message(message.channel, "Willkommen beim zahlenraten\n"
                                                   "scheib eine Zahl von 1 bis 10",tts=True)
        zahl = random.randint(1, 10)  # wählt zufällige zahl zwischen 1 und 10

        richtig = False  # initialisiert Prüf-Variable


        for i in range(3):  # wiederholt drei mal (Schleife)
            msg = await client.wait_for_message(60, author=message.author)  # wartet 60 Sekunden lang auf eine neue Nachricht vom Spielpartner
            dieZahl = int(msg.content)  # konvertiert Benutzereingabe in Ganzzahl und speichert sie in Variable
            if dieZahl == zahl:  # überprüft, ob die Zahl des Nutzers der Zufallszahl entspricht
                await client.send_message(message.channel, "richtig du hast gewonnen",tts=True)
                richtig = True  # setzt Prüf-Variable auf wahr
                break  # bricht Schleife ab
            elif dieZahl < zahl:  # überprüft, ob die Zahl des Nutzers kleiner ist, als die Zufallszahl
                await client.send_message(message.channel, "etwas mehr!",tts=True)
            else:  # wenn keines der oberen zutrifft --> Zahl des Nutzers größer als Zufallszahl
                await client.send_message(message.channel, "etwas weniger!",tts=True)
        if not richtig:  # prüft anhand der Prüf-Variable, ob der Nutzer richtig geraten hat
            await client.send_message(message.channel, zahl)  # wenn nicht, wird Lösung (Zufallszahl) gesendet

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







client.run("")  # lässt den Bot laufen; TODO: Token eintragen
