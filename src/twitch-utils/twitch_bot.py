import os
from twitchio.ext import commands
from dotenv import load_dotenv
load_dotenv()

OAUTH_TOKEN = os.getenv('TWITCH_OAUTH_TOKEN')
CHANNEL = os.getenv('TWITCH_CHANNEL')
BOT_NAME = os.getenv('TWITCH_BOT_NAME')
BOT_PREFIX = os.getenv('TWITCH_BOT_PREFIX')

class Bot(commands.Bot):

    def __init__(self):
        # Initialize the Bot with our access token and desired prefix
        super().__init__(token=OAUTH_TOKEN, prefix=BOT_PREFIX,
                         initial_channels=[CHANNEL])

    async def event_ready(self):
        # Called once when the bot goes online
        print(f'Logged in as | {self.nick}')
        print(f'Successfully joined chat: , martin_oravec')

    async def event_message(self, message):
        # Runs whenever a message is sent in chat
        print(f'Message from {message.author.name}: {message.content}')
        await self.handle_commands(message)

# Load the bot with the access token (make sure to replace 'your_access_token_here' with your actual access token)
# You can obtain the token from the Twitch Token Generator website or through the Twitch developer console
bot = Bot()
bot.run()
