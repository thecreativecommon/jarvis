import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def test(ctx):
	await ctx.send("Hello there!")

@bot.event
async def on_ready():
	# keeps track of how many servers it is in
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("Jarvis is in " + str(guild_count) + " Discord Servers.")

@bot.event
async def on_member_join(member):
	# TODO: Greet new members with information about TCC
	pass






DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(DISCORD_TOKEN)

