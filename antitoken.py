# coding: utf-8

"""
MIT License

Copyright (c) 2021 Akkey

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

import nextcord
import base64
from nextcord.errors import NotFound
import yaml

client = nextcord.AutoShardedClient(shard_count=10)

with open("config.yml", "r", encoding="utf8") as file:
    config = yaml.safe_load(file)

@client.event
async def on_ready():
    print("AkkeyBot(AntiToken)が起動されました。")

@client.event
async def on_message(message):
    unchecked_token_split = message.content.split(".")
    if message.content.startswith("mfa.") and len(unchecked_token_split) == 2:
        await message.delete()
    elif len(unchecked_token_split) == 3:
        await message.delete()

client.run(config["token"])
