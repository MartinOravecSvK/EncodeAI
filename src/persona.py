import openai
import os 
from dotenv import load_dotenv

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

def main() -> None:
    
    print("This is Aurora speaking! Type 'quit' if I have triggered you too much...!")
    user_input = ""
    chat_history = ""

    while user_input.lower() != "quit":
        user_input = input("Chat: ")
        if user_input.lower() == "quit":
            break
        prompt = f"{chat_history}Chat: {user_input}\nAurora: "
        response = ask_gpt(prompt)
        print("Aurora:", response)
        chat_history += f"Chat: {user_input}\nAurora: {response}\n"

    with open("chat_history.txt", "w", encoding="utf-8") as file:
        file.write(chat_history)

if __name__ == "__main__":
    main()
