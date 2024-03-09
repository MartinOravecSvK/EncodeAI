import openai
import os 
import time
from dotenv import load_dotenv
import emoji
import playsound
from tts_utils.eleven_labs import texttospeech

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def ask_gpt(prompt: str) -> str:
    chat_log = [{"role": "system", "content": "You are a white British male in your late 20s, funny, with a strong passion for gaming, also deeply knowledgeable about movie culture, close to an entertainment nerd, an individual who skipped university to pursue livestreaming, taking it a step further from just a simple hobby to a full-time job. Read and react to the user chat informally and with a sense of humor."},
                {"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        max_tokens=150,
    )
    return response.choices[0].message.content 


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
        response = emoji.demojize(ask_gpt(prompt))
        print(f"{latest_msg}\nAurora: {response}\n")
        
        texttospeech(response)
        playsound.playsound('output.mp3')
        f.write(response)
        f.close()


def main() -> None:
    
    chat_log_file = 'chat.log'
    while True:
        chat_log_content = read_chat_log(chat_log_file)
        process_chat_log(chat_log_content)
        time.sleep(10)

if __name__ == "__main__":
    main()
