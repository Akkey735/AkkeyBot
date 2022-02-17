# coding: utf-8

"""
MIT License

Copyright (c) 2021-2022 Akkey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import nextcord
import base64
import yaml
import json

from nextcord.errors import NotFound

client = nextcord.Client(shard_count=10)
with open("config.yml", "r", encoding="utf8") as file:
	config = yaml.safe_load(file)

@client.event
async def on_ready():
	print("AkkeyBot(ServerProtect)が起動されました。")

@client.event
async def on_message(message):
	with open("amm.json", "r") as file:
		amm_guild_data = json.load(file)[str(message.guild.id)]
	try:
		amm_guild_data["amm"]
	except KeyError:
		return
	if amm_guild_data["amm"] == "1":
		if int(len(message.mentions)) > int(amm_guild_data["maxuser"]):
			await message.delete()
			if amm_guild_data["mute"] == "1":
				guild = client.get_guild(message.guild.id)
				member = guild.get_member(message.author.id)
				role = guild.get_role(int(amm_guild_data["mrole"]))
				if role == None:
					return
				try:
					await member.add_roles(role)
				except TypeError:
					return
		elif int(len(message.role_mentions)) > int(amm_guild_data["maxrole"]):
			await message.delete()
			if amm_guild_data["mute"] == "1":
				guild = client.get_guild(message.guild.id)
				member = guild.get_member(message.author.id)
				role = guild.get_role(int(amm_guild_data["mrole"]))
				if role == None:
					return
				try:
					await member.add_roles(role)
				except TypeError:
					return

client.run(config["token"])
