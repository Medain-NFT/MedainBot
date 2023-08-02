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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="MedainNFT!"), status=discord.Status.do_not_disturb)
    print("Bot Is Online")


class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Tickets",emoji="<:points:1135400687749050439>",description="Need Help in Tickets." ),
            discord.SelectOption(label="Help ",emoji="<:points:1135400687749050439>",description="Help in Payments or Medain Guild."),
            discord.SelectOption(label="Promotions",emoji="<:points:1135400687749050439>",description="Know About Promotions."),
            discord.SelectOption(label="ChangeLogs",emoji="<:points:1135400687749050439>",description="Know About Bot Changelogs"),
            discord.SelectOption(label="Medain NFT",emoji="<:points:1135400687749050439>",description="See Our Medain NFT !")
            ]
        super().__init__(placeholder="Select a Option",max_values=1,min_values=1,options=options)
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
class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())



@bot.command()
async def medain(ctx):
    view = Select()
    await ctx.send('Hello User How can i help your Day.\nChoose a Option from the DropDown Menu 🥰', view=SelectView())

bot.run(os.getenv('tock'))
