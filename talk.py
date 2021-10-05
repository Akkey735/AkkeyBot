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
print("[StartUp]モジュール「nextcord」をインポートしました")
import yaml
print("[StartUP]モジュール「yaml」をインポートしました")

client = nextcord.Client()
with open("config.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)
print("[StartUP]config.ymlをロードしました")

@client.event
async def on_ready():
    version = config["version"]
    print("Bot has been launch")
    print(f"Bot version is {version}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if "おは" in message.content:
        await message.channel.send("おはよう...うちはもうちょっと寝てるわ...")
        return
    elif "おや" in message.content:
        await message.channel.send("おやすみーあ、まだ起きてるから電機はそのままで...")
        return
    elif "@everyone" in message.content:
        await message.channel.send("うるさいなぁ...今寝てたんだけど?")
        return
    elif "@here" in message.content:
        await message.channel.send("ちょっとうるさい...やっと寝れそうだったのに...")
        return
    else:
        pass

client.run(config["token"])
