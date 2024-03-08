import base64
import os
import requests
import io

from dotenv import load_dotenv

from PIL import Image

load_dotenv()

img_prompt = "A British male in his late twenties wearing gamer fashion and is really into movie culture on a live stream face cam speaking to a microphone"

bg_prompt = "A slightly messy room of a British male in his late twenties gamer who is into movies"

image = Image.open(f"./out/{img_prompt.replace(' ','_')}.png")

image_bytes=io.BytesIO()

image.save(image_bytes,format='PNG')

image_file_object = image_bytes.getvalue()

api_key = os.getenv("CLIPDROP_API_KEY")

r = requests.post('https://clipdrop-api.co/replace-background/v1',
  files = {
    'image_file': ('car.jpg', image_file_object, 'image/png'),
    },
  data = { 'prompt': bg_prompt },
  headers = { 'x-api-key': api_key}
)

if (r.ok):
    output = base64.b64decode(r.content)
    with open(f"./out/{img_prompt.replace(' ','_')}_with_bg.png", "wb") as img_file:
        img_file.write(output)
else:
  r.raise_for_status()