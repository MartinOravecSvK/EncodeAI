import openai
import time
import os

openai.api_key = "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"

def ask_gpt(prompt: str) -> str:
    chat_log = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        max_tokens=150,
    )
    return response['choices'][0]['message']['content']

def read_chat_log(chat_log_file):
    with open(chat_log_file, "r", encoding="utf-8") as file:
        chat_log_content = file.read()
    return chat_log_content

def process_chat_log(chat_log_content):
    chat_msgs = chat_log_content.strip().split('/n')

def main() -> None:
    
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
