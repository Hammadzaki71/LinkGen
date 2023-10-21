from discord.ext import commands
from discord.ext.commands import CommandOnCooldown
from keep_alive import keep_alive
from datetime import datetime

keep_alive()

# Imports

try:
    import json, os, platform, time, discord
    from discord.ext import commands
except Exception:
    if platform.system() == "Windows": os.system("cls")
    else: os.system("clear")
    print("LinkGen uses Pycord, Try to remove discord.py when installed")
    time.sleep(3)
    if platform.system() == "Windows": os.system("cls")
    else: os.system("clear")
    print("Pycord not found - Installing...\n")
    os.system("pip install py-cord==2.0.0b4")
    os._exit(0)

client = discord.Bot()

# Check if correctly setup

if os.path.exists("accounts"): pass
else: os.mkdir("accounts")
if platform.system() == "Windows": os.system("cls")
else: os.system("clear")
try: json.loads(open("config.json", "r").read())
except Exception: print("[ERROR] Config File missing")
try:json.loads(open("config.json", "r").read())["token"]
except Exception: print("[ERROR] Discord Token not set")
try:json.loads(open("config.json", "r").read())["guild_id"]
except Exception: print("[ERROR] Guild ID not set")
try:json.loads(open("config.json", "r").read())["log_channel"]
except Exception: print("[ERROR] Log Channel not set")

# When bot is logged in

@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name}")
    print(f"Using guild: {client.guilds[0].name}")
    print("LinkGen Ready", "\n")
    await client.change_presence(activity=discord.Game(name="Space Gen 3.0"))
    try: client.guilds[0].get_role(int(json.loads(open("config.json", "r").read())["gen_role"]))
    except Exception: print("[ERROR] Gen Role not set")
    try: client.guilds[0].get_channel(int(json.loads(open("config.json", "r").read())["gen_channel"]))
    except Exception: print("[ERROR] Gen Channel not set")
    services = ["roblox", "steam",]
    for service in services:
        if os.path.exists(f"accounts/{service}.txt"): pass
        else:
            open(f"accounts/{service}.txt", "a").write(f"Paste {service} accounts here")
            print(f"[WARNING] No Accounts found for {service} - Creating file...")
async def options_name(ctx: discord.AutocompleteContext):
      return ["steam", "roblox", "dickeyes", "tiktok",]

## Define a cooldown decorator with a 2-minute (60 seconds) cooldown period
cooldown = commands.cooldown(1, 60, commands.BucketType.user)

# Generate Command

