REMEMBER THIS URGENT OTHER WISE NOT WORK

first do pip uninstall py-cord
Then do pip install py-cord

then put things in config.json and then work bot ok































# LinkGen Account Generator

Version 2 is coming soon. This is an open source account generator bot.

## Features
- `/generate` command
- `/help` command
- Automatic `/stock` command
- Log channel
- Generator channel
- Generator role

## Installation
1. Delete `discord.py` if it is installed.
2. LinkGen will install `Pycord` automatically.
3. Accounts folder and files will be created automatically.
4. Put your configuration in `config.json`.
5. Start the bot with `python LinkGen.py`.

Make sure to invite the bot with `applications.commands` enabled in the URL generator from the developer portal. Otherwise, the slash commands will not work.

## How it works
1. Put your Discord bot token in `config.json`.
2. Create a `Free Gen` role and a `Premium Gen` role.
3. Create a generator channel.
4. Make sure you have Python 3.9 installed.
5. Add accounts to the `/accounts` folder.

If you have any problems or suggestions, please join my support server and create a ticket: https://discord.gg/gfmmBQB4tR.

embed = discord.Embed(title=f"{service} Account Generated", description="PL GENERATOR", color=0xff00f5)
                                embed.add_field(name="Login", value=f"```{data[0]}```", inline=True)
                                embed.set_image(url="https://cdn.discordapp.com/attachments/1125454494998741086/1125709637430280252/standard.gif")
                                user = await client.fetch_user(int(ctx.author.id))
                                await user.send(embed=embed)
                                embed =discord.Embed(title="**Account Generated Successfully**", description="**Check Your Dms for The Account**", color=0xff00f5)                            
                                embed.set_image(url="https://cdn.discordapp.com/attachments/1125454494998741086/1125709637430280252/standard.gif")
                                user = await client.fetch_user(int(ctx.author.id))
                                await ctx.respond(embed=embed)

                                #to add embed



                                from discord.ext import commands
from discord.ext.commands import CommandOnCooldown
from keep_alive import keep_alive

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
    services = ["roblox", "steam", "hulu", "disney+",]
    for service in services:
        if os.path.exists(f"accounts/{service}.txt"): pass
        else:
            open(f"accounts/{service}.txt", "a").write(f"Paste {service} accounts here")
            print(f"[WARNING] No Accounts found for {service} - Creating file...")
async def options_name(ctx: discord.AutocompleteContext):
      return ["steam", "disney+", "crunchyroll",]

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
        services = ["Roblox", "Hulu", "Steam", "buffalo", "cc", "crunchyroll", "", "Disney+", ""]
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
                                embed.add_field(name="**How to generate?**", value="If you do not have permission to type here, go to <#1157969432967127050> and follow the steps", inline=True)
                                embed.add_field(name="", value="Use the </free:1157967192579657770> command to generate.", inline=False)
                                embed.add_field(name="", value="Use the </stock:1157967138968047666> command to view stock.", inline=False)
                              
                                embed.set_image(url="https://cdn.discordapp.com/attachments/1155168403301081149/1156173164318040075/ice.gif?ex=651401ab&is=6512b02b&hm=d421f905d18e7fa5d643d6dec1aa22d60f66c3c0722d88ee08c58bf0cddbfc78&")
                                user = await client.fetch_user(int(ctx.author.id))
                                await ctx.respond(embed=embed)
                                await ctx.respond("Here's your account:", ephemeral=True)
                                await ctx.respond(f"{data[0]}", ephemeral=True)
                                embed = discord.Embed(title="If You Like Our Generator", description="Then Please Vouch On <#1157959392948408422> And Send Proof On <#1157959359083589705>", color=0x272a2b)
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
        # Create an embed for the cooldown message
        await ctx.respond(f"You can't generate an account too quickly. Please wait {error.retry_after:.0f} seconds.",)