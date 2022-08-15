
from discord.ext import commands
from python_aternos import Client, atconnect
import os

bot = commands.Bot(command_prefix="!")
print(os.environ['aternos_user'], os.environ['aternos_pass'],os.environ['server_id'], os.environ['TOKEN'])
TOKEN = os.environ['TOKEN']
ttoken= os.environ['ttoken']
# aternos=Client.from_credentials(os.environ['aternos_user'], os.environ['aternos_pass'])
# myserver=aternos.get_server(os.environ['server_id'])
sender = atconnect.AternosConnect()
sender.token=ttoken
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def startServer(ctx):
    try:
        # myserver.start()
        sender.request_cloudflare(
            url='https://aternos.org/panel/ajax/start.php', method='GET',
            params={'headstart': 0}, data=None,
            headers=None,
            reqcookies={
                'ATERNOS_SERVER': os.environ['server_id']
            },
            sendtoken=True)
    except commands.errors.CommandInvokeError:
        await ctx.send('already online')
    await ctx.send('Starting in a few seconds...') 
  
@bot.command()
async def stopServer(ctx):
    sender.request_cloudflare(
    url='https://aternos.org/panel/ajax/stop.php', method='GET',
    params={'headstart': 0}, data=None,
    headers=None,
    reqcookies={
        'ATERNOS_SERVER': os.environ['server_id']
    },
    sendtoken=True)
    await ctx.send('Stopping...') 
    
    
    
# @bot.command()
# async def status(ctx):
#     await ctx.send(myserver.status)
    
# @bot.command()
# async def infos(ctx):
#     info_string=f'''
#     Server address: {myserver.address}
    
#     players: {myserver.players_count}/{myserver.slots}:
#     {",".join(myserver.players_list)}
    
#     Minecraft {myserver.edition.name.capitalize()} Edition: {myserver.version}, {myserver.software}    
#     '''
#     await ctx.send(info_string)

if __name__ == "__main__":
    bot.run(TOKEN)
