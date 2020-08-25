import discord
import os
import random
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

points = dict()

with open("points.json") as json_file:
	points = json.load(json_file)

bot = commands.Bot(command_prefix='/')
bot.remove_command('help') #Override the help function


def get_praise(username: str):
	praises = [
		"There’s ordinary. And then there’s " + username + ".",
		"In high school, I bet " + username + " was voted \"most likely to keep being awesome.\"",
		"On a scale of 1 to 10, " + username + " is an 11.",
		username + " embodies all the best qualities of each Hogwarts house, rolled into one.",
		username + " is like a corner piece of a jigsaw puzzle. Without them, I would be lost.",
		"Hey " + username + ", is there anything you can’t do?",
		username + "never fails to amaze me with their diligence.",
		"If " + username + " were a vegetable, they would be a cute-cumber.",
		"You Know What’s Awesome? Chocolate Cake, Oh And " + username+ "\'s Face.",
		"Aside from food, " + username + " is my Favorite.",
		"If they based a movie on " + username + ", it would win an oscar because they are that incredible.",
		username + " could survive a zombie apocalypse because they are that badass.",
		"I can never remember my dreams, but I assure you that" + username + " is always in them.",
		"I know it's cheesy, but I think " + username + " is grate.",
		username + " is the only person I would trust with my passwords.",
		username + " is more fun than a ball pit filled with candy.",
	]

	return praises[random.randint(0, len(praises) - 1)]

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send("Invalid user, please enter the username of someone from this server!")

@bot.command(name='praise')
async def praise(ctx, member: discord.Member = None):

	print(str(member))

	# List kudos
	# List all kudos you've ever gotten, and if there are none, send them some praise!

	if member:
		if str(member) in points:
			points[str(member)] += 1
		else:
			points[str(member)] = 1

		with open("points.json", 'w') as file:
			json.dump(points, file)

		praise = get_praise(member.name.capitalize())
		pts = ""

		if points[str(member)] > 20:
			pts = "way too many"
		else:
			pts = str(points[str(member)])

		await ctx.send(praise + f" Nice! {member.mention} now at {pts} points.")

@bot.command(name='help')
async def help(ctx):
	await ctx.send("This bot enables you to send praise towards someone who you believe deserves it. Simply type `!praise <name-of-user>` to do so!")

bot.run(TOKEN)
