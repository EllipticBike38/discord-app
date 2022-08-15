
from discord.ext import commands
from python_aternos import Client
import credentials

bot = commands.Bot(command_prefix="!")
TOKEN = credentials.TOKEN
aternos = Client.from_credentials(credentials.aternos_user, credentials.aternos_pass)
myserver=aternos.get_server(credentials.server_id)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def startServer(ctx):
    try:
        myserver.start()
    except commands.errors.CommandInvokeError:
        await ctx.send('already online')
    await ctx.send('Starting in a few seconds...') 
  
@bot.command()
async def stopServer(ctx):
    myserver.stop()
    await ctx.send('Stopping...') 
    
    
    
@bot.command()
async def status(ctx):
    await ctx.send(myserver.status)
    
@bot.command()
async def infos(ctx):
    info_string=f'''
    Server address: {myserver.address}
    
    players: {myserver.players_count}/{myserver.slots}:
    {",".join(myserver.players_list)}
    
    Minecraft {myserver.edition.name.capitalize()} Edition: {myserver.version}, {myserver.software}    
    '''
    await ctx.send(info_string)

if __name__ == "__main__":
    bot.run(TOKEN)