# Define a cooldown decorator with a 2-minute (60 seconds) cooldown period
@commands.cooldown(1, 60, commands.BucketType.user)
# Generate Command with Cooldown
@client.slash_command(name="free", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def generate(
  ctx: discord.ApplicationContext,
  account: discord.Option(str, autocomplete = discord.utils.basic_autocomplete(options_name)
)):
    if str(ctx.channel.id) != json.loads(open("config.json", "r").read())["gen_channel"]:
        await ctx.respond(f"You can only gen in: <#{json.loads(open('config.json', 'r').read())['gen_channel']}>", ephemeral=True)
    else:
        services = ["Roblox", "Hulu", "Steam", "buffalo", "cc", "crunchyroll", "Dickeyes", "Disney+", "tiktok"]
        for service in services:
            if account.lower() == service.lower():
                if str(json.loads(open("config.json", "r").read())["gen_role"]) in str(ctx.author.roles):
                    if os.path.exists(f"accounts/{service.lower()}.txt"):
                        with open(f"accounts/{service.lower()}.txt", "r+") as accounts:
                            data = accounts.readlines()
                            accounts.seek(0)
                            accounts.truncate()
                            accounts.writelines(data[1:])
                            try:
                                embed = discord.Embed(title="Generated Account", description=f"{ctx.author.mention} just generated a **{service}** account", color=0x272a2b)
                                embed.add_field(name="**How to generate?**", value="If you do not have permission to type here, go to <#1161242383233589250> and follow the steps", inline=True)
                                embed.add_field(name="", value="Use the </free:1159867939277766658> command to generate.", inline=False)
                                embed.add_field(name="", value="Use the </stock:1159867939277766660> command to view stock.", inline=False)
                                embed.set_footer(text="ICY GEN",icon_url="https://slate.dan.onl/slate.png")
                                embed.timestamp = datetime.utcnow()
            
                                embed.set_image(url="https://cdn.discordapp.com/attachments/1161245232730492958/1162701068740861952/standard_4.gif?ex=653ce4c0&is=652a6fc0&hm=61239f45e0fe95ea3a7a0405&")
                                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1161247216858583050/1162724043405918368/IMG_0742.jpg?ex=653cfa26&is=652a8526&hm=7e01981b7248f7fa95bff7fd5cc0007cd1fd3713d321a968fe89bbe0b21457e4&")
                                user = await client.fetch_user(int(ctx.author.id))
                                await ctx.respond(embed=embed)
                                await ctx.respond("Here's your account:", ephemeral=True)
                                await ctx.respond(f"{data[0]}", ephemeral=True)
                                embed = discord.Embed(title="If You Like Our Generator", description="Then Please Vouch On <#1161247582371201075> And Send Proof On <#1161247623995465818>", color=0x272a2b)
                                embed.set_image(url="https://cdn.discordapp.com/attachments/1155168403301081149/1156171902176481280/standard_1.gif?ex=6514007e&is=6512aefe&hm=8632771a8cf737a7b29091ecccc9390697e0c0abc501ab62945196dabe742d69&")
                                
                                user = await client.fetch_user(int(ctx.author.id))
                                await ctx.respond(embed=embed)
                            except Exception:
                                await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                    else:
                        await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                else:
                    await ctx.respond(f"You cannot gen {service}!", ephemeral=True)

# Handle cooldown error
@generate.error
async def generate_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        embed = discord.Embed(title="`❌` Error", description=f"> You can generate in this channel again {error.retry_after:.0f} seconds.", color=0xFFFFF)
        await ctx.respond(embed=embed)
        


    



# Help Command

@client.slash_command(name="help", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def help(ctx):
    embed = discord.Embed(title="ICE SUPPORT", description="Usage: /generate <service name>, /stock", color=0x46a9f0)
    embed.add_field(name="All Services", value="``nordvpn``, ``hulu``, ``expressvpn``, ``nitro``, ``creditcard``, ``spotify``, ``netflix``, ``disney``, ``minecraft``")
    embed.set_footer(text="Made by Unfps")
    await ctx.respond(embed=embed)

# Stock Command

@client.slash_command(name="stock", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def stock(ctx):
    services = ["steam", "roblox", "dickeyes", "tiktok",]
    stocklist = []
    for service in services:
        if os.path.exists(f"accounts/{service.lower()}.txt"):
            stocklist.append(f"`{service}`: `{len(open(f'accounts/{service}.txt', 'r').readlines())}` accounts")
    embed = discord.Embed(title="Stocks In free generator", description="", color=0x46a9f0)
    embed.add_field(name="", value="\n".join(stocklist))
    embed.set_footer(text="Made by maulrs_ur_great")
    await ctx.respond(embed=embed)



async def options_name(ctx: discord.AutocompleteContext):
  return ["steam", "roblox",]
## Define a cooldown decorator with a 2-minute (120 seconds) cooldown period
cooldown = commands.cooldown(1, 30, commands.BucketType.user)

# Generate Command

# Define a cooldown decorator with a 2-minute (120 seconds) cooldown period
@commands.cooldown(1, 30, commands.BucketType.user)
# Generate Command with Cooldown

#premium
@client.slash_command(name="premium", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def generate(
    ctx: discord.ApplicationContext,
    account: discord.Option(str, autocomplete = discord.utils.basic_autocomplete(options_name)
  )):
    if str(ctx.channel.id) != json.loads(open("config.json", "r").read())["pgen_channel"]:
        await ctx.respond(f"You can only gen in: <#{json.loads(open('config.json', 'r').read())['pgen_channel']}>", ephemeral=True)
    else:
        services = ["Roblox", "", "Steam", "buffalo", "cc", "crunchyroll", "", "Disney+", ""]
        for service in services:  
            if account.lower() == service.lower():
                if str(json.loads(open("config.json", "r").read())["pgen_role"]) in str(ctx.author.roles):
                    if os.path.exists(f"paccounts/{service.lower()}.txt"):
                        with open(f"paccounts/{service.lower()}.txt", "r+") as paccounts:
                            data = paccounts.readlines()
                            paccounts.seek(0)
                            paccounts.truncate()
                            paccounts.writelines(data[1:])
                            try:
                                embed = discord.Embed(title="Generated Account", description=f"{ctx.author.mention} just generated a **{service}** account", color=0x272a2b)
                                embed.add_field(name="**How to generate?**", value="If you do not have permission to type here, go to <#1161242383233589250> and follow the steps", inline=True)
                                embed.add_field(name="", value="Use the </free:1159867939277766658> command to generate.", inline=False)
                                embed.add_field(name="", value="Use the </stock:1159867939277766660> command to view stock.", inline=False)
                              
                                embed.set_image(url="https://cdn.discordapp.com/attachments/1161245232730492958/1162701068740861952/standard_4.gif?ex=653ce4c0&is=652a6fc0&hm=61239f45e0fe95ea3a7a0405&")
                                user = await client.fetch_user(int(ctx.author.id))
                                await ctx.respond(embed=embed)
                                await ctx.respond("Here's your account:", ephemeral=True)
                                await ctx.respond(f"{data[0]}", ephemeral=True)
                                embed = discord.Embed(title="If You Like Our Generator", description="Then Please Vouch On <#1161247582371201075> And Send Proof On <#1161247623995465818>", color=0x272a2b)
                                embed.set_image(url="https://cdn.discordapp.com/attachments/1155168403301081149/1156171902176481280/standard_1.gif?ex=6514007e&is=6512aefe&hm=8632771a8cf737a7b29091ecccc9390697e0c0abc501ab62945196dabe742d69&")
                                
                                user = await client.fetch_user(int(ctx.author.id))
                                await ctx.respond(embed=embed)
                            except Exception:
                                await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                    else:
                        await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                else:
                    await ctx.respond(f"You cannot gen {service}!", ephemeral=True)

# Handle cooldown error
@generate.error
async def premium(ctx, error):
    if isinstance(error, CommandOnCooldown):
        # Create an embed for the cooldown message
        embed = discord.Embed(title="Cooldown", description=f"You can't generate an account too quickly. Please wait {error.retry_after:.0f} seconds.", color=0xFF0000)
        await ctx.respond(embed=embed)

async def options_name(ctx: discord.AutocompleteContext):
      return ["2010", "2017", "2018",]
## Define a cooldown decorator with a 2-minute (60 seconds) cooldown period
cooldown = commands.cooldown(1, 30, commands.BucketType.user)

# Generate Command

# Define a cooldown decorator with a 2-minute (60 seconds) cooldown period
@commands.cooldown(1, 30, commands.BucketType.user)
# Generate Command with Cooldown
@client.slash_command(name="roblox", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def generate(
  ctx: discord.ApplicationContext,
  account: discord.Option(str, autocomplete = discord.utils.basic_autocomplete(options_name)
)):
    if str(ctx.channel.id) != json.loads(open("config.json", "r").read())["rgen_channel"]:
        await ctx.respond(f"You can only gen in: <#{json.loads(open('config.json', 'r').read())['rgen_channel']}>", ephemeral=True)
    else:
        services = ["2010", "2017", "2018",]
        for service in services:
            if account.lower() == service.lower():
                if str(json.loads(open("config.json", "r").read())["rgen_role"]) in str(ctx.author.roles):
                    if os.path.exists(f"raccounts/{service.lower()}.txt"):
                        with open(f"raccounts/{service.lower()}.txt", "r+") as raccounts:
                            data = raccounts.readlines()
                            raccounts.seek(0)
                            raccounts.truncate()
                            raccounts.writelines(data[1:])
                            try:
                                embed = discord.Embed(title="Generated Account", description=f"{ctx.author.mention} just generated a **{service}** account", color=0x272a2b)
                                embed.add_field(name="**How to generate?**", value="If you do not have permission to type here, go to <#1161242383233589250> and follow the steps", inline=True)
                                embed.add_field(name="", value="Use the </free:1159867939277766658> command to generate.", inline=False)
                                embed.add_field(name="", value="Use the </stock:1159867939277766660> command to view stock.", inline=False)
                              
                                embed.set_image(url="https://cdn.discordapp.com/attachments/1161245232730492958/1162701068740861952/standard_4.gif?ex=653ce4c0&is=652a6fc0&hm=61239f45e0fe95ea3a7a0405&")
                                user = await client.fetch_user(int(ctx.author.id))
                                await ctx.respond(embed=embed)
                                await ctx.respond("Here's your account:", ephemeral=True)
                                await ctx.respond(f"{data[0]}", ephemeral=True)
                                embed = discord.Embed(title="If You Like Our Generator", description="Then Please Vouch On <#1161247582371201075> And Send Proof On <#1161247623995465818>", color=0x272a2b)
                                embed.set_image(url="https://cdn.discordapp.com/attachments/1155168403301081149/1156171902176481280/standard_1.gif?ex=6514007e&is=6512aefe&hm=8632771a8cf737a7b29091ecccc9390697e0c0abc501ab62945196dabe742d69&")
                                
                                user = await client.fetch_user(int(ctx.author.id))
                                await ctx.respond(embed=embed)
                            except Exception:
                                await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                    else:
                        await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                else:
                    await ctx.respond(f"You cannot gen {service}!", ephemeral=True)

# Handle cooldown error
@generate.error
async def roblox(ctx, error):
    if isinstance(error, CommandOnCooldown):
        embed = discord.Embed(title="`❌` Error", description=f"> You can generate in this channel again {error.retry_after:.0f} seconds.", color=0xFFFFF)
        await ctx.respond(embed=embed)

async def options_name(ctx: discord.AutocompleteContext):
  return ["steam", "roblox", "2018",]
## Define a cooldown decorator with a 2-minute (60 seconds) cooldown period
cooldown = commands.cooldown(1, 30, commands.BucketType.user)

# Generate Command

# Define a cooldown decorator with a 2-minute (60 seconds) cooldown period
@commands.cooldown(1, 30, commands.BucketType.user)
# Generate Command with Cooldown
#premium
@client.slash_command(name="booster", guild_ids=[json.loads(open("config.json", "r").read())["guild_id"]])
async def generate(
    ctx: discord.ApplicationContext,
    account: discord.Option(str, autocomplete = discord.utils.basic_autocomplete(options_name)
  )):
    if str(ctx.channel.id) != json.loads(open("config.json", "r").read())["bgen_channel"]:
        await ctx.respond(f"You can only gen in: <#{json.loads(open('config.json', 'r').read())['bgen_channel']}>", ephemeral=True)
    else:
        services = ["Roblox", "", "Steam", "buffalo", "cc", "crunchyroll", "", "Disney+", ""]
        for service in services:  
            if account.lower() == service.lower():
                if str(json.loads(open("config.json", "r").read())["bgen_role"]) in str(ctx.author.roles):
                    if os.path.exists(f"baccounts/{service.lower()}.txt"):
                        with open(f"baccounts/{service.lower()}.txt", "r+") as baccounts:
                            data = baccounts.readlines()
                            baccounts.seek(0)
                            baccounts.truncate()
                            baccounts.writelines(data[1:])
                        try:
                            embed = discord.Embed(title="Generated Account", description=f"{ctx.author.mention} just generated a **{service}** account", color=0x272a2b)
                            embed.add_field(name="**How to generate?**", value="If you do not have permission to type here, go to <#1161242383233589250> and follow the steps", inline=True)
                            embed.add_field(name="", value="Use the </free:1159867939277766658> command to generate.", inline=False)
                            embed.add_field(name="", value="Use the </stock:1159867939277766660> command to view stock.", inline=False)

                            embed.set_image(url="https://cdn.discordapp.com/attachments/1161245232730492958/1162701068740861952/standard_4.gif?ex=653ce4c0&is=652a6fc0&hm=61239f45e0fe95ea3a7a0405&")
                            user = await client.fetch_user(int(ctx.author.id))
                            await ctx.respond(embed=embed)
                            await ctx.respond("Here's your account:", ephemeral=True)
                            await ctx.respond(f"{data[0]}", ephemeral=True)
                            embed = discord.Embed(title="If You Like Our Generator", description="Then Please Vouch On <#1161247582371201075> And Send Proof On <#1161247623995465818>", color=0x272a2b)
                            embed.set_image(url="https://cdn.discordapp.com/attachments/1155168403301081149/1156171902176481280/standard_1.gif?ex=6514007e&is=6512aefe&hm=8632771a8cf737a7b29091ecccc9390697e0c0abc501ab62945196dabe742d69&")

                            user = await client.fetch_user(int(ctx.author.id))
                            await ctx.respond(embed=embed)
                        except Exception:
                            await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
                else:
                    await ctx.respond(f"We are currently out of {service}!", ephemeral=True)
            else:
                await ctx.respond(f"You cannot gen {service}!", ephemeral=True)

# Handle cooldown error
@generate.error
async def booster(ctx, error):
  if isinstance(error, CommandOnCooldown):
    embed = discord.Embed(title="`❌` Error", description=f"> You can generate in this channel again {error.retry_after:.0f} seconds.", color=0xFFFFF)
    await ctx.respond(embed=embed)



client.run(json.loads(open("config.json", "r").read())["token"])