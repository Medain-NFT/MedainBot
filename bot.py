import discord
import os
import dotenv

from discord.ui import Select , View 
from discord.ext import commands 
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
prefix = "!"  
bot = commands.Bot(command_prefix=prefix,intents=intents)



# Bot Triggers

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Medain Multiverse"), status=discord.Status.idle)
    print("Bot Is Online")





embed=discord.Embed(title="Help Wizard ", url="https://github.com/Medain-NFT", description="Hello, I am Medain Assist and i am Super Glad to help you . Choose a Option from this Embed Message and i will provide you the Help ", color=0xf67104)
embed.set_author(name="Medain Network")
embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1101145432941404166/1139544491716526253/dcku_004.png")
embed.add_field(name="Help ", value="Help in any Other Stuffs", inline=True)
embed.add_field(name="Promotions", value="Are you looking to promote your product or service, regardless of its size? Look no further! We have you covered. Our advertising plans are designed to meet your needs, starting from just a day of promotion. We offer three comprehensive plans to help you reach your target audience effectively.", inline=True)
embed.add_field(name="ChangeLogs", value="A Clear Change Log list of Medain Assitent Bot and Medain Guard Bot ", inline=True)
embed.add_field(name="Medain NFT", value="Explore our Medain NFT by purchasing our NFT Collection in Open Sea ", inline=True)
embed.add_field(name="Medain Status ", value="Explore our Status Page to Ensure that our Bot is Working Properly and Smoothly To use just type `!medainstatus`", inline=True)
embed.add_field(name="Collab", value="You can Collab the Bot by adding more functions and New Stuffs for the bot .", inline=True)
embed.set_footer(text="This Embed is Prepared and hooked into the bot in 11/8/2023")


class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Tickets",emoji="<:Ticket:1139953355070898296>",description="Need Help in Tickets." ),
            discord.SelectOption(label="Help ",emoji="<:help:1139953548063412284>",description="Help in Payments or Medain Guild."),
            discord.SelectOption(label="Promotions",emoji="<:Promotions:1139954508575801425>",description="Know About Promotions."),
            discord.SelectOption(label="ChangeLogs",emoji="<:logs:1140679922067701810>",description="Know About Bot Changelogs"),
            discord.SelectOption(label="Medain NFT",emoji="<:cripto:1140680107762139188>",description="See Our Medain NFT !"),
            discord.SelectOption(label="Collab",emoji="<:collaborazioni:1142128813690589264>",description="You add more Functions to the Bot By Collab in Github.")
            ]
        super().__init__(placeholder="Select a Help Service",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Tickets":
            await interaction.response.send_message(content=" <#1130396102772916297> Read our Guildes. If There is a Issue contact <@&1126118005760327684>",ephemeral=True)
        elif self.values[0] == "Help":
            await interaction.response.send_message("Create a Ticket in <#1126514356268584970>. If it is a Bot Issue please create a New Ticket from <#1126118006515318795> .",ephemeral=True)
        elif self.values[0] == "Promotions":
            await interaction.response.send_message("Are you looking to promote your product or service? .😁 Choose a plan in <#1126543699791327333>.",ephemeral=True)
        elif self.values[0] == "ChangeLogs":
            await interaction.response.send_message(" See the Change Logs : https://github.com/Medain-NFT/MedainBot/releases\n Updated and Maintained by : <@957196694393614367>.")
        elif self.values[0] == "Medain NFT":
            await interaction.response.send_message("Medain NFT Collection \n Link : https://opensea.io/collection/medain")
        elif self.values[0] == "Collab":
            await interaction.response.send_message("Hello There User Seems that You wanted to collab me . Your Collab Makes this bot More Good and Safe Bot For the Community . \n **How to Contribute**\n- You can Contribute the Bot By forking the Repo \n - Make Changes to File and Add some new Functions \n - Send a Pull Request in Gihub \n  **Note** \n - Please Note all the Changes in the Pull Requset Message So that Devs Can Understand the Changes Properly . ")
class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())


@bot.command()
async def medain(ctx):
    
    view = Select()
    await ctx.send(embed=embed,view=SelectView())




@bot.command()
async def medainstatus(ctx):
    emoji = bot.get_emoji(1139954508575801425)
    await ctx.send(f'To See our Latest Status just Visit our Status Page {emoji} \n https://medainbot.statuspage.io/')


bot.run(os.getenv('tock'))
