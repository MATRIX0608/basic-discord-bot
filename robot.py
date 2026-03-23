import discord
import asyncio# it use to do multiple task without stucking
import os
from dotenv import load_dotenv
load_dotenv()

#intents is a permission  that tell discord what bot is allow to do 
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
#intent mean permission

# discord bot 
client = discord.Client(intents=intents)


guild = None
channel1 = None

async def loop():
    while True:
        if guild is None:
         await asyncio.sleep((2))
         continue
        a = open("H:\\code\\c+++\\c+\\.vscode\\repo\\discordbot\\command.txt","r")
        d = a.read()
        a.close()
        if d == "JOIN_VC": 
            await channel1.connect()
            s = open("H:\\code\\c+++\\c+\\.vscode\\repo\\discordbot\\status.txt","w")
            s.write("succesfully join")
            s.close()
        

        if d.startswith("SEND:"):
             m = d[5:]
             await channel1.send(m)
             l = open("H:\\code\\c+++\\c+\\.vscode\\repo\\discordbot\\status.txt","w")
             l.write("successfully send")
             l.close()

        if d.startswith("BAN:"):
            id = d[4:]
            for member in guild.members:
                if member.name == id:
                  await member.ban()
                  n = open("H:\\code\\c+++\\c+\\.vscode\\repo\\discordbot\\status.txt","w")
                  n.write("succesfully ban")
                  n.close()
                  break

        if d.startswith("DM:"):
             parts = d.split(":")
             part1 = parts[1]
             part2 = parts[2]
             for member in guild.members:
              if member.name == part1:    
               await member.send(part2)
               b = open("H:\\code\\c+++\\c+\\.vscode\\repo\\discordbot\\status.txt","w")
               b.write("succesfully dm")
               b.close()
               break

        await asyncio.sleep(2)


@client.event
async def on_ready():
    print("ready")
    asyncio.ensure_future(loop())


@client.event
async def on_message(message):
    global guild
    guild = message.guild

    if message.author == client.user:
        return
    if message.guild is None:
      return # ignore DMs to bot

    
    if message.content.startswith("!join"):
        global channel1
        channel1 = message.author.voice.channel
        await channel1.connect()
        await message.channel.send("bot success fuly joined")

    if message.content.startswith("!send"):
        text = message.content[6:]
        await message.channel.send(text)

    if message.content.startswith("!ban"):
        text = message.content[5:]
        global member
        for member in message.guild.members:
            if member.name == text:
              await member.ban()
              break

    if message.content.startswith("!dm"):
        text = message.content[4:]
        parts = text.split(" ")
        username = parts[0]
        dm_text = " ".join(parts[1:])
        for member in message.guild.members:
            if member.name == username:
                await member.send(dm_text)
                break    

t = os.getenv("token")



client.run(t)
