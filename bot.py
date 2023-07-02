import discord
import dotenv
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

prefix = "!"  
bot = commands.Bot(command_prefix=prefix,intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Medain"), status=discord.Status.do_not_disturb)
    print(f'Bot Ready : {bot.user.name}')  






@bot.event
async def on_message(message):

    # Hello cmd

    if message.content == 'hello medain':
        
        await message.channel.send('Hello! How can I help you? :face_holding_back_tears:')

    if message.content == 'Hello Medain':
        await message.channel.send('Hello How can i help you ?')
        await message.channel.send('My Commands')
        await message.channel.send('medain Help , medain bot help , medain info , medain status , medain Report')

    # Help

    if message.content == 'medain Help':
        await message.channel.send("Please report to <@&1114475917180407848>.They will assit your issue :face_with_monocle:")

    if message.content == 'Medain help':
        await message.channel.send("Please report to <@&1114475917180407848>.They will assit your issue :face_with_monocle:")    
    
    # Bot issue help

    if message.content == 'medain bot help':
        await message.channel.send("If any Issues in Bot please Report to <@&1114476458648281108>. :face_with_monocle:")

    if message.content == 'Medain Bot Help':
        await message.channel.send("If any Issues in Bot please Report to <@&1114476458648281108>. :face_with_monocle:")    

    
    # info


    if message.content == 'medain info':
        await message.channel.send("Medain Info :information_source:")
        await message.channel.send("Owner : <@754726440704147517> , <@997848260062478386> , <@896777693650108456>")
        await message.channel.send("Bot Devaloper : <@957196694393614367> .")

    if message.content == 'Medain Info':
        await message.channel.send("Medain Info :information_source:")
        await message.channel.send("Owner : <@754726440704147517> , <@997848260062478386> , <@896777693650108456>")
        await message.channel.send("Bot Developer : <@957196694393614367> .")
    

    if message.content == 'medain status':
        await message.channel.send("Todays Status :cricket:")
        await message.channel.send("Bans : 0 ")
        await message.channel.send("Reports : 0")


    if message.content == 'Medain Status':
        await message.channel.send("Todays Status :cricket:")
        await message.channel.send("Bans : 0 ")
        await message.channel.send("Reports : 0")



    if message.content == 'medain Report':
        await message.channel.send("Bot Issues ?")
        await message.channel.send("Middle Man Issues ?")


    if message.content == 'Middle Man Issues':
        await message.channel.send("Median Report :grinning:")
        await message.channel.send("If Any Issues Please Dm <@754726440704147517> ")
        await message.channel.send('Not Responding ? Forward your Issue to <@&1114475917180407848> Team .')

    if message.content == 'Bot Issues':
        await message.channel.send("Dm : <@957196694393614367> ")
        await message.channel.send("Not Responding ? Forward your Issue to <@754726440704147517>. ")

    await bot.process_commands(message)

bot.run(os.getenv('BOT_TOKEN'))
