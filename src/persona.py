import openai
# from openai import OpenAI
import os 
import time
from dotenv import load_dotenv
import emoji
import threading
from twitch_utils.twitch_bot import Bot
from tts_utils.eleven_labs import texttospeech
from elevenlabs import play

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

OAUTH_TOKEN = os.getenv('TWITCH_OAUTH_TOKEN')
CHANNEL = os.getenv('TWITCH_CHANNEL')
BOT_NAME = os.getenv('TWITCH_BOT_NAME')
BOT_PREFIX = os.getenv('TWITCH_BOT_PREFIX')

def play_audio():
    f = open("output.mp3", "rb")
    play(f.read())
    f.close()
    

def ask_gpt(prompt: str) -> str:
    # chat_log = [{"role": "system", "content": "You are a white British male in your late 20s, funny, with a strong passion for gaming, also deeply knowledgeable about movie culture, close to an entertainment nerd, an individual who skipped university to pursue livestreaming, taking it a step further from just a simple hobby to a full-time job. Read and react to the user chat informally and with a sense of humor."},
    #             {"role": "user", "content": prompt}]
    
    # response = openai.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=chat_log,
    #     max_tokens=150,
    # )

    # return response.choices[0].message.content 
    return "HELLO I AM VERY TIRED"


def read_chat_log(chat_log_file):
    with open(chat_log_file, "r", encoding="utf-8") as file:
        chat_log_content = file.read()
    return chat_log_content


def process_chat_log(chat_log_content):
    chat_msgs = chat_log_content.strip().split('\n')
    f = open("persona_latest_response.txt", "w")

    if chat_msgs:
        latest_msg = chat_msgs[-1]

        user, content = latest_msg.split(':', 1)
        prompt = content
        response = ask_gpt(prompt)
        print(f"{latest_msg}\nAurora: {response}\n")
        f.write(emoji.demojize(response))
        f.close()



def main() -> None:
    # openai.api_key = api_key
    # client = OpenAI(api_key=api_key)
    # openai.api_key = api_key
    # print(api_key)
    chat_log_file = 'chat.log'
    while True:
        print("Checking chat log...")
        chat_log_content = read_chat_log(chat_log_file)
        process_chat_log(chat_log_content)

        f = open("persona_latest_response.txt", "r")
        response = f.read()
        f.close()
        texttospeech(response, voice_id='EXAVITQu4vr4xnSDxMaL', stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        
        play_audio()
        
        time.sleep(10)
        return

if __name__ == "__main__":
    # Run main in a separate thread
    # thread = threading.Thread(target=main)
    # thread.start()
    main()
    # Run chat bot in main thread
    bot = Bot(token=OAUTH_TOKEN, prefix=BOT_PREFIX, initial_channels=[CHANNEL])
    bot.run()