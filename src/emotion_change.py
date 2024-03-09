import base64
import os
import requests

from dotenv import load_dotenv

load_dotenv()

engine_id = "stable-diffusion-v1-6"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
api_key = os.getenv("STABILITY_API_KEY")

img_prompt = "A British male in his late twenties wearing gamer fashion and is really into movie culture on a live stream face cam speaking to a microphone"

emotion_prompt="Make him angry"

if api_key is None:
    raise Exception("Missing Stability API key.")

response = requests.post(
    f"{api_host}/v1/generation/{engine_id}/image-to-image",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    files={
        "init_image": open(f"./out/{img_prompt.replace(' ','_')}_with_bg.png", "rb")
    },
    data={
        "image_strength": 0.55,
        "init_image_mode": "IMAGE_STRENGTH",
        "text_prompts[0][text]": emotion_prompt,
        "cfg_scale": 14,
        "samples": 1,
        "steps": 30,
    }
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):
    with open(f"./out/{img_prompt.replace(' ','_')}_emotion_change.png", "wb") as f:
        f.write(base64.b64decode(image["base64"]))
