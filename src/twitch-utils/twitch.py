import os
import requests
from dotenv import load_dotenv
import irc.bot
import irc.strings

# Load environment variables from .env file
load_dotenv()

# Twitch API Credentials
CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
OAUTH_TOKEN = os.getenv('TWITCH_OAUTH_TOKEN')
CHANNEL = os.getenv('TWITCH_CHANNEL')

def get_oauth_token():
    # Replace these with your client ID and client secret
    CLIENT_ID = 'hof5gwx0su6owfnys0yan9c87zr6t'
    CLIENT_SECRET = '41vpdji4e9gif29md0ouet6fktd2'

    # Twitch OAuth token URL
    TOKEN_URL = 'https://id.twitch.tv/oauth2/token'

    # Parameters for the POST request
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }

    # Make the POST request to get the access token
    response = requests.post(TOKEN_URL, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON and extract the access token
        data = response.json()
        access_token = data['access_token']
        expires_in = data['expires_in']
        token_type = data['token_type']

        print(f"Access Token: {access_token}")
        print(f"Expires In: {expires_in}")
        print(f"Token Type: {token_type}")
    else:
        print(f"Failed to obtain token, status code: {response.status_code}")

class TwitchChatBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Twitch IRC server details
        server = 'irc.chat.twitch.tv'
        # port = 6667
        port =  6697
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
