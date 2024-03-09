import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# def ask_gpt(prompt: str) -> str:
#     response = openai.chat.completions.create(
#         engine = "gpt-3.5-turbo",
#         prompt = prompt,
#         max_tokens = 4000,
#         temperature=0.5,
#         frequency_penalty=0,
#         presence_penalty=0,
#     )
#     return response.choices[0].text.strip()

def ask_gpt(prompt: str) -> str:
    # change this for the entire hisotry of the chat
    chat_log = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        max_tokens=100,
    )
    return response['choices'][0]['message']['content']

def main():
    
    print("This is Aurora speaking! Type 'quit' if I have triggered you too much.")
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
