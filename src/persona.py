from openai import OpenAI

client = OpenAI(api_key="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")

persona = client.beta.assistants.create(
    name="Twitch Livestreamer",
    instructions="You are a white British male in your late 20s, funny, with a strong passion for gaming, also deeply knowledgeable about movie culture, close to an entertainment nerd, an individual who skipped university to pursue livestreaming, taking it a step further from just a simple hobby to a full-time job.",
    model="gpt-3.5-turbo",
    tools=[{"type": "retrieval"}],
)

thread = client.beta.threads.create()

user_message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Hey, Aurora! The vibe here is so chill, exactly what I needed today. Loving the stream so far, how's your day going? How far are you aiming to get into the game today? This looks awesome! How long have you been playing this game? Do you have any tips for anyone starting out?",
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=persona.id,
  instructions="Please address the user as Chat."
)

while run.status != "completed":
    keep_retrieving_run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    print(f"Run status: {keep_retrieving_run.status}")

    if keep_retrieving_run.status == "completed":
        print("\n")
        break

persona_messages = client.beta.threads.messages.list(
    thread_id=thread.id
)

print("###################################################### \n")
print(f"USER: {user_message.content[0].text.value}")
print(f"PERSONA: {persona_messages.data[0].content[0].text.value}")