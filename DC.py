import discord
import random
client = discord.Client()  # 'client' repräsentiert den Bot

@client.event
async def on_ready():  # wenn das Programm eingeloggt ist
    print(client.user.name)  # schreibt Namen des Bots in Konsole

@client.event
async def on_message(message):
    if message.content.startswith("!hallo"):
        andworten = ["hi", "moin", "was gibt es denn?", "Guten Tag"]  # Liste mit möglichen Antworten
        await client.send_message(message.channel, random.choice(andworten))  # sendet zufällige Antwort aus Liste

    elif message.content.startswith("!Zahlenspiel"):
        await client.send_message(message.channel, "willkommen beim Zahlenraten\n"
                                                   "scheib eine Zahl von 1 bis 10")
        zahl = random.randint(1, 10)  # wählt zufällige zahl zwischen 1 und 10

        richtig = False  # initialisiert Prüf-Variable


        for i in range(3):  # wiederholt drei mal (Schleife)
            msg = await client.wait_for_message(60, author=message.author)  # wartet 60 Sekunden lang auf eine neue Nachricht vom Spielpartner
            dieZahl = int(msg.content)  # konvertiert Benutzereingabe in Ganzzahl und speichert sie in Variable
            if dieZahl == zahl:  # überprüft, ob die Zahl des Nutzers der Zufallszahl entspricht
                await client.send_message(message.channel, "richtig du hast gewonnen")
                richtig = True  # setzt Prüf-Variable auf wahr
                break  # bricht Schleife ab
            elif dieZahl < zahl:  # überprüft, ob die Zahl des Nutzers kleiner ist, als die Zufallszahl
                await client.send_message(message.channel, "etwas mehr!")
            else:  # wenn keines der oberen zutrifft --> Zahl des Nutzers größer als Zufallszahl
                await client.send_message(message.channel, "etwas weniger!")

        if not richtig:  # prüft anhand der Prüf-Variable, ob der Nutzer richtig geraten hat
            await client.send_message(message.channel, zahl)  # wenn nicht, wird Lösung (Zufallszahl) gesendet


client.run("")  # lässt den Bot laufen; TODO: Token eintragen
