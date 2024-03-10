import base64
import os
import requests

from dotenv import load_dotenv

load_dotenv()

engine_id = "stable-diffusion-v1-6"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
api_key = os.getenv("STABILITY_API_KEY")

img_prompt = "A British male in his late twenties wearing gamer fashion and is really into movie culture on a live stream face cam speaking to a microphone"

emotion_prompts=[("Make him angry","angry"),("Make him have a neutral expression","neutral"),("Make him sad","sad"),("Make him laugh","laughing"),("Make him confused","confused"),("Make him cringe","cringing"),("Make him excited","excited"),("Make him shocked","shocked")]

if api_key is None:
    raise Exception("Missing Stability API key.")

for i in emotion_prompts:

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/image-to-image",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        files={
            "init_image": open("./out/happy_guy.png", "rb")
        },
        data={
            "image_strength": 0.6,
            "init_image_mode": "IMAGE_STRENGTH",
            "text_prompts[0][text]": i[0],
            "cfg_scale": 30,
            "samples": 1,
            "steps": 30,
        }
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for j, image in enumerate(data["artifacts"]):
        with open(f"./out/{i[1]}_guy.png", "wb") as f:
            f.write(base64.b64decode(image["base64"]))
