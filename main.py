import requests
import os
from twitchio.ext import commands
from selenium import webdriver

OAUTH_TOKEN = os.environ.get('twitch_api_secret')
account_username = os.environ.get('BOT_USERNAME')
BOT_USERNAME = account_username
CHANNEL_NAME = account_username
DRIVER_PATH = 'chromedriver.exe'

cookie = webdriver.Chrome(DRIVER_PATH)
cookie.get(url='https://orteil.dashnet.org/cookieclicker/')
big_cookie = cookie.find_element_by_id('bigCookie')


def click_cookie():
    big_cookie.click()


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=OAUTH_TOKEN, prefix='!', initial_channels=[CHANNEL_NAME])

    async def event_ready(self):
        print(f'Logged in as {self.nick}')

    async def event_message(self, message):
        if message.echo:
            return
        print(message.content)
        await self.handle_commands(message)
        click_cookie()

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}')

    @commands.command()
    async def click(self, ctx: commands.Context):
        click_cookie()


bot = Bot()
bot.run()
