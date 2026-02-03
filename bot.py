import discord
from discord.ext import commands
import subprocess
import os

TOKEN = "HERE IS YOUR OWN BOT TOKE"

VIENNA_PATH = r"YOUR PATH TO THE VIENNA SERVER'S ROOTFOLDER"

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} is ready")

@bot.command()
async def addbuildplate(ctx, playfab_id: str):
    """Run buildplate-importer for the player"""
    
    try:
        await ctx.send(f"⏳ Adding a buildplate for the player `{playfab_id}`...")
        
        cmd = f'cd /d "{VIENNA_PATH}" && buildplate-importer.bat {playfab_id}'
        
        process = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if "Added buildplate with ID" in process.stdout:
            await ctx.send(f"✅ Success! Buildplate added for player `{playfab_id}`")
        else:
            await ctx.send(f"✅ Adding a buildplate for the player `{playfab_id}`")
            
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

@bot.command()
async def check(ctx):
    ""Check the path""
    if os.path.exists(VIENNA_PATH):
        await ctx.send(f"✅ The path has been found: {VIENNA_PATH}")
    else:
        await ctx.send(f"❌ Path not found: {VIENNA_PATH}")

if __name__ == "__main__":
    bot.run(TOKEN)