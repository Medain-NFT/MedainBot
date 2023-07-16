import discord
import dotenv
import os
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from discord.ui import Button , View

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
kicked_users = {}
ban_channel_id = 1114461769235177512

prefix = "!"  
bot = commands.Bot(command_prefix=prefix,intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Medain"), status=discord.Status.do_not_disturb)
    print(f'Bot Ready : {bot.user.name}')  

@bot.event
async def on_message(message):

    # Hello cmd

    if message.content == 'Hello Medain':
        await message.channel.send('Hello How can i help?')
        await message.channel.send('My Commands')
        await message.channel.send('Medain Help , Medain bot help , Medain info , Medain status , Medain Report and Medain NFT')

    # Help

    if message.content == 'Medain Help':
        await message.channel.send("Please report to <@&1114475917180407848>.They will Assist your issue :face_with_monocle:")

    # Bot issue help

    if message.content == 'Medain bot help':
        button1 = Button(label="GitHub Report" , url="https://github.com/Medain-NFT/MedainBot/issues")
        view = View()
        view.add_item(button1)
        await message.channel.send("If any Issues in Bot please Report to <@&1114476458648281108>. :face_with_monocle: or create a Issue on Github" , view=view)


    
    # info


    if message.content == 'Medain info':
        await message.channel.send("Medain Info :information_source:")
        await message.channel.send("Owner : <@754726440704147517> , <@997848260062478386> , <@896777693650108456>")
        await message.channel.send("Bot Developer : <@957196694393614367> .")


    if message.content == 'Medain status':
        await message.channel.send("Todays Status :cricket:")
        await message.channel.send("Bans : 0 ")
        await message.channel.send("Reports : 0")



    if message.content == 'Medain Report':
        await message.channel.send("Bot Issues ?")
        await message.channel.send("Middle Man Issues ?")


    if message.content == 'Middle Man Issues':
        await message.channel.send("Median Report :grinning:")
        await message.channel.send("If Any Issues Please Dm <@754726440704147517> ")
        await message.channel.send('Not Responding ? Forward your Issue to <@&1114475917180407848> Team .')

    if message.content == 'Bot Issues':
        button2 = Button(label="Report" , url="https://github.com/Medain-NFT/MedainBot/issues")
        view = View()
        view.add_item(button2)
        await message.channel.send("Dm : <@957196694393614367> ")
        await message.channel.send("Not Responding ? Forward your Issue to <@754726440704147517>." , view=view)


    if message.content == 'Medain NFT':
        link1 = Button(label='Medain NFT' , url="https://opensea.io/collection/medain")
        view=View()
        view.add_item(link1)
        await message.channel.send("To See the Medain  NFT Collection Click the Link Below of this Message. 😀" , view=view)


    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'FuckYou' in message.content.lower():
        if not message.author.bot:
            user_id = message.author.id
            if user_id not in kicked_users:
                kicked_users[user_id] = 1
            else:
                kicked_users[user_id] += 1
                if kicked_users[user_id] >= 3:
                    await message.guild.ban(message.author, reason="Repeatedly saying the specific word")
                    ban_channel = bot.get_channel(ban_channel_id)
                    await ban_channel.send(f'{message.author.mention} has been Banned from the server for saying the Bad Word.')
                    await message.author.send("You Have Benn Baned from this Server")
                    await message.author.send("Saying Bad Word for 3 Times")
                    del kicked_users[user_id]
                    return

            await message.author.send("You said the Bad word and have been kicked from the server.")
            await message.auther.send("3 Kicks = BAN 🚧")
            await message.author.kick(reason="Said the specific word")
            await message.channel.send(f'{message.author.mention} has been kicked from the server for saying the specific word.')



    await bot.process_commands(message)

bot.run(os.getenv('BOT_TOKEN'))
