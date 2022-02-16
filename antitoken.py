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

from nextcord.errors import NotFound

client = nextcord.AutoShardedClient(shard_count=10)
with open("config.yml", "r", encoding="utf8") as file:
    config = yaml.safe_load(file)
    
async def check_token(token) {
	headers = {
		"Authorization": token
	}
	response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
	if response.status_code == 200:
		return True
	else:
		return False
}

@client.event
async def on_ready():
    print("AkkeyBot(ServerProtect)が起動されました。")

@client.event
async def on_message(message):
    unchecked_token_split = message.content.split(".")
    checked_response = await check_token(message.content)
    if message.content.startswith("mfa.") and len(unchecked_token_split) == 2:
        pass
    elif len(unchecked_token_split) == 3 and checked_response == True:
        await message.delete()
   	if int(len(message.mentions)) > 5:
   		await message.delete()
   		warning_message = await message.reply(f"<@{message.author.id}> 最大メンション数を超過しています")
   		await asyncio.sleep(5000)
   		await warning_message.delete()
   	if int(len(message.role_mentions)) > 3:
   		await message.delete()
   		warning_message = await message.reply(f"<@{message.author.id}> 最大メンション数を超過しています")
   		await asyncio.sleep(5000)
   		await warning_message.delete()

client.run(config["token"])
