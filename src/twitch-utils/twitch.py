import os
from dotenv import load_dotenv
import irc.bot
import irc.strings

# Load environment variables from .env file
load_dotenv()

# Twitch API Credentials
CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
OAUTH_TOKEN = os.getenv('TWITCH_OAUTH_TOKEN')
CHANNEL = os.getenv('TWITCH_CHANNEL')

class TwitchChatBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Twitch IRC server details
        server = 'irc.chat.twitch.tv'
        port = 6667
        print(f'Connecting to {server} on port {port}...')

        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, f"oauth:{token}")], username, username)

    def on_welcome(self, c, e):
        print(f"Joining {self.channel}")

        # You must request capabilities before you can successfully join a channel
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        # Extracting the display name (nickname) and message from the tags
        display_name = e.source.split('!')[0]
        message = e.arguments[0]
        print(f"{display_name}: {message}")

if __name__ == "__main__":
    bot = TwitchChatBot(CLIENT_ID, CLIENT_ID, OAUTH_TOKEN, CHANNEL)
    bot.start()
